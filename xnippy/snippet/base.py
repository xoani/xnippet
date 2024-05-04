"""BaseSnippet for provide platform for developing Snippet to configure and/or interface with integrated apps's ecosystem.
"""

from __future__ import annotations
from xnippy.formatter import Fetcher
from typing import TYPE_CHECKING
from packaging.version import parse
if TYPE_CHECKING:
    from packaging.version import _Version as VersionType


class Snippet(Fetcher):
    name: str
    version: VersionType
    type: str
    is_valid: bool
    
    def parse_version(self, version_string):
        self.version = parse(version_string)