from threading import get_native_id
import requests
import json
import random
import time
from datetime import datetime
import pandas as pd
import numpy as np

def checkrepeat(Participate, DC, msg_id):
    hist_msgid = Participate.loc[Participate.loc[:,'DC']==DC, 'MSGid'].values
    print("HIST:", hist_msgid, " MSG:", msg_id)
    if msg_id in hist_msgid:
        print("====== repeat ======")
        return False
    return True

def getlist(Giveaways, authorization_list, Participate):
    for authorization in authorization_list:
        # step1. choice header, designated user
        header = {
            "Authorization": authorization,
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
        }
        # step2. loop for every channels
        for index in range(len(Giveaways)):
            """
            [DC, Channel, Keyword, Link]
            """
            data = Giveaways.loc[index].values
            DC = data[0]
            Channel = [1]
            Keyword = data[2]
            channel_id = data[3].split('/')[-1]
            Giveaways.loc[index, 'Vaild'] = False
            try:
            # if True:
                # step2-1. verify the link useful.
                url = "https://discord.com/api/v9/channels/{}/messages?limit=5".format(channel_id)            
                res = requests.get(url=url, headers=header)
                json_results = json.loads(res.text)
                num_array = len(json_results)
                if num_array>0:
                    Giveaways.loc[index, 'Vaild'] = True

                giveaway_botlist = [ "Giveaway Boat", "GiveawayBoat", "TylerTakesATrip", "Lawliet"]
                # step2-2. check messages.
                for i in range(0,num_array):
                    try:
                        if (Keyword in json_results[i]["content"]) or (json_results[i]['author']['username'] in giveaway_botlist): 
                            msg_id = json_results[i]["id"]    # 訊息編號
                            timestamp = json_results[i]["timestamp"]  # 編輯時間
                            react = json_results[i]['reactions'][0]['me']  # 是否已經按了
                            print("DC:{%s}, MSG:{%s}, Content:{%s}"%(DC, msg_id, json_results[i]["content"]))
                            url = "https://discord.com/api/v9/channels/{}/messages/{}/reactions/%F0%9F%8E%89/%40me".format(channel_id, '_'+str(msg_id))
                            requests.put(url=url, headers=header)
                            time.sleep(0.2)
                            if react == False:
                                # check repeat
                                print("=========================================================")
                                if checkrepeat(Participate, DC, '_'+str(msg_id)):
                                    Giveaways.loc[index, 'Touch'] = True
                                    Participate.loc[len(Participate)+1] = [authorization[:5], data[0], data[1], data[2], data[3], timestamp, '_'+str(msg_id), json_results[i]["content"]]
                            continue
                    except:
                        pass
                    continue
            except:
                pass
            continue
        print(datetime.now())
        Giveaways.to_csv("./1_Giveaway_chs.csv", index=False)
        Participate.to_csv('./2_Participate_log.csv', index=False)

if __name__ == "__main__":
    #1. put channel id here
    ##################################################################
    # use Giveaway_List.loc[0].values
    # [DC, Channel, Keyword, Link], Pid need to pick [1:]
    ##################################################################
    Giveaway_List = pd.read_csv('./1_Giveaway_chs.csv')   # 使用
    Giveaway_List['Vaild'] = None
    # Giveaway_List['Touch'] = None

    #2. put authorization here
    with open('./0_authorizations.txt', 'r') as F:
        Auth = F.read()
    authorization_list = Auth.split('\n')

    #3. Set result log
    ##################################################################
    # use to save touch history
    # [Auth, DC, Channel, Keyword, Link, Timestamp, MSGid, Content]
    ##################################################################
    Participate_log = pd.read_csv('./2_Participate_log.csv')

    while True:
        print("# GetList ==================")
        getlist(Giveaway_List, authorization_list, Participate_log)
        print(Giveaway_List.head())

        #check frequency : every 1~2 hrs by default( in seconds )
        sleeptime = random.randrange(300, 600)   # 預設間格時間 五分鐘至十分鐘檢查所有channels
        for i in range(sleeptime):
            print('.', end='')
            time.sleep(1)
        print("")            