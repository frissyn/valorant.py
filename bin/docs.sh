#!/usr/bin/env bash

echo -n "Installing... "
pip install sphinx > /dev/null 2>&1
pip install sphinx-rtd-theme > /dev/null 2>&1
echo "Done!"

cd "./docs"
make html
cd "./_build/html/"
ruby -run -ehttpd . -p 8080
