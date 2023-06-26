"""
pause.py 실행을 중지시키는 파일.
"""
import os
import signal

# Get the process ID of the second code
file = 'C:/Aily/yolov5/pause.txt'
with open(file, "r") as f:
    pid = int(f.readline())

# Send a SIGTERM signal to the process, which will stop it gracefully
os.kill(pid, signal.SIGTERM)
if os.path.isfile(file):
  os.remove(file)

