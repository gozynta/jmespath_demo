# JMESPath Python Kubernetes Yaml Example

## Overview
Finding no good jsonpath libraries for Python, this is the best method I've found so far of manipulating kubernetes yamls (or any other data structure represented as nested dicts/lists).

See the [blog post I wrote on this topic](https://www.gozynta.com/blog/posts/yaml-json-python-jsonpath-jmespath/).

## Usage
Take a look at the code under pysrc/.

If you want to run the tests, use
```bash
PYTHONPATH=pysrc pipenv run pytest pytests
```

## Dev Prerequisites
- python 3.9
- pipenv
- (optional) VSCode with `editorconfig.editorconfig`, `ms-python.python`, and `ms-python.vscode-pylance` extensions installed

## Dev Installation

```bash
pipenv install -d
./dev-scripts/install
```
