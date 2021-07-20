#!/usr/bin/env python3

import sys
import argparse
from enum import Enum


class ExitCode(Enum):
    Success = 0
    Failure = 1


def main() -> ExitCode:
    cli = argparse.ArgumentParser(description="Module entry point")

    args = cli.parse_args()
    print(args)  # TODO remove

    return ExitCode.Success


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code.value)
