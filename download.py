import os
import time
import sys
import datetime
from subprocess import call

with open('streamlink_master_id.txt') as f:
    ids = f.read().splitlines()

with open('streamlink_master_list.txt') as f:
    links = f.read().splitlines()

id_map = dict(zip(ids, links))

current_section = int(sys.argv[1])
number_section = int(sys.argv[2])

index = current_section
while index < len(ids):
        key = ids[index]
        print(index+1, key)
        try:
            os.makedirs(key)
        except FileExistsError:
            pass    
        now = datetime.datetime.now().strftime('%Y-%m-%d_%H_%M_%S')
        call("timeout -sHUP 5s streamlink "+id_map[key]+" best -o "+key+"/"+now+".mp4", shell = True)
        print("timeout -sHUP 60s streamlink "+id_map[key]+" best -o "+key+"/"+now+".mp4")
        index += number_section
