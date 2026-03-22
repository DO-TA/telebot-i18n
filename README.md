# 🌍 TeleBot-i18n: Dynamic Internationalization for Telegram Bots

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)

**TeleBot-i18n** is a lightweight, zero-dependency Python framework designed to solve the biggest pain point in Telegram Bot development: **Hardcoded Strings and spaghetti localization logic.**

Whether you are building a simple utility bot or a complex Super App, TeleBot-i18n allows you to seamlessly serve users in their native languages using dynamic JSON routing.

## 🚀 Why We Built This
While developing complex, data-heavy Telegram bots (such as global astrology and psychology tools), we realized that managing `InlineKeyboard` callbacks and message handlers across multiple languages (`EN`, `DE`, `FA`, etc.) leads to unmaintainable code. 

Existing solutions are either too bloated or lack native integration with Python's formatting syntax. We built this to make bot localization plug-and-play.

## 🛠️ Features
- **Zero Dependencies:** Pure Python. Just drop it into your project.
- **Dynamic Formatting:** Supports standard Python `**kwargs` for dynamic variable injection (e.g., `Hello, {name}!`).
- **Graceful Fallbacks:** Automatically falls back to the default language (e.g., English) if a translation key is missing in the target locale.
- **Memory Efficient:** Loads locales into memory once on startup.

## 🗺️ Future Roadmap & The AI Vision
We are currently applying for the **OpenAI Codex for OSS** program. Our Phase 2 vision is to integrate Large Language Models directly into the localization pipeline:
1. **Automated Locale Generation:** Using OpenAI models to auto-generate `de.json`, `es.json`, etc., directly from the base `en.json` while maintaining context and tone.
2. **Context-Aware Fallbacks:** Instead of returning a missing key error, the system will query an LLM in real-time to translate the fallback string conceptually, ensuring zero downtime for non-English users.

## 💻 Quick Start
Check out the `example_bot.py` file to see how easily you can implement dynamic multi-language keyboards in under 20 lines of code.

## 🤝 Contributing
Open-source is about community. If you have ideas for improving the LLM integration or adding new storage adapters (Redis, PostgreSQL), please open an issue or submit a Pull Request!

---
*Built with ❤️ for the global developer community.*