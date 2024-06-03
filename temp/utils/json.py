#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import jsonify

from temp.dto import DTO

def send(obj):
    if not isinstance(obj, DTO):
        return jsonify({})
    return jsonify(obj.to_json())


def send_obj(obj):
    return jsonify(obj)
