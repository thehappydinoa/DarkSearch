#!/usr/bin/env bash

pip install twine wheel

rm dist/*
python3 setup.py sdist bdist_wheel
python2 setup.py sdist bdist_wheel

twine upload dist/*
