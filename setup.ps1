
cd ./src

pip install -r requirements.txt

./setup.py

pyarmor gen ./setup.py ./main.py ./lib.py

cd ..