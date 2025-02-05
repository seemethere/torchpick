import os
import pathlib
from hatchling.metadata.plugin.interface import MetadataHookInterface

ROOT_DIR = pathlib.Path(os.path.realpath(__file__)).parent.parent

LINUX = "platform_system == 'Linux'"
LINUX_X86 = "platform_system == 'Linux' and platform_machine == 'x86_64'"
LINUX_OR_WINDOWS = f"{LINUX} or platform_system == 'Windows'"


def generate_torch_dependency(
    version: str, suffix: str = "", specifiers: str = ""
) -> str:
    return f"torch=={version}{'+' if suffix else ''}{suffix}{';' if specifiers else ''}{specifiers}"


class JSONMetaDataHook(MetadataHookInterface):
    def update(self, metadata):
        torch_version = open(ROOT_DIR / "VERSION").read().strip()
        metadata["optional-dependencies"] = {
            "cpu": [generate_torch_dependency(torch_version, "cpu", LINUX_OR_WINDOWS)],
            "cpu.cxx11.abi": [
                generate_torch_dependency(
                    torch_version, "cpu.cxx11.abi", LINUX_OR_WINDOWS
                )
            ],
            "cuda": [
                generate_torch_dependency(torch_version, "cu124", LINUX_OR_WINDOWS)
            ],
            "cuda12.6": [
                generate_torch_dependency(torch_version, "cu126", LINUX_OR_WINDOWS)
            ],
            "cuda12.4": [
                generate_torch_dependency(torch_version, "cu124", LINUX_OR_WINDOWS)
            ],
            "cuda12.1": [
                generate_torch_dependency(torch_version, "cu121", LINUX_OR_WINDOWS)
            ],
            "cuda11.8": [
                generate_torch_dependency(torch_version, "cu118", LINUX_OR_WINDOWS)
            ],
            "xpu": [generate_torch_dependency(torch_version, "xpu", LINUX_OR_WINDOWS)],
            "rocm": [generate_torch_dependency(torch_version, "rocm6.2.4", LINUX_X86)],
            "rocm6.2": [
                generate_torch_dependency(torch_version, "rocm6.2.4", LINUX_X86)
            ],
            "rocm6.1": [generate_torch_dependency(torch_version, "rocm6.1", LINUX_X86)],
        }
        metadata["version"] = torch_version
