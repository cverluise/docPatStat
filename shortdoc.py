#!/usr/bin/env python
#  coding: utf-8
import pickle

from IPython.display import display, Markdown, HTML


def print_warning():
    display(HTML('<font color=#1F618D>WARNING: completeness is not guaranteed</font>'))


def print_markdown(obj: dict):
    for k, v in obj.items():
        display(Markdown('**{}**: {}'.format(str(k).capitalize(), str(v).capitalize())))
    print_warning()


def print_signature():
    display(Markdown('*{}*'.format(', '.join(ShortDoc().version().values()))))


class ShortDoc:
    """
    Class returning the main features of the short doc
    """

    def __init__(self):
        self.desc = pickle.load(open('patstat2016a_doc-api.pickle', 'rb'))
        self.meta = self.desc['meta']
        self.tables = self.desc['tables']
        self.variables = self.desc['variables']

    def version(self):
        """
        Returns the version for which ShortDoc is relevant
        """
        return self.meta

    def list_tables(self):
        """
        Returns the list of tables supported by ShortDoc
        """
        return self.tables.keys()

    def list_variables(self):
        """
        Returns the list of variables supported by ShortDoc
        """
        return self.variables.keys()

    def desc_variable(self, var_code: str):
        """
        Returns the description of a given variable
        """
        return self.variables[var_code]

    def desc_table(self, tab_code: str):
        """
        Returns the description of a given table
        """
        return self.tables[tab_code]
