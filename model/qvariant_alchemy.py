from __future__ import absolute_import, unicode_literals, print_function

from PyQt5.QtCore import QVariant
from sqlalchemy import types

"""
SQLAlchemy types for dealing with QVariants & various QTypes (like QString)
"""

import datetime


def gen_process_bind_param(pytype, toqtype, self, value, dialect):
    if value is None:
        return None
    elif isinstance(value, QVariant):
        return pytype(toqtype(value))
    elif not isinstance(value, pytype):
        return pytype(value)
    else:
        return value


class Integer(types.TypeDecorator):
    impl = types.Integer

    def process_bind_param(self, value, dialect):
        return gen_process_bind_param(
            int, lambda value: value.toLongLong(),
            self, value, dialect)


class Boolean(types.TypeDecorator):
    impl = types.Boolean

    def process_bind_param(self, value, dialect):
        return gen_process_bind_param(
            bool, lambda value: value.toBool(),
            self, value, dialect)


class String(types.TypeDecorator):
    impl = types.String

    def process_bind_param(self, value, dialect):
        return gen_process_bind_param(
            str, lambda value: value.toString(),
            self, value, dialect)


class Date(types.Date):
    impl = types.Date

    def process_bind_param(self, value, dialect):
        return gen_process_bind_param(
            datetime.datetime, lambda value: value.toDate(),
            self, value, dialect)


class DECIMAL(types.Date):
    impl = types.DECIMAL

    def process_bind_param(self, value, dialect):
        return gen_process_bind_param(
            float, lambda value: value.toDECIMAL(),
            self, value, dialect)
