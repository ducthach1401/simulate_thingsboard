import subprocess
import _thread

FILE = "token.txt"

def run_device(token):
    subprocess.run(["python3","./test_device.py",token])

token_file = open(FILE, 'r')
tokens = token_file.read().split()
for token in tokens:
    _thread.start_new_thread(run_device, (token, ))
while True:
    pass