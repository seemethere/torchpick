import os
import pathlib
from hatchling.metadata.plugin.interface import MetadataHookInterface

ROOT_DIR = pathlib.Path(os.path.realpath(__file__)).parent.parent


def generate_torch_dependency(version: str, suffix: str = "") -> str:
    return f"torch=={version}{'+' if suffix else ''}{suffix}"


class JSONMetaDataHook(MetadataHookInterface):
    def update(self, metadata):
        torch_version = open(ROOT_DIR / "VERSION").read().strip()
        metadata["version"] = torch_version
        metadata["optional-dependencies"] = {
            # TODO: Generate these automatically based on current platform
            "cpu": [generate_torch_dependency(torch_version, "cpu")],
            "cpu.cxx11.abi": [
                generate_torch_dependency(torch_version, "cpu.cxx11.abi")
            ],
            "cuda": [generate_torch_dependency(torch_version, "cu124")],
            "cuda12.4": [generate_torch_dependency(torch_version, "cu124")],
            "cuda12.1": [generate_torch_dependency(torch_version, "cu121")],
            "rocm": [generate_torch_dependency(torch_version, "rocm6.2.4")],
            "rocm6.2": [generate_torch_dependency(torch_version, "rocm6.2.4")],
            "rocm6.1": [generate_torch_dependency(torch_version, "rocm6.1")],
            "xpu": [generate_torch_dependency(torch_version, "xpu")],
        }
