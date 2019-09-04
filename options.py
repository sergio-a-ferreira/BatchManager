#! /usr/bin/env python3

"""
command line option / argument parser
    standardizes common options: help, man, test, logging, debug, ...
    enables adding / removing specific options / option groups to modules / scripts


Usage:
    >>> from BatchManager import optionMenu

    >>> menu_cls = optionMenu

    >>> print(menu_cls)
    <class 'BatchManager.options.optionMenu'>

    >>> menu = optionMenu()

    >>> print(menu)     #doctest: +ELLIPSIS
    <BatchManager.options.optionMenu object at ...>
    

See Also:
    The Python Standard Library:
        argparse: Parser for command-line options, arguments and sub-commands

Notes:
    functions / methods and variables / atributes initialized as _ (e.g.: _var; _fun())
        are for internal use and may be changed without previous warning

TODO:
    N/A

"""

"""Version:"""
__version__ = '0.2'

"""Author:"""
__author__ = "Sergio Ferreira"

"""Date:"""
__date__ = "2018-04-20"

import os, sys
import argparse


class optionMenu():
    """
    creates an options / arguments menu object

    attributes:
        - prog
            <class 'str'> caller program
        - module
            <class 'str'> caller module
        - usage
            <class 'str'> program|module's summary usage
        - description
            <class 'str'> program|module's summary description
        - version
            <class 'str'> program|module's version
        - author
            <class 'str'> program|module's author
        - data
            <class 'str'> program|module's version's date
        - epilog
            <class 'str'>
        - parser
            <class 'argparse.ArgumentParser'> object parser

        Examples:
            >>> from BatchManager import optionMenu as opt
            >>> print(opt)
            <class 'BatchManager.options.optionMenu'>

    """

    def __init__(self, **kwargs):
        """
        sets defaults for optionMenu object atributes.
        creates a object parser to argparse.ArgumentParser()

        kwargs:
            description: <class 'str'>
                program's description
            author: <class 'str'>
                program's author
            data: <class 'str'>
                program's date
            version: <class 'str'>
                program's version
            epilog: <class 'str'>
                formatted string: version+data+author
            help: <class 'bool'>
                False to disable help menu; default True
            
        Returns: <class 'options.optionMenu'>
            optionsMenu object

        Raises:
            N/A

        Examples:
            >>> from BatchManager import optionMenu as opt

            >>> menu = opt(description = "built-in unit test: creating a new menu")

            >>> print(menu)    #doctest: +ELLIPSIS
            <BatchManager.options.optionMenu object at 0x...>
            >>> print(menu.module)  #doctest: +ELLIPSIS
            <module 'options' from...options.py'>
            >>> print(menu.prog)
            options.py
            >>> print(menu.help)
            True
            >>> print(menu.description)
            built-in unit test: creating a new menu
            >>> print(menu.epilog)
            options.py vN/A; by N/A [N/A]
        """

        self.prog = os.path.basename(sys._getframe(1).f_globals['__file__'])
        globals()['_my_module'] = __import__(os.path.splitext(self.prog)[0])
        self.module = globals()['_my_module'] 
        # XXX # self.usage = kwargs.get('usage', '%prog [OPTIONS] [KWORDS]')
        self.description = kwargs.get('description', 'insert a description of your program / class')
        self.author = kwargs.get('author', 'N/A')
        self.data = kwargs.get('data', 'N/A')
        self.version = kwargs.get('version', 'N/A')
        self.epilog = self.prog + " v" + self.version + "; by " + self.author + " [" + self.data + "]"
        self.help = kwargs.get('help', True)
        
        self.parser = argparse.ArgumentParser(
            prog=self.prog, add_help = self.help, description = self.description, epilog = self.epilog
        )


    def add_option(self, *flags, **kwargs):
        """
        adds an argument to an option group, defining how a single command-line argument should be parsed.
        [Note: just a parser to argparse.ArgumentParser.add_argument()]
        
        *flags: <class 'list'>
            a name or a list of names or flags; e.g. 'foo' '-foo' '-f'

        **kwargs: <class 'dict'>
            action:
                the basic type of action to be taken when this argument is encountered at the command line.
            nargs:
                the number of command-line arguments that should be consumed. 
            const:
                a constant value required by some action and nargs selections. 
            default:
                the value produced if the argument is absent from the command line.
            type:
                the type to which the command-line argument should be converted. 
            choices:
                a container of the allowable values for the argument. 
            required:
                whether or not the command-line option may be omitted (optionals only). 
            help:
                a brief description of what the argument does. 
            metavar:
                 a name for the argument in usage messages.
            dest:
                the name of the attribute to be added to the object returned by parse_args(). 

        Returns: updates the argparse.Namespace with a new option
            
        Raises:
            N/A

        Examples:
            >>> from BatchManager import optionMenu as opt

            >>> menu = opt(description = "built-in unit test: creating a new menu")

            >>> menu.add_option('-X', action = 'store', default = 0)

            >>> print(menu.parser)
            ArgumentParser(prog='options.py', usage=None, description='built-in unit test: creating a new menu', formatter_class=<class 'argparse.HelpFormatter'>, conflict_handler='error', add_help=True)
            >>> print(menu.parser.prog)
            options.py
            >>> print(menu.parser.usage)
            None
            >>> print(menu.parser.description)
            built-in unit test: creating a new menu
            >>> print(menu.parser.formatter_class)
            <class 'argparse.HelpFormatter'>
            >>> print(menu.parser.conflict_handler)
            error
            >>> print(menu.parser.add_help)
            True

        """
        self.parser.add_argument(*flags, **kwargs)


    def add_group(self, title = None, description = None):
        """
        creates an option group.
        [Note: just a parser to argparse.ArgumentParser.add_argument_group()]

        **kwargs: <class 'dict'>
            title:
                title for the sub-parser group in help output;
                by default "subcommands" if description is provided, otherwise uses title for positional arguments 
            description:
                description for the sub-parser group in help output,
                by default None

        Returns: updates the argparse.Namespace with a new group
            
        Raises:
            N/A

        Examples:
            >>> from BatchManager import optionMenu as opt

            >>> menu = opt(description = "built-in unit test: creating a new menu")

            >>> menu.add_group(title='testGroup', description='testing group addition')
            
            >>> print(menu.group)  #doctest: +ELLIPSIS
            <argparse._ArgumentGroup object at 0x...>
            >>> print(menu.group.title)
            testGroup
            >>> print(menu.group.description)
            testing group addition

        """
        self.group = self.parser.add_argument_group(title = title, description = description)


    def add_group_option(self, *flags, **kwargs):
        """
        adds an option to a option group
        [Note: just a parser to argparse.ArgumentParser.add_argument_group().add_argument()]

        *flags: <class 'list'>
            a name or a list of names or flags; e.g. 'foo' '-foo' '-f'

        **kwargs: <class 'dict'>
            action:
                the basic type of action to be taken when this argument is encountered at the command line.
            nargs:
                the number of command-line arguments that should be consumed. 
            const:
                a constant value required by some action and nargs selections. 
            default:
                the value produced if the argument is absent from the command line.
            type:
                the type to which the command-line argument should be converted. 
            choices:
                a container of the allowable values for the argument. 
            required:
                whether or not the command-line option may be omitted (optionals only). 
            help:
                a brief description of what the argument does. 
            metavar:
                 a name for the argument in usage messages.
            dest:
                the name of the attribute to be added to the object returned by parse_args().

        Returns: updates the current argparse.Namespace group with a new option
            
        Raises:
            N/A

        Examples:
            >>> from BatchManager import optionMenu as opt

            >>> menu = opt(description = "built-in unit test: creating a new menu")

            >>> menu.add_group(title='testGroupOption')
            
            >>> menu.add_group_option('-X', action = 'store', type = int, default = 0, dest = '_X')
                        
            >>> print(menu.group)  #doctest: +ELLIPSIS
            <argparse._ArgumentGroup object at 0x...>
            >>> print(menu.group.__dict__['_actions'][1])
            _StoreAction(option_strings=['-X'], dest='_X', nargs=None, const=None, default=0, type=<class 'int'>, choices=None, help=None, metavar=None)

        """
        self.group.add_argument(*flags, **kwargs)
        
        
    def create_menu(
        self, manual = True, test = True,  benchmark = True, version = True, epilog = True,
        verbose = True, log = True, config = True
    ):
        """
        creates the optionMenu object, setting defaults to common options

        kwargs:
            manual: <class 'bool'>
                enables 'manual' page option
            test: <class 'bool'>
                enables 'test' page option
            version: <class 'bool'>
                enables program / module version
            epilog: <class 'bool'>
                enables epilog line
            verbose: <class 'bool'>
                enables verbosity sub-menu
            log:
                enables logging sub-menu
            debug:
                enables debugging sub-menu
            config:
                enables configuraton sub-menu

        Returns: <class 'argparse.Namespace'>

        Raises:
            N/A

        Examples:
            >>> from BatchManager import optionMenu as opt

            >>> menu = opt(description = "built-in unit test: creating a new menu")

            >>> menu.add_group(title='testGroupOption')
            
            >>> menu.add_group_option('-X', action = 'store', type = int, default = 1000, dest = '_X')
                        
            >>> menu.create_menu()

            >>> print(menu.args)
            Namespace(_X=1000, _benchmark=False, _config_file=None, _config_format='cfg', _level=30, _log_file=None, _manual=False, _test=True, _verbose=3)
            
            >>> print(menu.args._X)
            1000

        """
        if manual:
            self.add_option('-m', '--m', '--manual', dest = '_manual', action = 'store_true', default = False, help = 'module / class manual page')

        if test or benchmark:
        	self.add_group(title = 'Tests and Benchmarks', description = 'enabling testing and benchmarking options')
        	self.add_group_option('-t', '--t', '--test', dest = '_test', action = 'store_true', default = False, help = 'test\'s the module')
        	self.add_group_option('-b', '--b', '--benchmark', dest = '_benchmark', action = 'store_true', default = False, help = 'benchmark\'s the module')

        if version:
            self.add_option('-V', '--version', action = 'version', version = '%(prog)s ' + self.version)


        if epilog is False:
            self.parser.epilog = None

        if verbose:
            self.add_group(title = 'Verbosity', description = 'stdout / stderr verbosity level; defaults to 3')
            self.add_group_option(
                '-v', '--v', '--verbose',
                dest = '_verbose', type = int, action = 'store', default = 3, metavar = '<int>',
                choices=list(range(6)),
                help = 'sets stdout / stderr verbosity level: 0 .. 5'
            )
            self.add_group_option(
                '-q', '--q', '--quiet',
                dest = "_verbose", action = "store_false",
                help = "sets verbosity to min level(--verbose = 0)"
            )
            self.add_group_option(
                '-d', '--d', '--debug',
                dest = "_verbose", action = "store_false",
                help = "sets verbosity to max level(--verbose = 5)"
            )

        if log:
            self.add_group(title = 'Log', description = 'log options')
            self.add_group_option(
                '-l', '--l', '--log-level',
                dest = '_level', type = int, action = 'store', default = 30, metavar = '<int>',
                choices=list(range(0, 51, 10)),
                help = "sets logging verbosity level: 0 .. 50"
            )
            self.add_group_option(
                '-L', '--L', '--log-file',
                dest = "_log_file", action = "store", metavar = "<file>",
                help = "/path/to/file"
            )

        if config:
            self.add_group(title = 'Config', description = 'configuration options')
            self.add_group_option(
                '-c', '--c', '--config-file',
                dest = "_config_file", action = "store", metavar = "<file>",
                help = "/path/to/file"
            )
            self.add_group_option(
                '-C', '--C', '--config-format',
                dest = "_config_format", action = "store", default = 'cfg', metavar = "<format>",
                choices = ['ini', 'cfg', 'conf', 'json', 'xml', 'csv', 'unl'],
                help = "file format: ini, cfg, conf, json, xml, csv, unl"
            )

        self.args = self.parser.parse_args()


def main():
    """
    to run module as script

    >>> print(main) #doctest: +ELLIPSIS
    <function main at 0x...>

    """
    kwargs = {
        'description': "standardizes common options and enables adding specific options to modules / scripts.",
        'version': __version__, 'data': __date__, 'author': __author__
    }
    menu = optionMenu(**kwargs)
    menu.create_menu()
    
    if menu.args._manual:
        help(menu.module)
        exit(0)

    if menu.args._test:
        import doctest
        doctest.testmod(verbose = True)


if __name__ == '__main__':
    main()
    
