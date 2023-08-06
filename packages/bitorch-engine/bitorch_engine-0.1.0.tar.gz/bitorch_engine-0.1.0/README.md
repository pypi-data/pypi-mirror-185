# Bitorch Engine

Readme will be extended soon.
This package contains layer to provide fast(er) layer implementations for [BITorch](https://github.com/hpi-xnor/bitorch).

## Installation

Currently, the supported installation method is using pip:

- Without any special cuda requirements (to hide the build output remove `-v`):
```bash
pip install -e . -v
```
- With higher CUDA versions you may need to install a torch pre-release and/or add an extra index URL:
```bash
pip install --upgrade --pre torch --extra-index-url https://download.pytorch.org/whl/nightly/cu113
```

For example, for Cuda 11.6.124 `torch==1.12.0.dev20220324+cu113` should work.

## Cuda Device Selection

To select a certain CUDA device, set the environment variable `BIE_DEVICE`, e.g.:
```bash
export BIE_DEVICE=1  # use 2nd cuda device
```

## Development

If building fails, adapt the options in
[cpp_extension.py](bitorch_engine/utils/cpp_extension.py)/
[cuda_extension.py](bitorch_engine/utils/cuda_extension.py).

While developing, a specific cpp/cuda extension can be (re-)build, by using the environment variable `BIE_BUILD_ONLY`,
like so:
```bash
BIE_BUILD_ONLY="bitorch_engine/layers/qconv/binary/cpp" pip install -e . -v
```
It needs to a relative path to one extension directory.

To build for a different CUDA Arch, use the environment variable `BIE_CUDA_ARCH` (e.g. use 'sm_75', 'sm_80', 'sm_86'):
```bash
BIE_CUDA_ARCH="sm_86" pip install -e . -v
```

### MacOS

You should install OpenMP (`brew install libomp`) with homebrew and make sure to add the corresponding environment variables:

```bash
export LIBRARY_PATH=$LIBRARY_PATH:"$(brew --prefix)/lib"
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:"$(brew --prefix)/lib"
export CPATH=$CPATH:"$(brew --prefix)/include"
# during libomp installation it should something like this:
export LDFLAGS="-L$(brew --prefix)/opt/libomp/lib"
export CPPFLAGS="-I$(brew --prefix)/opt/libomp/include"
```
