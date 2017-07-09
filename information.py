
import wikipedia       #https://pypi.python.org/pypi/wikipedia/
import requests
from bs4 import BeautifulSoup
from gtts import gTTS
import os

opt = input("What do you want?: Listen to the LATEST NEWS or SOME OTHER INFO.Press 1 for news or 2 for others:\n")
if opt == '1':
    def news():

        content = " "
        # the target we want to open
        url = 'http://www.hindustantimes.com/top-news'

        # open with GET method
        resp = requests.get(url)

        # http_response 200 means OK status
        if resp.status_code == 200:
            print("Successfully Scrapped")
            print("The news is as follow :-\n")

            # we need a parser,Python built-in HTML parser is enough .
            soup = BeautifulSoup(resp.text, 'html.parser')
            # print(soup.prettify())
            # l is the list which contains all the text i.e news
            l = soup.find("ul", attrs={'class': 'latest-news-bx more-latest-news more-separate'})
            # Notice here its findAll, above it was find only
            # find all the elements of a, i.e anchor
            for i in l.findAll("a"):
                content += i.text
                content += "."
                content += ","
            return content
        else:
            content = "Error Occurred"
            return content


    news_found = news()
    language = 'en'
    myobj = gTTS(text=news_found, lang=language, slow=False)
    myobj.save("news.mp3")
    os.system("news.mp3")
else:
    topic = input("Enter the topic you want to hear about: ")
    lang = input("Enter your preferred language(Hindi/English): ")

    #function to handle request to listen in hindi language


    def hindi():
        wikipedia.set_lang("hi")
        info = wikipedia.summary(topic, sentences=1)
        language = 'hi'       #for hindi audio by gTTS
        myObj = gTTS(text=info, lang=language, slow=False)
        myObj.save("go.mp3")
        os.system("go.mp3")

    #function to handle request to listen in english language


    def eng():
        wikipedia.set_lang("en")
        info = wikipedia.summary(topic, sentences=2)
        language = 'en'
        myObj = gTTS(text=info, lang=language, slow=False)
        myObj.save("go.mp3")
        os.system("go.mp3")

    if lang == "hindi" or lang == "Hindi" or lang == "HINDI":
        hindi()
    else:
        eng()

    #Aman Vats Creation

