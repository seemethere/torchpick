#!/usr/bin/env -S uv run

# /// script
# requires-python = ">=3.11"
# dependencies = ["build"]
# ///

import sys
import subprocess


def build_wheel():
    subprocess.run([sys.executable, "-m", "build"], check=True)


def main() -> None:
    print("+ Building wheel")
    build_wheel()


if __name__ == "__main__":
    main()
