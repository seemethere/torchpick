#!/usr/bin/env -S uv run

# /// script
# requires-python = ">=3.11"
# dependencies = ["setuptools", "wheel", "build"]
# ///

import sys
import subprocess
import os
import pathlib
from setuptools.command.bdist_wheel import get_platform

ROOT_DIR = pathlib.Path(os.path.realpath(__file__)).parent


def build_wheel():
    subprocess.run([sys.executable, "-m", "build"], check=True)


def rename_wheel():
    platform_tag = get_platform(".")
    torch_version = open(ROOT_DIR / "VERSION").read().strip()
    # Assuming the wheel file is in the dist directory and has a standard naming convention
    wheel_file = f"dist/torchpick-{torch_version}-py3-none-any.whl"
    new_wheel_file = f"dist/torchpick-{torch_version}-py3-none-{platform_tag}.whl"
    os.rename(wheel_file, new_wheel_file)


def main() -> None:
    print("+ Building wheel")
    build_wheel()
    print("+ Renaming wheel")
    rename_wheel()


if __name__ == "__main__":
    main()
