from datetime import date
from unicodedata import name
from bs4 import BeautifulSoup
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import requests 
from fastapi import FastAPI
from pydantic import BaseModel
import itertools
import gc




class Title():
    
    def __init__(self,id, title, polarity,subjectivity):
        self.id = id
        self.title = title
        self.polarity = polarity
        self.subjectivity = subjectivity

    def __str__(self):
        return  "\nTitle: " + self.title + "\npolarity: " + str(self.polarity) + "\nsubjectitvity: " + str(self.subjectivity)
   
    


source = requests.get("https://www.nytimes.com/").text


content = BeautifulSoup(source, "lxml")
#Date


#titles
titles= []
for h3 in content.find_all('h3', class_="indicate-hover css-1pvrrwb"):
    title = h3.text
    title = title.split()
    titles.append(title)

polara = []
subje = []
for counts, title in enumerate(titles):
    title = " ".join(title)
    titles[counts] = title

    analysis = TextBlob(title)
    polara.append(analysis.sentiment.polarity)
    subje.append(analysis.sentiment.subjectivity)

call = []
for i in range(len(titles)):
    titlei = Title(i,titles[i],polara[i],subje[i])
    call.append(titlei)

print(call[0])
dictionar={
    
    1: {
        call
    }
    
}
addedPol = 0
addedSub = 0
amount = len(polara)


for pol in polara:
    addedPol +=pol
totalPol = addedPol/amount
print("This is the average of all the titles at the New York times on ",date, "with a polarity of", totalPol)

for sub in subje:
    addedSub += sub
totalSub = addedSub/amount

if totalSub <= 0.5:
    print("The New York Times titles is on average more objective on",date, "with average score of", totalSub)
if totalSub > 0.5:
    print("The title is on average more subjective with average score of", totalSub)



app = FastAPI()

@app.get("/")
def index():
    return {"name": "First Data"}

@app.get("/get-list/{list_id}")
def get_list(list_id: int):
    return(dictionar[list_id])
    


