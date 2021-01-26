#!/bin/bash

function propmt_clear() {
    echo -n "Clear the screen? >> "
    read res

    if [ $res == "yes" ]; then
        clear
    else
        echo "Skipping clear screen..."
    fi
}

echo "Upgrading Dist Tools..."
pip install --upgrade setuptools wheel twine
propmt_clear

echo "Building Distribution..."
python3 setup.py sdist bdist_wheel
propmt_clear


echo "Executing Distribution..."
python3 -m twine upload dist/*
propmt_clear

echo "Dist Done!"
echo "Removing PKG files/folders..."

rm -r "build"; rm -r "dist"
rm -r "valorant.egg-info"

echo "Done!"
