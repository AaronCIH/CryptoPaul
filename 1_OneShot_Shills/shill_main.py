# %%
'''
create by Cihsiang, 2022/03/03
This tool is convenient for one-click shill !
'''
from threading import get_native_id
import requests
import json
import random
import time
from datetime import datetime
import pandas as pd
import re

def oneshot_shill(shill_chs, authorization_list, content):
    for author in authorization_list: # multi_users
        # step1. choice header, designated user
        header = {
            "Authorization": author,
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
        }
        # step2. define shill messages.
        msg = {
            "content": content,
            # "nonce": "82329451214{}33232234".format(random.randrange(0, 100)),
            "tts": False,
        }
 
        print(content)
        # step3. loop for every channels.
        for index in range(len(shill_chs)):
            """
            [DC, Channel, Url, Vaild]
            """
            data = shill_chs.loc[index].values
            DC = data[0]
            Channel = data[1]
            channel_id = data[2].split('/')[-1]
            shill_chs.loc[index, 'Vaild'] = False
            time.sleep(2)
            try:      
                # step3-1. verify the pid useful.
                url = "https://discord.com/api/v9/channels/{}/messages?limit=5".format(channel_id)
                res = requests.get(url=url, headers=header)
                json_results = json.loads(res.text)
                num_array = len(json_results)
                if num_array>0:
                    shill_chs.loc[index, 'Vaild'] = True
                
                # step3-2. post the content.
                try:
                    res = requests.post(url="https://discord.com/api/v9/channels/{}/messages".format(channel_id), headers=header, data=json.dumps(msg))
                    print("{%s}-[%s] : shill finish!" %(DC, Channel))
                except:
                    print("{%s}-[%s] : shill time limit!" %(DC, Channel))
            except:
                print("{%s}-[%s] : shill link timeout!" %(DC, Channel))
            continue
        print(datetime.now())
        shill_chs.to_csv("./2_shill_chs.csv", index=False)

if __name__ == "__main__":
    #1. put channel id here
    ##################################################################
    # use shill_chs.loc[0].values
    # [DC, Channel, url, Vaild], pid need to split('/')[-1] with url.
    ##################################################################
    shill_chs = pd.read_csv('./2_shill_chs.csv') 
    shill_chs['Vaild'] = None

    #2. put authorization here
    with open('./0_authorizations.txt', 'r') as F:
        Auth = F.read()
    authorization_list = Auth.split('\n')

    #3. read content
    with open('./1_shill_content.txt', 'r', encoding='UTF-8') as F:
        content = F.read()

    #3. repeat
    while True:
        print("# GetList ==================")
        oneshot_shill(shill_chs, authorization_list, content)
        print(shill_chs.head())
        #check frequency : every 1~2 hrs by default( in seconds )
        sleeptime = random.randrange(3600, 7200)  # units is seconds.
        for i in range(int(sleeptime)):
            if i%10==0:
                print('.', end='')
            time.sleep(1)
        print("")            
