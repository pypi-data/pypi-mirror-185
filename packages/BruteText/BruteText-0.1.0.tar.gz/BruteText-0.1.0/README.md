# Brute Text
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
Use `python3 -m BruteText Your text to be typed` to type your text. If you like to change the time interval you can use the program as `python3 -m BruteText -t x Your text to be type` where x is the time (milliseconds) to wait between inputs.

### As a module
You can import this script and use it like this:
```py
import BruteText

BruteText("Text to be typed", x)  ## x where the time (milliseconds) between inputs.
```
