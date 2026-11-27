"""
CTypeImplBaseClass – base class for all converted C# model types.

Existing classes keep working unchanged. New, all optional:

    CsType["OptionMonsterSkillModel"]
        Annotation for a member whose Python class does not exist yet.
        Only when default values are built, the type is resolved:
          1. already imported Python class  CPrefix + name  (registry)
          2. module  <classes_package>.C<name>  (imported on demand)
          3. only if neither exists: skel.default(name) reads the .cs file.
        As soon as you write the Python class, the member uses it automatically,
        the annotation does not have to change.

    Cls.fields()    -> [(annotation, member_name), ...]   (like skel.fields)
    Cls.default()   -> instance with every member filled   (like skel.default)
    obj.autoJSON()  -> generic dict, usable from toJSON()

Members are the annotated attributes whose name starts with MEMBER_PREFIX
("m_"), including those of base classes. Instances are created with
cls.__new__(cls), __init__ is not called. A class still has to implement
toJSON(), otherwise Python refuses to instantiate the abstract class.
"""
from __future__ import annotations

import collections.abc
import datetime
import enum
import importlib
import logging
import time
import types
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import (
    Annotated, Any, Callable, ClassVar, Dict, List, Tuple, TypeVar, Union,
    get_args, get_origin, get_type_hints,
)

log = logging.getLogger(__name__)

T = TypeVar("T", bound="CTypeImplBaseClass")

# ── Configuration (adjust with configure()) ───────────────────────────────────
CLASSES_PACKAGE = "serverfiles.types.classes"   # where C<Name>.py files live
SKEL_MODULE = "serverfiles.skel"                # module that provides default(name)
CLASS_PREFIX = "C"                              # C# "Foo" <-> Python "CFoo"
MEMBER_PREFIX = "m_"                            # C# field "Foo" <-> Python "m_Foo"


def configure(*, classes_package: str | None = None, skel_module: str | None = None,
              class_prefix: str | None = None, member_prefix: str | None = None) -> None:
    """Override module settings; also clears the per-class member cache."""
    global CLASSES_PACKAGE, SKEL_MODULE, CLASS_PREFIX, MEMBER_PREFIX
    if classes_package is not None:
        CLASSES_PACKAGE = classes_package
    if skel_module is not None:
        SKEL_MODULE = skel_module
    if class_prefix is not None:
        CLASS_PREFIX = class_prefix
    if member_prefix is not None:
        MEMBER_PREFIX = member_prefix
    _SPEC_CACHE.clear()


# ── Registry of all Python classes (filled by __init_subclass__) ──────────────
_REGISTRY: Dict[str, type] = {}
_SPEC_CACHE: Dict[type, List[Tuple[str, Any]]] = {}


class CTypeImplBaseClass(ABC):

    def __init_subclass__(cls, **kwargs: Any) -> None:
        super().__init_subclass__(**kwargs)
        _REGISTRY[cls.__name__] = cls
        _SPEC_CACHE.pop(cls, None)

    @abstractmethod
    def toJSON(self) -> dict[str, Any]:
        pass

    # ── lazy defaults: unset members are filled on first access ───────────────
    def __getattr__(self, name: str) -> Any:
        # only called when normal lookup failed, i.e. the member is not set yet
        if name.startswith("__") or not name.startswith(MEMBER_PREFIX):
            raise AttributeError(name)
        cls = type(self)
        for n, tp in _member_specs(cls):
            if n == name:
                value = _default_value(tp, (cls,))
                object.__setattr__(self, name, value)
                return value
        raise AttributeError(f"{cls.__name__!s} has no member {name!r}")

    # ── introspection ─────────────────────────────────────────────────────────
    @classmethod
    def fields(cls) -> List[Tuple[Any, str]]:
        """[(annotation, member_name)] incl. base classes, like skel.fields."""
        return [(tp, name) for name, tp in _member_specs(cls)]

    # ── default values ────────────────────────────────────────────────────────
    @classmethod
    def default(cls: type[T]) -> T:
        """Instance of cls with every member filled with a default value."""
        return cls._build(())  # type: ignore[return-value]

    @classmethod
    def _build(cls, stack: tuple) -> Any:
        if cls in stack:                       # circular reference -> None, like skel
            return None
        obj = cls.__new__(cls)
        inner = stack + (cls,)
        for name, tp in _member_specs(cls):
            setattr(obj, name, _default_value(tp, inner))
        return obj

    # ── optional helper ───────────────────────────────────────────────────────
    def autoJSON(self) -> dict[str, Any]:
        """Generic dict with camelCase keys; can be returned from toJSON()."""
        return {
            json_key(name): _to_json_value(getattr(self, name))
            for name, _ in _member_specs(type(self))
        }


# ── Not yet converted types ───────────────────────────────────────────────────
@dataclass(frozen=True)
class CsRef:
    """Marker: C# type name (without prefix) that is resolved lazily."""
    name: str


class CDynamic(CTypeImplBaseClass):
    """Holds the dict built from the .cs file for a type without Python class."""

    def __init__(self, type_name: str, value: Any) -> None:
        self.type_name = type_name
        self.value = value

    def toJSON(self) -> Any:
        return self.value

    def __getitem__(self, key: str) -> Any:
        return self.value[key]

    def __setitem__(self, key: str, item: Any) -> None:
        self.value[key] = item

    def __repr__(self) -> str:
        return f"CDynamic({self.type_name!r}, {self.value!r})"


class CsType:
    """Use as annotation:  m_Foo: CsType["FooModel"]   or   list[CsType["FooModel"]]"""

    def __class_getitem__(cls, name: str) -> Any:
        if not isinstance(name, str) or not name:
            raise TypeError("CsType[...] needs the C# type name as string")
        return Annotated[CDynamic, CsRef(name)]


# ── Helpers ───────────────────────────────────────────────────────────────────
def json_key(member_name: str) -> str:
    """m_OptionMonster -> optionMonster (same rule as skel.cam)."""
    name = member_name[len(MEMBER_PREFIX):] if MEMBER_PREFIX and member_name.startswith(MEMBER_PREFIX) else member_name
    return name[:1].lower() + name[1:]


def _member_specs(cls: type) -> List[Tuple[str, Any]]:
    cached = _SPEC_CACHE.get(cls)
    if cached is not None:
        return cached
    hints = get_type_hints(cls, include_extras=True)
    specs: List[Tuple[str, Any]] = []
    for name, tp in hints.items():
        if MEMBER_PREFIX and not name.startswith(MEMBER_PREFIX):
            continue
        if tp is ClassVar or get_origin(tp) is ClassVar:
            continue
        specs.append((name, tp))
    _SPEC_CACHE[cls] = specs
    return specs


def _resolve_python_class(name: str) -> type | None:
    py_name = CLASS_PREFIX + name
    found = _REGISTRY.get(py_name)
    if found is not None:
        return found
    module_name = f"{CLASSES_PACKAGE}.{py_name}"
    try:
        module = importlib.import_module(module_name)
    except ModuleNotFoundError as e:
        if e.name == module_name:              # file simply does not exist (yet)
            return None
        raise                                  # wrong package setting or broken import inside
    return getattr(module, py_name, None) or _REGISTRY.get(py_name)


def _load_from_disk(name: str) -> Any:
    skel = importlib.import_module(SKEL_MODULE)
    value = skel.default(name)
    if value is None:
        log.warning("CsType[%r]: no Python class and no .cs file found", name)
    return value


def _default_cs(name: str, stack: tuple) -> Any:
    py_cls = _resolve_python_class(name)
    if py_cls is not None:
        return _default_value(py_cls, stack)
    return CDynamic(name, _load_from_disk(name))


# Extra defaults, e.g. register_default(Vector3, lambda: [0.0, 0.0, 0.0])
_CUSTOM_DEFAULTS: Dict[Any, Callable[[], Any]] = {}


def register_default(tp: Any, factory: Callable[[], Any]) -> None:
    _CUSTOM_DEFAULTS[tp] = factory


def _timestamp_now() -> Any:
    try:
        import msgpack
        return msgpack.Timestamp(seconds=int(time.time()))   # same as skel
    except ImportError:
        return datetime.datetime.now(datetime.timezone.utc)


try:                                           # msgpack.Timestamp members (like skel: now)
    import msgpack as _msgpack
    _CUSTOM_DEFAULTS[_msgpack.Timestamp] = lambda: _msgpack.Timestamp(seconds=int(time.time()))
except ImportError:
    pass


def _enum_default(tp: type[enum.Enum]) -> Any:
    try:
        return tp(0)                           # like skel: 0 ...
    except ValueError:
        return next(iter(tp), None)            # ... or the first member if 0 is not defined


# order matters: bool before int
_SCALAR_DEFAULTS: List[Tuple[type, Callable[[], Any]]] = [
    (bool, lambda: False),
    (int, lambda: 0),
    (float, lambda: 0.0),
    (str, lambda: ""),
    (bytes, lambda: b""),
    (datetime.datetime, _timestamp_now),
    (dict, dict),
    (list, list),
    (tuple, tuple),
    (set, set),
]


def _default_value(tp: Any, stack: tuple) -> Any:
    if tp in _CUSTOM_DEFAULTS:
        return _CUSTOM_DEFAULTS[tp]()

    origin = get_origin(tp)
    if origin is Annotated:
        base, *meta = get_args(tp)
        for m in meta:
            if isinstance(m, CsRef):
                return _default_cs(m.name, stack)
        return _default_value(base, stack)
    if origin in (Union, types.UnionType):
        args = get_args(tp)
        if type(None) in args:
            return None                        # Optional[X] / X | None
        return _default_value(args[0], stack)
    if origin is not None:                     # list[X], dict[K, V], tuple[...], Sequence[X] ...
        if origin in (dict, collections.abc.Mapping, collections.abc.MutableMapping):
            return {}
        if origin in (set, frozenset, collections.abc.Set):
            return set()
        if origin is tuple:
            return ()
        return []

    if isinstance(tp, type):
        if issubclass(tp, CTypeImplBaseClass):
            return tp._build(stack)
        if issubclass(tp, enum.Enum):
            return _enum_default(tp)
        for base, factory in _SCALAR_DEFAULTS:
            if issubclass(tp, base):
                return factory()
    if tp is not Any:
        log.warning("no default for type %r -> None (use register_default)", tp)
    return None                                # Any / unknown


def _to_json_value(value: Any) -> Any:
    if isinstance(value, CTypeImplBaseClass):
        return value.toJSON()
    if isinstance(value, enum.Enum):
        return value.value
    if isinstance(value, (list, tuple, set)):
        return [_to_json_value(v) for v in value]
    if isinstance(value, dict):
        return {k: _to_json_value(v) for k, v in value.items()}
    return value