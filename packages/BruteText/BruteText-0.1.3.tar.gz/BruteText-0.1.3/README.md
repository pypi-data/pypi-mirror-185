# Brute Text
![PyPI - Downloads](https://img.shields.io/pypi/dm/BruteText) ![PyPI - License](https://img.shields.io/pypi/l/BruteText) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/BruteText) ![PyPI](https://img.shields.io/pypi/v/BruteText) ![PyPI - Wheel](https://img.shields.io/pypi/wheel/BruteText) ![PyPI - Implementation](https://img.shields.io/pypi/implementation/BruteText)

This is a program which emulates text input like a brute force technique.

## Usage
You can both use it as imported and from terminal screen.

## Installation
```
pip install BruteText
```

or 

```
pip3 install BruteText
```

### Terminal
Use `python3 -m BruteText.brutetext Your text to be typed` to type your text. If you like to change the time interval you can use the program as `python3 -m BruteText.brutetext -t x Your text to be type` where x is the time (milliseconds) to wait between inputs.

### As a module
You can import this script and use it like this:
```py
from BruteText import bruteText

brutetext.bruteText("Text to be typed", x)  ## x where the time (milliseconds) between inputs.
```
