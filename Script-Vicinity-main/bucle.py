from main import *
import time

exe = True
try:
    while exe == True:
        main()
        time.sleep(5)
except Exception as e:
    print(f"Error {e}")