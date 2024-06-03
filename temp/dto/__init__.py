#!/usr/bin/env python
# -*- coding: utf-8 -*-
from temp.exception import OnlyAccpteDTO


class DTO(object):
    def to_json(self):
        return {}


class ResultDTO(DTO):
    def __init__(self, status=-1, data=None, msg="unknown exception", type="success"):
        self.status = status
        self.data = data
        self.msg = msg
        self.type = type

    def exception(self, err):
        self.status = err.code
        self.msg = err.msg
        self.data = DTO()

    def failed(self, status, msg):
        self.status = status
        self.msg = msg
        self.data = DTO()

    def success(self, data=None):
        if data is None:
            obj = DTO()
        else:
            obj = data

        if not isinstance(obj, DTO):
            raise OnlyAccpteDTO()

        self.status = 200
        self.data = obj
        self.type = "success"
        self.msg = "success"

    def to_json(self):
        return {"code": self.status, "result": self.data.to_json(), "type": self.msg, "message": self.msg}


class DTOConverse(DTO):
    def __init__(self, data):
        self.data = data

    def to_json(self):
        return self.data


class ModelConverse(DTO):
    _exclude_columns = ['query', 'query_class', 'metadata', 'registry']

    def __init__(self, model):
        self.model = model

    def to_json(self):
        return {_: getattr(self.model, _) for _ in dir(self.model) if not _.startswith('_') and _ not in ModelConverse._exclude_columns}
