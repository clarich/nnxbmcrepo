#!/bin/bash

git submodule update
python repo_prep.py
for file in `find ./ -iname *.zip | grep -v repo/`; do mv $file repo/; done

