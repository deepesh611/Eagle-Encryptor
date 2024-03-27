
# Change directory to ./src
Set-Location ./src

# Install dependencies using requirements.txt
pip install -r requirements.txt

# Run setup.py script
python setup.py

# Generate with pyarmor
pyarmor gen ./setup.py ./main.py ./lib.py

# Change directory back to the previous location
Set-Location ..
