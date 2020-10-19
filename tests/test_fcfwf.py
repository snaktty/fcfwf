# coding: utf_8
import fcfwf


def test_escape():
    assert fcfwf.escape('%' + fcfwf.CHARACTERS) == '%25%3C%3E%3A%22%2F%5C%7C%3F%2A'
    assert fcfwf.escape('$' + fcfwf.CHARACTERS, escape_char='$') == '$24$3C$3E$3A$22$2F$5C$7C$3F$2A'


def test_fullwidth():
    assert fcfwf.fullwidth(fcfwf.CHARACTERS) == '＜＞：＂／＼｜？＊'
