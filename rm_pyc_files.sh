echo "Deleting pyc files from: `pwd`"
find . -name "*.pyc" -not -path "*/venv/*" -exec rm {} \;
