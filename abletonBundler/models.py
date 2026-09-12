"""Shared data model: SampleReference, PluginReference, PluginType, ReferenceKind."""

from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Optional


class PluginType(Enum):
    VST = "VST"
    VST3 = "VST3"
    AU = "AU"
    MAX_FOR_LIVE = "Max for Live"
    STOCK = "Stock"


class ReferenceKind(Enum):
    """Distinguishes raw audio samples from preset/patch files (Wavetable
    tables, Sampler multisample zones, device presets, etc.) so both get the
    same missing/bundled tracking without being confused for one another."""

    SAMPLE = "Sample"
    PATCH = "Patch"


@dataclass
class SampleReference:
    originalPath: str
    exists: bool
    targetPath: Optional[Path] = None
    kind: ReferenceKind = ReferenceKind.SAMPLE
    sourceLibrary: Optional[str] = None
    """Name of the external sample/preset library this file lives under
    (e.g. "Splice"), if its path matches a known library folder pattern.
    None for project-local or unrecognized sources. Informational only —
    bundling behavior is the same regardless of this value."""


@dataclass(frozen=True)
class PluginReference:
    name: str
    pluginType: PluginType
    link: Optional[str] = None
    """Purchase/info URL for this plugin, if known, so a recipient missing
    the plugin has somewhere to go. None means the debrief should fall back
    to listing just the plugin name."""
