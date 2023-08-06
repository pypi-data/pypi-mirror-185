#  This file is part of Pynguin.
#
#  SPDX-FileCopyrightText: 2019–2023 Pynguin Contributors
#
#  SPDX-License-Identifier: LGPL-3.0-or-later
#
from abc import ABC
from abc import abstractmethod


class Foo(ABC):
    @abstractmethod
    def foo(self):
        pass
