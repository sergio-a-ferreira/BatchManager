#! /usr/bin/env python3

"""
test script for BatchManager.optionMenu

usage:
	python options_t.py 

"""
from BatchManager import optionMenu

__version__ = '0.1'
__author__ = "Sergio Ferreira"
__date__ = "2018-04-28"

kwargs = {
  'description': "test script for BatchManager.optionMenu",
  'version': __version__, 'data': __date__, 'author': __author__, 'help': True
}


def main():
	"""
    to run as script

    >>> print(main) #doctest: +ELLIPSIS
    <function main a 0x...>

    """
	menu = optionMenu(**kwargs)
	menu.create_menu(verbose = False, log = False, config = False)

	print("\nmenu.args:\n\t", type(menu.args), "\n\t", menu.args, "\n")

	if menu.args._manual:
		help(menu.module)
		exit(0)

	#import doctest, BatchManager
	#doctest.testmod(BatchManager.options)

	#python -m doctest -v .\options.py

if __name__ == '__main__':
	main()

