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
"""Provides cli functionality for versioning info."""

from __future__ import annotations

import platform
from pathlib import Path

from wom import __git_sha__, __version__


def info() -> None:
    """Prints package/system info and exits."""
    path = Path(__file__).parent.absolute()
    py_impl = platform.python_implementation()
    py_ver = platform.python_version()
    py_c = platform.python_compiler()
    p = platform.uname()

    print(f"wom.py v{__version__} from {__git_sha__}")
    print(f"@ {path}")
    print(f"{py_impl} {py_ver} {py_c}")
    print(f"{p.system} {p.node} {p.release} {p.machine}")
    print(p.version)
