#!/usr/bin/env -S uv run --verbose

# /// script
# requires-python = ">=3.11"
# dependencies = ["setuptools", "toml", "wheel"]
# ///

import sys
import toml
import subprocess

TORCH_VERSION = "2.6.0"

def generate_torch_dependency(version: str, suffix: str = "") -> str:
    return f"torch=={version}{"+" if suffix else ""}{suffix}"

def generate_pyproject():
    metadata = {
        "project": {
            "name": "metatorch",
            "description": "This is a meta package to install PyTorch for different accelerator versions",
            "readme": "README.md",
            "requires-python": ">=3.9",
            "version": TORCH_VERSION,
            # NOTE: Setting a default dependency here ends up making it error out with ResolutionImpossible conflicts
            #       It might be beneficial to think of a way to do this but for now this is what we have
            "optional-dependencies": {
                # TODO: Generate these automatically based on current platform
                "cpu": [generate_torch_dependency(TORCH_VERSION, "cpu")],
                "cpu.cxx11.abi": [generate_torch_dependency(TORCH_VERSION, "cpu.cxx11.abi")],
                "cuda": [generate_torch_dependency(TORCH_VERSION, "cu124")],
                "cuda12.4": [generate_torch_dependency(TORCH_VERSION, "cu124")],
                "cuda12.1": [generate_torch_dependency(TORCH_VERSION, "cu121")],
                "rocm": [generate_torch_dependency(TORCH_VERSION, "rocm6.2.4")],
                "rocm6.2": [generate_torch_dependency(TORCH_VERSION, "rocm6.2.4")],
                "rocm6.1": [generate_torch_dependency(TORCH_VERSION, "rocm6.1")],
                "xpu": [generate_torch_dependency(TORCH_VERSION, "xpu")],
            },
        }
    }
    with open('pyproject.toml', 'w') as fp:
        toml.dump(metadata, fp)

def build_wheel():
    subprocess.run([sys.executable, "-m", "build"], check=True)

def main() -> None:
    generate_pyproject()
    # TODO: Build wheel with python -m build
    # TODO: Rename wheel with platform specific tag using python -m wheel
    #       You should be able to grab the tag using:
    #       from setuptools.command.bdist_wheel import get_platform

if __name__ == "__main__":
    main()
