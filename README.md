# READ ME

## Prior words

The goal of this repo is to build a Python documentation API for PatStat2016a. This is meant to be a temporary repo for dev. 

Ultimately, the output and functions will be part of the open PatStat2016a. Actually, this is already the case but the current version is still incomplete.

## Current (main) issues

1. Variable documentation is incomplete whenever it exceeds 1 page in the original pdf.
2. The documentation display in notebooks does not survive preview

## Desirable features

- Provide a way to  quickly  visualize table interdependencies
- Provide a library of standard SQL query for getting started (see for example de Rassenfosse, G., Kracker, M. & Tarasconi, G., 2017. "Getting Started with PATSTAT Register". Australian Economic Review 50(1), 110-120 and de Rassenfosse, G., Dernis, H. & Boedt, G., 2014. "An introduction to the Patstat database with example queries". Australian Economic Review 47(3), 395-408.)

## Finding your way in `docPatStat`

- `DataCatalog_v5.07.pdf` : EPO data catalog (input documentation)
- `dev-snippets`: a notebook with snippets and dev features (this is the lab of the repo)
- `extract_data`: script to extract data from `DataCatalog...` and compile the relevant data in `patstat2016a_doc-api.pickle`
- `shortdoc.py` functions to query the pickle file 