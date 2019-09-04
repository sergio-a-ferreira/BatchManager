#! /usr/bin/env python3

"""
python3 scripts/modules, classes, methods/functions template
with built-in skeleton for help, documentation, basic unit testing, cli options

Classes:
  - className()

Methods:
  - methodName(self, **kwargs)

Functions:
  - functionName(*args, **kwargs)

Usage:
  !>>> from template import className()
  !>>> var = className()
  !>>> var
  !<dir.module.class instance at 0x11eb128>

See Also:
  N/A

Notes:
  N/A

Todo:
  externalise unit test system and help / documentation system

"""

"""Version:"""
__version__ = '0.1'

"""Author:"""
__author__ = "Sergio Ferreira"

"""Date:"""
__date__ = "2018-04-18"


class className():
  """
  class description

  attributes:
    N/A

  methods:
    - method(signature)

"""

  def __init__(self):
    """construtor"""
    pass


  def method_name(self, **kwargs):
    """
    method description

    Args:
      arg01: type <name>
        arg01 description
      argXY: type <name>
        argXY description

    Returns: type
      return description

    Raises:
      errors raized

    Examples:
      !>>> var.isType(1, int)
      True
      !>>> var.isType(1, str)
      False
    """
    pass


def function_name(*args, **kwargs):
  """
  function description

  Args:
    arg01: type <name>
      arg01 description
    argXY: type <name>
      argXY description

  Returns: type
    return description

  Raises:
    errors raized

  Examples:
    !>>> var.isType(1, int)
    True
    !>>> var.isType(1, str)
    False
  """
  pass


def fn_example(values):
  """
  function / method with built-in unit test example; 
  this example computes the arithmetic mean of a list of numbers.

  Args:  
    values: list of integers

  Returns: integer

  Examples:
    >>> print(fn_example([20, 30, 70]))
    40.0
    """
  return sum(values) / len(values)


def __main__():
  """
  get options
    help && manual
    tests
    debug / logging verbosiness levels
  """
  """ test: to test.py"""
  #import doctest
  #doctest.testmod(name='fn_example')
  
  """ manual && help: to help.py """
  # help on template.py
  #help(__name__)
  # help on class / method / function
  help(__main__)
  #print(className.__doc__)
  #help(className)
  #help(functionName)
  #help(fn_example)

  #print(fn_example([10,24,12,4]))
  pass


if __name__ == '__main__':
    __main__()


