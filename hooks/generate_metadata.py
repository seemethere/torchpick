import os
import pathlib
from hatchling.metadata.plugin.interface import MetadataHookInterface
from setuptools.command.bdist_wheel import get_platform

ROOT_DIR = pathlib.Path(os.path.realpath(__file__)).parent.parent


def generate_torch_dependency(version: str, suffix: str = "") -> str:
    return f"torch=={version}{'+' if suffix else ''}{suffix}"


class JSONMetaDataHook(MetadataHookInterface):
    def update(self, metadata):
        torch_version = open(ROOT_DIR / "VERSION").read().strip()
        platform = get_platform(".")
        platform_dependencies = {
            "linux_x86_64": {
                "cpu": [generate_torch_dependency(torch_version, "cpu")],
                "cpu.cxx11.abi": [
                    generate_torch_dependency(torch_version, "cpu.cxx11.abi")
                ],
                "cuda": [generate_torch_dependency(torch_version, "cu124")],
                "cuda12.4": [generate_torch_dependency(torch_version, "cu124")],
                "cuda12.1": [generate_torch_dependency(torch_version, "cu121")],
                "cuda11.8": [generate_torch_dependency(torch_version, "cu118")],
                "rocm": [generate_torch_dependency(torch_version, "rocm6.2.4")],
                "rocm6.2": [generate_torch_dependency(torch_version, "rocm6.2.4")],
                "rocm6.1": [generate_torch_dependency(torch_version, "rocm6.1")],
                "xpu": [generate_torch_dependency(torch_version, "xpu")],
            },
            "macos": {
                "cpu": [generate_torch_dependency(torch_version)],
            },
            "win_amd64": {
                "cpu": [generate_torch_dependency(torch_version, "cpu")],
                "cpu.cxx11.abi": [
                    generate_torch_dependency(torch_version, "cpu.cxx11.abi")
                ],
                "cuda": [generate_torch_dependency(torch_version, "cu124")],
                "cuda12.4": [generate_torch_dependency(torch_version, "cu124")],
                "cuda12.1": [generate_torch_dependency(torch_version, "cu121")],
                "cuda11.8": [generate_torch_dependency(torch_version, "cu118")],
                "xpu": [generate_torch_dependency(torch_version, "xpu")],
            },
        }
        # special case for macOS
        if platform.startswith("macos"):
            platform = "macos"
        metadata["version"] = torch_version
        metadata["optional-dependencies"] = platform_dependencies.get(platform, [])
