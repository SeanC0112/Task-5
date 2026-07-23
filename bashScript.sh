apt install python3.12 python3.12-venv python3.12-dev -y
apt install pip -y

python3 -m venv venv
source venv/bin/activate

pip install --upgrade pip
pip install gymnasium
pip install numpy
pip install stable_baselines3
pip install stable-baselines3[extra]
pip install gym[box2d]

python3 carracinggym.py