"""
template for test scripts

usage:
	template_t.py

"""

import template

__version__ = '0.1'
__author__ = "Sergio Ferreira"
__date__ = "2019-08-18"

kwargs = {
  'description': "test template " + __file__,
  'version': __version__, 'data': __date__, 'author': __author__,
  'help': True
}


""" insert your tests """
def main():
	values=[2, 15, 54, 22, 33]
	mean = template.fn_example(values)
	print(mean)


if __name__ == '__main__':
    main()