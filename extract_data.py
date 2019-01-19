#!/usr/bin/env python
#  coding: utf-8
import pickle

import PyPDF2
import numpy as np

"""
The purpose of this 
"""

pdf_file = 'doc-api/DataCatalog_v5.07.pdf'

pdf = open(pdf_file, 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf)
par = ['Name', 'Also Known As', 'Description', 'Domain', 'Default value', 'Source database',
       'Source field name', 'Source sub-field identifier', 'Comments', 'Modification history']


#  # Table description

def get_table_description(page: int):
    """
    Returns the description of the table described at the given page(if there is one)
    Args:
        page: page number in the DataCatalog_v5.07.pdf (starts at 0)

    Returns:
        - nested dicts {tab_name: {'description':str, page:int}}
        - or empty dict when no table description at the given page

    """
    corpus = pdf_reader.getPage(page).extractText().replace('\n', '').replace('  ', '\n').split('\n')[1:]
    tab_name = corpus[0].split(':')[0]
    if tab_name[:3] == 'TLS':
        paragraphs = [i for i in range(len(corpus)) if tab_name in corpus[i]]
        if len(paragraphs) == 1:
            return {tab_name: {'description': '\n'.join(corpus), 'page': page + 1}}
        else:
            return {tab_name: {'description': '\n'.join(corpus[paragraphs[0]: paragraphs[1]]), 'page': page + 1}}
    else:
        return {}


# Var description

def get_variable_description(page: int):
    """
    Returns the description of the variable described at the given page (if there is one)
    Args:
        page: page number in the DataCatalog_v5.07.pdf (starts at 0)

    Returns:
        - nested dicts {var_name:{desc1:str, desc2:str, ..., page:int}}
        - empty dict when no table description at the given page

    """

    var_dict = {}
    text = pdf_reader.getPage(page).extractText()
    var_name = text.replace('\n', '').replace('  ', '\n').split('\n')[1].split(' ')[0]
    count = 0
    for p in par:
        if p in text:
            count += 1
    if count >= 3:
        for i in range(len(par) - 1):
            j = 1
            while j <= len(par) - (i + 1):
                start = par[i]
                end = par[i + j]
                j += 1
                if start in text and end in text:
                    var_dict.update({par[i]: text.replace('\n', '').replace('  ', '\n').split(start)[1].split(end)[
                        0].replace(':', '')})
                    break
        var_dict.update({'page': page + 1})
        return {var_name: var_dict}
    else:
        return {}


meta = {'Author': 'European Patent Office',
        'Distribution': 'EPO PATSTAT customers',
        'PATSTAT Edition': '2016 Spring Edition',
        'Version': '5.07',
        'Date': '01.04.2016'}

tables = {}
no_desc = []
for page in np.arange(1, 200):
    try:
        tables.update(get_table_description(page))
    except:
        no_desc += [page]

variables = {}
no_desc = []
for page in np.arange(1, 275):
    try:
        variables.update(get_variable_description(page))
    except:
        no_desc += [page]

doc_patstat = {'meta': meta, 'tables': tables, 'variables': variables}

pickle.dump(doc_patstat, open('doc-api/patstat2016a_doc-api.pickle', 'wb'))






# Snippet

# print(pdf_reader.getPage(67).extractText()) #

# primer on table description

# l_page = 68
# text = pdf_reader.getPage(l_page).extractText()
# print(text[:50])

# we get rid of the chapeau
# corpus = text.replace('\n', '').replace(' ', '\n').split('\n')[1:] print(corpus[:5])
# we store the table name in a var
# table_name = corpus[0].split(':')[0]
# print(table_name)
# bounds = [i for i in range(len(corps)) if table_name in corpus[i]] print('\n'.join(corpus[bounds[0]: bounds[1]]))
