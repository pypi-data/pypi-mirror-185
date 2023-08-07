# Dumbo Scopus

Simple CLI to search on Scopus and obtain the results in a XLSX file.


# Prerequisites

- Python 3.10
- An API key from http://dev.elsevier.com


# Install

```bash
$ pip install dumbo-scopus
```


# Usage

Use the following command line:
```bash
$ python -m dumbo_scopus "TITLE(magic sets)" --api-key=YOUR-API-KEY
```

A file `scopus.xlsx` with the results will be produced.
Add `--help` to see more options.
