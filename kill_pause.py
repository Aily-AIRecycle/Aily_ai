# detect.py 중단시키는 code2.py 종료(kill)
import os
import signal

# Get the process ID of the second code
file = 'pause.txt'
with open(file, "r") as f:
    pid = int(f.readline())

# Send a SIGTERM signal to the process, which will stop it gracefully
os.kill(pid, signal.SIGTERM)
if os.path.isfile(file):
  os.remove(file)
