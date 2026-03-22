"""TeleBot-i18n: A lightweight internationalization framework for Telegram bots."""

import json
import os
from typing import Any, Dict, Optional


class TeleBotI18n:
    """Internationalization manager for Telegram bots.

    Loads JSON locale files from a directory and provides translated strings
    with optional variable formatting.

    Usage:
        i18n = TeleBotI18n("locales")
        greeting = i18n.get_text("en", "welcome", name="Alice")
    """

    def __init__(self, locales_dir: str = "locales", fallback: str = "en"):
        self.locales_dir = locales_dir
        self.fallback = fallback
        self._cache: Dict[str, Dict[str, str]] = {}
        self._load_all()

    def _load_all(self) -> None:
        """Load all JSON locale files from the locales directory."""
        if not os.path.isdir(self.locales_dir):
            raise FileNotFoundError(
                f"Locales directory not found: {self.locales_dir}"
            )
        for filename in os.listdir(self.locales_dir):
            if filename.endswith(".json"):
                lang = filename[:-5]
                path = os.path.join(self.locales_dir, filename)
                with open(path, encoding="utf-8") as f:
                    self._cache[lang] = json.load(f)

    def available_languages(self) -> list[str]:
        """Return a list of loaded language codes."""
        return list(self._cache.keys())

    def reload(self) -> None:
        """Hot-reload all locale files from disk."""
        self._cache.clear()
        self._load_all()

    def get_text(
        self,
        language_code: str,
        key: str,
        *,
        default: Optional[str] = None,
        **kwargs: Any,
    ) -> str:
        """Return a translated string, formatted with any keyword arguments.

        Falls back to the fallback language, then to a default string, then
        returns the raw key if nothing matches.
        """
        text = self._lookup(language_code, key)
        if text is None:
            text = self._lookup(self.fallback, key)
        if text is None:
            text = default or key
        if kwargs:
            try:
                text = text.format(**kwargs)
            except (KeyError, IndexError) as exc:
                raise ValueError(
                    f"Missing placeholder in key '{key}': {exc}"
                ) from exc
        return text

    def _lookup(self, lang: str, key: str) -> Optional[str]:
        """Look up a key in a specific language's translations."""
        return self._cache.get(lang, {}).get(key)
