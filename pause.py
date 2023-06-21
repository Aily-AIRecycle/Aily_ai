"""
detect.py를 실행했을때 중단시키는 파일
"""
import os
import time

# Write the process ID to a file.(pause.txt)
if not os.path.isfile('pause.txt'):
    with open("pause.txt", "w") as f:
        f.write(str(os.getpid()))
# f.close()
n = 0
while True: # 
    print(f"detect.py is stopped...{n}")
    n += 1
    time.sleep(1)
