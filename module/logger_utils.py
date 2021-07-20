#!/usr/bin/env python3

import colorama
from enum import Enum
from datetime import datetime


class LogLevel(Enum):
    Debug = 4
    Info = 3
    Warn = 2
    Error = 1
    Nothing = 0


class Logger:
    def __init__(self, name: str, level: LogLevel = LogLevel.Nothing):
        self.name = name
        self.level = level

    def _print(self, kind: LogLevel, *args):
        colors = {
            LogLevel.Debug: colorama.Fore.MAGENTA,
            LogLevel.Info: colorama.Fore.CYAN,
            LogLevel.Warn: colorama.Fore.YELLOW,
            LogLevel.Error: colorama.Fore.RED,
        }

        if kind.value > self.level.value:
            return

        prefix = f"[{colors[kind]}{kind.name:^5}{colorama.Fore.RESET}]"
        now = datetime.now().isoformat(timespec="minutes")
        colored_now = f"{colorama.Fore.MAGENTA}{now}{colorama.Fore.RESET}"
        rest = " ".join(str(el) for el in args)

        print(f"{prefix} -- {colored_now} -- {rest}")

    def debug(self, *args):
        self._print(LogLevel.Debug, *args)

    def info(self, *args):
        self._print(LogLevel.Info, *args)

    def warn(self, *args):
        self._print(LogLevel.Warn, *args)

    def error(self, *args):
        self._print(LogLevel.Error, *args)


colorama.init()
