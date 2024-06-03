#!/usr/bin/env python
# -*- coding: utf-8 -*-

class TempException(Exception):
    pass


class ParamException(TempException):
    def __init__(self):
        self.code = 100001
        self.msg = " 参数错误 "


class OnlyAccpteDTO(TempException):
    def __init__(self):
        self.code = 100002
        self.msg = " 结果结构错误 "
