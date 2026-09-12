"""Static lookup of purchase/info links for known third-party plugins.

Ableton can't legally ship a third-party VST/AU/AAX binary inside an export,
so the debrief instead points the recipient at where to get it. Used by
ProjectScanner (to populate PluginReference.link) and DebriefGenerator (to
print the link when known, falling back to just the plugin name otherwise).
"""

from typing import Optional


def lookupPluginLink(pluginName: str) -> Optional[str]:
    """Look up a known purchase/info URL for pluginName (case-insensitive
    match against a small static table of common plugins), and return None
    if nothing is known — callers must treat that as "just show the name"."""
    # TODO: implement (static dict of plugin name -> vendor URL)
    pass
