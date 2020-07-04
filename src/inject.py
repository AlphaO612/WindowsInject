import os
from time import sleep
import sys

arr = sys.argv
try:
    for i in range(len(arr)):
        if arr[i] == '-n':    
            name = arr[i+1]
        if arr[i] == '-w':
            way = arr[i+1]
        if arr[i] == '-set':
            mode = False
        if arr[i] == '-del':
            mode = True
    if not mode:
        os.system(f'SCHTASKS /delete /tn AirInject{name} /f')
        result = os.system(f'SCHTASKS /Create /SC ONLOGON /TN AirInject{name} /TR {way}')
        if result == 1:
            print('none')
        else:
            print('success')
    elif mode:
        result = os.system(f'SCHTASKS /delete /tn AirInject{name} /f')
        if result == 1:
            print('none')
        else:
            print('success')
    else:
        print('none')
except:
    print('none')