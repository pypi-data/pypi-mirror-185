_It is currently under early development, but little by little new algorithms will be added_

# PyCrypTools
### Version 1.4.0 | Polybios
PyCrypTools is a python library that brings us a series of algorithms to encrypt and decrypt inputs.

```
888       888 888     888       d8888 888
888   o   888 888     888      d88888 888
888  d8b  888 888     888     d88P888 888        (code by WUAL)
888 d888b 888 888     888    d88P 888 888            twitter.com/codewual
888d88888b888 888     888   d88P  888 888     github.com/14wual
88888P Y88888 888     888  d88P   888 888            youtube: WualPK
8888P   Y8888 Y88b. .d88P d8888888888 888     
888P     Y888  "Y88888P" d88P     888 88888888
```

See commits updates (CHANGELOG) here: <a href="https://github.com/14wual/pycryptools/blob/main/CHANGELOG.md"><b>Link</b></a>

## Install

```python
pip install pycryptools
```

## Examples

**Result**: `OWRILHO`| `EXAMPLE`
```python
from pycryptools.scytale import scytale

message = "example"
keyword = "random"

encrypt = scytale.encrypt(message, keyword)
print(encrypt)

decrypt = scytale.decrypt(encrypt, keyword)
print(decrypt)
```

## Available algorithms:

[PyCrypTools](https://github.com/14wual/pycryptools) currently has 4 algorithm.

[Read More](https://github.com/14wual/pycryptools/tree/main/about#readme)

1. [AtBash](https://github.com/14wual/pycryptools/blob/main/about/algorithms.md#atbash)
2. [Scytale](https://github.com/14wual/pycryptools/blob/main/about/algorithms.md#scytale)
3. [Polybios](https://github.com/14wual/pycryptools/blob/main/about/algorithms.md#polybios)
4. [Caesar](https://github.com/14wual/pycryptools/blob/main/about/algorithms.md#caesar)

