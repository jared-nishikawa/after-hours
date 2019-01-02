# Intro to Programming in Java

Willamette University

CS 231

Spring 2009

## Assignment 1

### Problem 1
User inputs a month, a day, and a year.

This program will print "true" if that is a valid date, and "false" if not.

Also, it will print whether or not the date falls on a weekend.

Reading: https://en.wikipedia.org/wiki/Zeller%27s_congruence

### Problem 2
User inputs four values:
- a height
- a width
- a thickness
- a quantity of cylindrical drinking glasses.

The program prints the volume of glass needed to fill this order.

Reading: https://en.wikipedia.org/wiki/Cylinder#Volume

Hint: What do you do with the thickness?

### Problem 3
User inputs a temperature in Fahrenheit, and a wind speed in mph.

The program displays the effective temperature (or "wind chill").

Reading: https://en.wikipedia.org/wiki/Wind_chill

## Assignment 2

### Problem 1

Print the first 50 values of the n! function, where n is an integer.

Reading: https://en.wikipedia.org/wiki/Factorial

### Problem 2
User inputs values for x and n, where x is the value to be used in approximating e^x, and n is the number of terms to be used (in the Taylor series approximation).

Reading: https://en.wikipedia.org/wiki/Exponential_function (See Taylor series)

### Problem 3
User inputs a value for x, and the program approximates sin(x) and cos(x)

Reading: https://en.wikipedia.org/wiki/Taylor_series (See Trigonometric functions)

## Assignment 3

Given a month and a year, the program checks for validity and either exits (for invalid dates, or dates that occurred before the beginning of the Gregorian calendar) or prints a formatted calendar of the month and year specified).


Reading:

- https://en.wikipedia.org/wiki/Zeller%27s_congruence
- https://en.wikipedia.org/wiki/Gregorian_calendar

## Assignment 4

### Problem 1

Given an integer between 0 and 1,000,000,000, this program prints that integer in English, with appropriate formatting (caps, hyphens, and commas).

Example:
```
Integer: 1234567
One million, two hundred and thirty-four thousand, five hundred and sixty-seven
```

### Problem 2

Implement the following array methods:
- `copy`
- `index_of` (get the index of a value)
- `is_in`
- `concat`
- `slice` (given two integer indices, return a sub array between those two indices)
- `remove`
- `bubble_sort`

Reading: https://en.wikipedia.org/wiki/Bubble_sort

## Assignment 5

### Problem 1

Open a text file and convert the contents to Pig Latin.  The program should prompt for the file name, open the specified file (if it exists), translate the contents to Pig Latin, and write the result to a new file.

### Problem 2

Vigenere Cipher

This program will prompt the user for three pieces of information:
- Secret key
- Mode (encrypt/decrypt)
- File name

The program should open the specified file, encrypt or decrypt it (as directed), and write the result to a new file.

Reading: https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher

