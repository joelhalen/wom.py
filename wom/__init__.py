# wom.py - An asynchronous wrapper for the Wise Old Man API.
# Copyright (c) 2023-present Jonxslays
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from __future__ import annotations

from typing import Final

__all__ = (
    "constants",
    "enums",
    "models",
    "routes",
    "services",
    "Client",
)

from . import constants
from . import enums
from . import models
from . import routes
from . import services

from .client import *

__packagename__: Final[str] = "wom.py"
__version__: Final[str] = "0.1.0"
__author__: Final[str] = "Jonxslays"
__copyright__: Final[str] = "2023-present Jonxslays"
__description__: Final[str] = "An asynchronous wrapper for the Wise Old Man API."
__url__: Final[str] = "https://github.com/Jonxslays/wise-old-man"
__docs__: Final[str] = "https://jonxslays.github.io/wise-old-man"
__repository__: Final[str] = __url__
__license__: Final[str] = "MIT"
__git_sha__: Final[str] = "[HEAD]"
