# What is this?

This repository is a proof of concept on how we can change PyTorch's package installation
for the better. It should enable a path to where we can have users specify which
specific accelerator they would like to use by using the following installation command(s):

> [!NOTE]
> This doesn't work as of today this is just showcasing what this could look like if we rolled
> this as the default torch package.

```bash
# Based on accelerator type
pip install torch[cpu]
pip install torch[cuda]
pip install torch[rocm]
pip install torch[xpu]

# Based on accelerator version
pip install torch[cpu-cxx11-abi]
pip install torch[cuda12-4]
pip install torch[cuda12-1]
pip install torch[rocm6-2]
pip install torch[rocm6-1]
```

## How to build

### Pre-requisites:
* [uv](https://github.com/astral-sh/uv)
* python3.12 (with build module installed)

### Commands to run

```bash
# Generate the pyproject.toml
./generate.py
# Building the wheel
python3.12 -m build
```

## Work Todo
- [ ] Move wheel building into the singular script
- [ ] Rename the wheel with platform specific tags so that users on macOS / Windows can have specific version for their own OS
- [ ] Automate this to automatically reflect PyTorch's binary build matrix
