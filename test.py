import datetime
from linenotipy import Line
Line_TOKEN = Line(token='8WsXx13EQKjQxxsgEUtBj1XpoE8lMfw5Zm0SuxkmO65')
Line_message_header = ('content-type:''application.x-www-form-urlencoded','Authorization:''Bearer ' , Line_TOKEN)
Line_date = datetime.datetime.now().date()
text_test = ["Account_1","Account_2","Account_3","Account_4","Account_5"]
result = []
for i, t in enumerate(text_test):
    result.append(str(i + 1) + ". " + t)

Line_message = '\nAuto Check-In Reward Honkai&Genshin \nประจำวัน '+str(Line_date)+' เรียบร้อย\n' + "\n".join(result)
print(Line_message)


Line_photo = "kokomi2.png"
Line_TOKEN.post(headers=Line_message_header, message=Line_message,imageFile=Line_photo)