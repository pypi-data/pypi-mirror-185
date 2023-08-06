_It is currently under early development, but little by little new algorithms will be added_

# PyCrypTools
### Version 1.5.0 | Alberti Disk
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

1. [AtBash](https://github.com/14wual/pycryptools/blob/main/about/README.md#atbash)

<details>

Usage:
```python
from pycryptools.atbash import atbash

message = "example"

encrypt = atbash.encrypt(message)
print(encrypt)

decrypt = atbash.decrypt(encrypt)
print(decrypt)
```

Atbash is a monoalphabetic substitution encryption algorithm. This means that it uses a single substitution table to encode all the letters in the original message. In the case of Atbash encryption, the substitution table is built from a given keyword and consists of reversing the order of the letters of the alphabet to substitute each letter of the original message.

</details>

2. [Scytale](https://github.com/14wual/pycryptools/blob/main/about/README.md#scytale)

<details>

Usage: 
```python
from pycryptools.scytale import scytale

message = "example"
keyword = "random"

encrypt = scytale.encrypt(message, keyword)
print(encrypt)

decrypt = scytale.decrypt(encrypt, keyword)
print(decrypt)
```

To encrypt a message, the message is written on a strip of paper or a stick and wrapped around the cylindrical object using the keyword to determine the number of columns. The message is then read across the columns, from top to bottom. The result is an encrypted message in which the letters appear in a different order than in the original message.

To decrypt the message, you need to know the keyword used to encrypt it, since it determines the number of columns and the order in which the letters must be read.

</details>


3. [Polybios](https://github.com/14wual/pycryptools/blob/main/about/README.md#polybios)

<details>

Usage: 
```python
from pycryptools.polybios import polybios

message = "example"

encrypt = polybios.encrypt(message)
print(encrypt)

decrypt = polybios.decrypt(encrypt)
print(decrypt)
```

The Polybios cipher is a polyalphabetic substitution cipher technique that uses a 5x5 table to assign a pair of numerical coordinates to each letter of the alphabet. The table is built using a 5x5 matrix where the letters of the alphabet are placed in a specific order, rather than in alphabetical order.

</details>

4. [Caesar](https://github.com/14wual/pycryptools/blob/main/about/README.md#caesar)

<details>

```python
from pycryptools.caesar import caesar

message = "example"
keyword = 9

encrypt = caesar.encrypt(message, keyword)
print(encrypt)

decrypt = caesar.decrypt(encrypt, keyword)
print(decrypt)
```

The Caesar cipher is a single substitution cipher method in which each letter in the original text is replaced by another letter that is a fixed number of positions later in it. This fixed number is known as the encryption key. For example, if the key is 3, then 'A' is replaced with 'D', 'B' is replaced with 'E', and so on. The registered Caesar is one of the earliest and simplest known methods.

</details>

5. [Alberti Disk](https://github.com/14wual/pycryptools/blob/main/about/README.md#alberti)

<details>

Usage:
```python
from pycryptools.alberti import alberti

message = "example"
outer_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
inner_alphabet = "XZYWVUTSRQPONMLKJIHGFEDCBA"

encrypt = alberti.encrypt(message, inner_alphabet, outer_alphabet)
print(encrypt)

decrypt = alberti.decrypt(encrypt, inner_alphabet, outer_alphabet)
print(decrypt)
```

The Alberti disk is a mechanical device used to encrypt and decrypt messages using the polyalphabetic substitution cipher. It was invented by the Italian humanist and scientist Leon Battista Alberti in the 15th century. The disk consists of two overlapping wheels, each with an alphabet printed on its rim. The top wheel, known as the recorder wheel, is free to rotate and has a hole in the center through which the bottom wheel, known as the decryption wheel, can be seen.

</details>