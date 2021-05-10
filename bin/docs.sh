echo -n "Installing... "
npm install serve > /dev/null 2>&1
echo "Done!"

cd "./docs"
make clean html
serve "./_build/html/"
