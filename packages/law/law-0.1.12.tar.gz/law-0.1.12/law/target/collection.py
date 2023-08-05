# coding: utf-8

"""
Collections that wrap multiple targets.
"""

__all__ = [
    "TargetCollection", "FileCollection", "SiblingFileCollection", "NestedSiblingFileCollection",
]


import types
import random
from contextlib import contextmanager

import six

from law.config import Config
from law.target.base import Target
from law.target.file import FileSystemTarget, FileSystemDirectoryTarget, localize_file_targets
from law.target.local import LocalDirectoryTarget
from law.util import colored, flatten, map_struct
from law.logger import get_logger


logger = get_logger(__name__)


class TargetCollection(Target):
    """
    Collection of arbitrary targets.
    """

    def __init__(self, targets, threshold=1.0, **kwargs):
        if isinstance(targets, types.GeneratorType):
            targets = list(targets)
        elif not isinstance(targets, (list, tuple, dict)):
            raise TypeError("invalid targets, must be of type: list, tuple, dict")

        super(TargetCollection, self).__init__(**kwargs)

        # store targets and threshold
        self.targets = targets
        self.threshold = threshold

        # store flat targets per element in the input structure of targets
        if isinstance(targets, (list, tuple)):
            gen = (flatten(t) for t in targets)
        else:  # dict
            gen = ((k, flatten(t)) for k, t in six.iteritems(targets))
        self._flat_targets = targets.__class__(gen)

        # also store an entirely flat list of targets for simplified iterations
        self._flat_target_list = flatten(targets)

    def __len__(self):
        return len(self.targets)

    def __getitem__(self, key):
        return self.targets[key]

    def __iter__(self):
        # explicitly disable iterability enabled by __getitem__ as per PEP234
        # to (e.g.) prevent that flatten() applies to collections
        raise TypeError("'{}' object is not iterable".format(self.__class__.__name__))

    def _copy_kwargs(self):
        kwargs = super(TargetCollection, self)._copy_kwargs()
        kwargs["threshold"] = self.threshold
        return kwargs

    def _repr_pairs(self):
        return Target._repr_pairs(self) + [("len", len(self)), ("threshold", self.threshold)]

    def _iter_flat(self, keys=False):
        # prepare the generator for looping
        if isinstance(self._flat_targets, (list, tuple)):
            gen = enumerate(self._flat_targets)
        else:  # dict
            gen = six.iteritems(self._flat_targets)

        # loop and yield
        for key, targets in gen:
            yield (key, targets) if keys else targets

    def iter_existing(self, keys=False):
        for key, targets in self._iter_flat(keys=True):
            if all(t.exists() for t in targets):
                yield (key, targets) if keys else targets

    def iter_missing(self, keys=False):
        for key, targets in self._iter_flat(keys=True):
            if any(not t.exists() for t in targets):
                yield (key, targets) if keys else targets

    def keys(self):
        if isinstance(self._flat_targets, (list, tuple)):
            return list(range(len(self)))
        else:  # dict
            return list(self._flat_targets.keys())

    def uri(self, *args, **kwargs):
        return flatten(t.uri(*args, **kwargs) for t in self._flat_target_list)

    @property
    def first_target(self):
        if not self._flat_target_list:
            return None

        return flatten_collections(self._flat_target_list)[0]

    def remove(self, silent=True):
        for t in self._flat_target_list:
            t.remove(silent=silent)

    def _abs_threshold(self):
        if self.threshold < 0:
            return 0
        elif self.threshold <= 1:
            return len(self) * self.threshold
        else:
            return min(len(self), max(self.threshold, 0.0))

    def exists(self, count=None):
        threshold = self._abs_threshold()

        # trivial case
        if threshold == 0:
            return True

        # when a count was passed, simple compare with the threshold
        if count is not None:
            return count >= threshold

        # simple counting with early stopping criteria for both success and fail
        n = 0
        for i, targets in enumerate(self._iter_flat()):
            if all(t.exists() for t in targets):
                n += 1
                if n >= threshold:
                    return True

            if n + (len(self) - i - 1) < threshold:
                return False

        return False

    def count(self, existing=True, keys=False):
        # simple counting
        n = 0
        existing_keys = []
        for key, targets in self._iter_flat(keys=True):
            if all(t.exists() for t in targets):
                n += 1
                existing_keys.append(key)

        if existing:
            return n if not keys else (n, existing_keys)
        else:
            n = len(self) - n
            missing_keys = [key for key in self.keys() if key not in existing_keys]
            return n if not keys else (n, missing_keys)

    def random_target(self):
        if isinstance(self.targets, (list, tuple)):
            return random.choice(self.targets)
        else:  # dict
            return random.choice(list(self.targets.values()))

    def map(self, func):
        """
        Returns a copy of this collection with all targets being transformed by *func*.
        """
        return self.__class__(map_struct(func, self.targets), **self._copy_kwargs())

    def status_text(self, max_depth=0, flags=None, color=False, exists=None):
        count, existing_keys = self.count(keys=True)
        exists = count >= self._abs_threshold()

        if exists:
            text = "existent"
            _color = "green"
        else:
            text = "absent"
            _color = "red" if not self.optional else "dark_grey"

        text = colored(text, _color, style="bright") if color else text
        text += " ({}/{})".format(count, len(self))

        if flags and "missing" in flags and count != len(self):
            missing_keys = [str(key) for key in self.keys() if key not in existing_keys]
            text += ", missing branches: " + ",".join(missing_keys)

        if max_depth > 0:
            if isinstance(self.targets, (list, tuple)):
                gen = enumerate(self.targets)
            else:  # dict
                gen = six.iteritems(self.targets)

            for key, item in gen:
                text += "\n{}: ".format(key)

                if isinstance(item, TargetCollection):
                    t = item.status_text(max_depth=max_depth - 1, color=color)
                    text += "\n  ".join(t.split("\n"))
                elif isinstance(item, Target):
                    t = item.status_text(color=color, exists=key in existing_keys)
                    text += "{} ({})".format(t, item.repr(color=color))
                else:
                    t = self.__class__(item).status_text(max_depth=max_depth - 1, color=color)
                    text += "\n   ".join(t.split("\n"))

        return text


class FileCollection(TargetCollection):
    """
    Collection of targets that represent files or other FileCollection's.
    """

    def __init__(self, *args, **kwargs):
        TargetCollection.__init__(self, *args, **kwargs)

        # check if all targets are either FileSystemTarget's or FileCollection's
        for t in self._flat_target_list:
            if not isinstance(t, (FileSystemTarget, FileCollection)):
                raise TypeError("FileCollection's only wrap FileSystemTarget's and other "
                    "FileCollection's, got {}".format(t.__class__))

    @contextmanager
    def localize(self, *args, **kwargs):
        # when localizing collections using temporary files, it makes sense to put
        # them all in the same temporary directory
        tmp_dir = kwargs.get("tmp_dir")
        if not tmp_dir:
            tmp_dir = LocalDirectoryTarget(is_tmp=True)
        kwargs["tmp_dir"] = tmp_dir

        # enter localize contexts of all targets
        with localize_file_targets(self.targets, *args, **kwargs) as localized_targets:
            # create a copy of this collection that wraps the localized targets
            yield self.__class__(localized_targets, **self._copy_kwargs())


class SiblingFileCollection(FileCollection):
    """
    Collection of targets that represent files which are all located in the same directory.
    Specifically, the performance of :py:meth:`exists` and :py:meth:`count` can greatly improve with
    respect to the standard :py:class:`FileCollection` as the directory listing is used internally.
    This is especially useful for large collections of remote files.
    """

    @classmethod
    def from_directory(cls, directory, **kwargs):
        # dir should be a FileSystemDirectoryTarget or a string, in which case it is interpreted as
        # a local path
        if isinstance(directory, six.string_types):
            d = LocalDirectoryTarget(directory)
        elif isinstance(d, FileSystemDirectoryTarget):
            d = directory
        else:
            raise TypeError("directory must either be a string or a FileSystemDirectoryTarget "
                "object, got '{}'".format(directory))

        # find all files, pass kwargs which may filter the result further
        kwargs["type"] = "f"
        basenames = d.listdir(**kwargs)

        # convert to file targets
        targets = [d.child(basename, type="f") for basename in basenames]

        return cls(targets)

    def __init__(self, *args, **kwargs):
        FileCollection.__init__(self, *args, **kwargs)

        # find the first target and store its directory
        if self.first_target is None:
            raise Exception("{} requires at least one file target".format(self.__class__.__name__))
        self.dir = self.first_target.parent

        # check that targets are in fact located in the same directory
        for t in flatten_collections(self._flat_target_list):
            if t.dirname != self.dir.path:
                raise Exception("{} {} is not located in common directory {}".format(
                    t.__class__.__name__, t, self.dir))

    def _repr_pairs(self):
        expand = Config.instance().get_expanded_boolean("target", "expand_path_repr")
        dir_path = self.dir.path if expand else self.dir.unexpanded_path
        return TargetCollection._repr_pairs(self) + [("fs", self.dir.fs.name), ("dir", dir_path)]

    def iter_existing(self, keys=False):
        basenames = self.dir.listdir() if self.dir.exists() else None
        for key, targets in self._iter_flat(keys=True):
            if basenames and all(t.basename in basenames for t in flatten_collections(targets)):
                yield (key, targets) if keys else targets

    def iter_missing(self, keys=False):
        basenames = self.dir.listdir() if self.dir.exists() else None
        for key, targets in self._iter_flat(keys=True):
            if (
                basenames is None or
                any(t.basename not in basenames for t in flatten_collections(targets))
            ):
                yield (key, targets) if keys else targets

    def exists(self, count=None, basenames=None):
        threshold = self._abs_threshold()

        # trivial case
        if threshold == 0:
            return True

        # when a count was passed, simple compare with the threshold
        if count is not None:
            return count >= threshold

        # check the dir
        if not self.dir.exists():
            return False

        # get the basenames of all elements of the directory
        if basenames is None:
            basenames = self.dir.listdir()

        # simple counting with early stopping criteria for both success and fail
        n = 0
        for i, targets in enumerate(self._iter_flat()):
            for t in targets:
                if any(_t.basename not in basenames for _t in flatten_collections(t)):
                    break
            else:
                n += 1

            # early success
            if n >= threshold:
                return True

            # early fail
            if n + (len(self) - i - 1) < threshold:
                return False

        return False

    def count(self, existing=True, keys=False, basenames=None):
        # trivial case when the contained directory does not exist
        if not self.dir.exists():
            if existing:
                return 0 if not keys else (0, [])
            else:
                return len(self) if not keys else (len(self), self.keys())

        # get the basenames of all elements of the directory
        if basenames is None:
            basenames = self.dir.listdir()

        # simple counting
        n = 0
        existing_keys = []
        for key, targets in self._iter_flat(keys=True):
            for t in targets:
                if any(_t.basename not in basenames for _t in flatten_collections(t)):
                    break
            else:
                n += 1
                existing_keys.append(key)

        if existing:
            return n if not keys else (n, existing_keys)
        else:
            n = len(self) - n
            missing_keys = [key for key in self.keys() if key not in existing_keys]
            return n if not keys else (n, missing_keys)

    def remove(self, silent=True):
        for targets in self.iter_existing():
            for t in targets:
                t.remove(silent=silent)


class NestedSiblingFileCollection(FileCollection):
    """
    Collection of targets that represent files which are located across several directories, with
    files in the same directory being wrapped by a :py:class:`SiblingFileCollection` to exploit its
    benefit over the standard :py:class:`FileCollection` (see description above). This is especially
    useful for large collections of remote files that are located in different (sub) directories.

    The constructor identifies targets located in the same physical directory (identified by URI),
    creates one collection for each of them, and stores them in the *collections* attribute. Key
    access, iteration, etc., is identical to the standard :py:class:`FileCollection`.
    """

    def __init__(self, *args, **kwargs):
        super(NestedSiblingFileCollection, self).__init__(*args, **kwargs)

        # as per FileCollection's init, targets are already stored in both the _flat_targets and
        # _flat_target_list attributes, but store them again in sibling file collections to speed up
        # some methods by grouping them into targets in the same physical directory
        self.collections = []
        self._flat_target_collections = {}
        grouped_targets = {}
        for t in flatten_collections(self._flat_target_list):
            grouped_targets.setdefault(t.parent.uri(), []).append(t)
        for targets in grouped_targets.values():
            # create and store the collection
            collection = SiblingFileCollection(targets)
            self.collections.append(collection)
            # remember the collection per target
            for t in targets:
                self._flat_target_collections[t] = collection

    def _repr_pairs(self):
        return FileCollection._repr_pairs(self) + [("collections", len(self.collections))]

    def _get_basenames(self):
        return {
            collection: (collection.dir.listdir() if collection.dir.exists() else [])
            for collection in self.collections
        }

    def iter_existing(self, keys=False):
        basenames = self._get_basenames()
        for key, targets in self._iter_flat(keys=True):
            for t in flatten_collections(targets):
                if t.basename not in basenames[self._flat_target_collections[t]]:
                    break
            else:
                yield (key, targets) if keys else targets

    def iter_missing(self, keys=False):
        basenames = self._get_basenames()
        for key, targets in self._iter_flat(keys=True):
            for t in flatten_collections(targets):
                if t.basename not in basenames[self._flat_target_collections[t]]:
                    yield (key, targets) if keys else targets
                    break

    def exists(self, count=None):
        threshold = self._abs_threshold()

        # trivial case
        if threshold == 0:
            return True

        # when a count was passed, simple compare with the threshold
        if count is not None:
            return count >= threshold

        # simple counting with early stopping criteria for both success and fail
        n = 0
        basenames = self._get_basenames()
        for i, targets in enumerate(self._iter_flat()):
            for t in flatten_collections(targets):
                if t.basename not in basenames[self._flat_target_collections[t]]:
                    break
            else:
                n += 1

            # early success
            if n >= threshold:
                return True

            # early fail
            if n + (len(self) - i - 1) < threshold:
                return False

        return False

    def count(self, existing=True, keys=False):
        # simple counting
        n = 0
        existing_keys = []
        basenames = self._get_basenames()
        for key, targets in self._iter_flat(keys=True):
            for t in flatten_collections(targets):
                if t.basename not in basenames[self._flat_target_collections[t]]:
                    break
            else:
                n += 1
                existing_keys.append(key)

        if existing:
            return n if not keys else (n, existing_keys)
        else:
            n = len(self) - n
            missing_keys = [key for key in self.keys() if key not in existing_keys]
            return n if not keys else (n, missing_keys)

    def remove(self, silent=True):
        for targets in self.iter_existing():
            for t in targets:
                t.remove(silent=silent)


def flatten_collections(*targets):
    lookup = flatten(targets)
    targets = []

    while lookup:
        t = lookup.pop(0)
        if isinstance(t, TargetCollection):
            lookup[:0] = t._flat_target_list
        else:
            targets.append(t)

    return targets
