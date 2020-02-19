from collections import abc
from typing import Any, Callable, Dict, Hashable, Iterable, Sequence, TypeVar

T = TypeVar('T')
H = TypeVar('H', bound=Hashable)


def build_dict_tree_by_keys(
    s: Iterable[T], key_func: Callable[[T], Sequence[H]]
) -> Dict[H, Any]:
    """
    Returns tree-like structure of nested dicts with list at the lowest level.

    >>> build_dict_tree_by_keys(
    ...    [
    ...        {"a": 1, "b": 1},
    ...        {"a": 2, "b": 1},
    ...    ],
    ...    key_func=lambda d: (d["a"], d["b"])
    ... )
    {1: {1: [{'a': 1, 'b': 1}]}, 2: {1: [{'a': 2, 'b': 1}]}}
    """
    result: Dict[H, Any] = {}
    for i in s:
        keys = key_func(i)
        if not isinstance(keys, abc.Iterable):
            keys = (keys,)
        if len(keys) == 0:
            raise ValueError("key_func returned zero keys")
        elif len(keys) == 1:
            result.setdefault(keys[0], []).append(i)
        else:
            node = result
            for k in keys[:-1]:
                node = node.setdefault(k, {})
            node.setdefault(keys[-1], []).append(i)
    return result
