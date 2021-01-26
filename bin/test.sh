#!/bin/bash

function propmt_test() {
    echo -n "Tests -- Script Name >> "
    read name

    if [ $name != "*" ]; then
        if python "tests/test_$name.py"; then
            printf "\n\nError occured while running tests."
        else
            echo "Tests run successfully."
        fi
    else
        echo "lmao what?"
    fi
}

# propmt_test
python "test.py"

echo "Done!"
