from urllib.request import urlopen
import requests
import pandas as pd
import json

api_token = "1901776894:AAGa-wIXdBiqrCUDYMdh2ZhTr7W-PwVRSpk"
base_url = "https://api.telegram.org/bot{}/getUpdates".format(api_token)
old_mess = 1
update_id = 1

Data = pd.read_excel('Data.xlsx', header=None,names=['R','S'])
print(Data)

while 1:
    old_update_id = update_id
    resp = urlopen(base_url)
    content = json.loads(resp.read())
    n = len(content['result'])
    update_id =  content['result'][n-1]['update_id']

    if update_id > old_update_id:
        try:
            mess = content['result'][n-1]['message']['text']
            
            print(mess)
        except:
            pass
        print(len(Data))
        for i in range(len(Data)):
            if mess  == Data.iloc[i,0]:
                chat_id= content['result'][n-1]['message']['chat']['id']
                print(chat_id)
                text = Data.iloc[i,1]
                requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}".format(api_token,chat_id, text))
