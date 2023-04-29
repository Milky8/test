from linenotipy import Line
import os
import requests

#Your Account
'ltuid' = os.environ.get(LTUID)
'ltoken' = os.environ.get(LTOKEN)

account_1 = {'ltuid': ltuid, 'ltoken': ltoken}

#Line_Token
Line_notify = False
Line_TOKEN = Line(token='')

#Discord_Webhook
webhook = 'https://discord.com/api/webhooks/1101237890232631450/WV_MAzqXlcbjSvL66YJHM4lgv30CKBvVA6ftbVmW8yTgp3SHUQE7Oi75RtvYaHZSSTTI'

#Discord_notify
discord_notify = True
discord_server = [  
                    ''
                 ]
