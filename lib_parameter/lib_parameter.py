from typing import Any


def get_default_if_none(parameter: Any, default: Any) -> Any:
    """
    >>> get_default_if_none(parameter=None, default=True)
    True
    >>> get_default_if_none(parameter=False, default=True)
    False

    """
    if parameter is None:
        return default
    else:
        return parameter
