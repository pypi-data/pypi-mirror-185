
# fhm-unittest

A package for unittest. It will take two parameters where the first parameter will be the returned value and the second parameter will be the expected value.



### Installation Instructions
Using PIP via PyPI
```
pip install fhm-unittest
```
for installing on Google Colab:
```
! pip3 install fhm-unittest
```

### Usage
```
>>> import fhm_unittest as unittest
```
To test a function, call the output_test function as pass your returned value and expected value as parameters

```
>>> unittest.output_test(returned value, expected value)
```

### Example - 01
```
def even_odd_checker(number):
  if number % 2 == 0:
    return 'The number is even'
  else:
    return 'The number is odd'
```
```
>>> unittest.output_test(even_odd_checker(10), 'The number is even')
    Accepted
```

### Example - 02
```
def even_odd_checker(number):
  if number % 2 == 0:
    return 'even'
  else:
    return 'odd'
```
```
>>> unittest.output_test(even_odd_checker(10), 'The number is even')
    Accepted [90%]
```

### Example - 03
```
def even_odd_checker(number):
  if number % 2 == 0:
    return 'even'
  else:
    return 'odd'
```
```
>>> unittest.output_test(even_odd_checker(10), 'The number is odd')
    Wrong Answer [45%]
```
