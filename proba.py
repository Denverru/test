# from tabulate import tabulate

# data =[ 
#     ["APlle",1.2,7],
#     ["banana",1.2,7],
#     ["kralus",1.2,7],
# ]
# headers = ["Fruct","Price","amount"]
# print(tabulate(data,headers=headers,tablefmt='grid'))
from gtts import gTTS
import os

text = 'Привет мир, у тебя все будет хорошо'
language = 'ru'
tts = gTTS(text=text,lang=language)
tts.save("c:\\temp\\hello.mp3")

#os.system("mpg321 hello.mp3")