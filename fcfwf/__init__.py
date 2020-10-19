# coding: utf_8
import functools
from typing import Dict, Union

CHARACTERS: str = '"*/:<>?\\|'

FULLWIDTH = str.maketrans({
    '"': '＂',
    '*': '＊',
    '/': '／',
    ':': '：',
    '<': '＜',
    '>': '＞',
    '?': '？',
    '\\': '＼',
    '|': '｜',
})


@functools.lru_cache
def _maketrans(c: str) -> Dict[int, Union[int, str, None]]:
    if c in CHARACTERS:
        raise ValueError('Forbidden characters cannot be specified as escape characters')

    d: Dict[str, Union[int, str, None]] = {}
    d[c] = c + '{0:02X}'.format(ord(c))
    for n in CHARACTERS:
        d[n] = c + '{0:02X}'.format(ord(n))
    return str.maketrans(d)


def escape(name: str, escape_char: str = '%') -> str:
    return name.translate(_maketrans(escape_char))


def fullwidth(name: str) -> str:
    return name.translate(FULLWIDTH)
