# -*- coding: utf-8 -*-
#
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Wrappers for protocol buffer enum types."""

import enum


class NullValue(enum.IntEnum):
    """
    ``NullValue`` is a singleton enumeration to represent the null value
    for the ``Value`` type union.

    The JSON representation for ``NullValue`` is JSON ``null``.

    Attributes:
      NULL_VALUE (int): Null value.
    """

    NULL_VALUE = 0


class View(enum.IntEnum):
    """
    Column identifier used for the values in the row.

    Attributes:
      VIEW_UNSPECIFIED (int): Defaults to user entered text.
      COLUMN_ID_VIEW (int): Uses internally generated column id to identify values.
    """

    VIEW_UNSPECIFIED = 0
    COLUMN_ID_VIEW = 1
