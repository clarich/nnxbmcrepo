#!/bin/bash

git submodule update
python repo_prep.py
for dir in `git submodule | cut -d' ' -f3`; do cp -fr $dir repo/; done
cp -fr repository.nuskunetworks repo/
for item in `find ./repo/ -iname .git`; do rm -rf $item ; done
cd repo/repository.nuskunetworks
rm -rf .git
cd ../../

