# -*- coding:utf-8 -*-
from typing import Union


class Pinner(object):
    """用于记录时间间隔的工具"""
    times: list
    show_everytime: bool

    def __init__(self, pin: bool = False, show_everytime: bool = True) -> None: ...

    @property
    def records(self) -> list: ...

    @property
    def winner(self) -> Union[tuple, None]: ...

    def pin(self, text: str = '', show: bool = None) -> tuple: ...

    def skip(self) -> None: ...

    def show(self) -> None: ...

    def clear(self) -> None: ...
