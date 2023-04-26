# gitlag

## Install

```sh
git clone git@gitlab.be-md.ncbi.nlm.nih.gov:pd/do/p2/ex/radetska2/kata/gitlag.git
cd gitlag
virtualenv -p python3.9 venv
source venv/bin/activate
pip install -r requirements/test.txt -e .
```

## Test

To run tests:

```sh
py.test
```
