from datetime import date
from bs4 import BeautifulSoup
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import requests 
from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def index():
    return {"name": "First Data"}




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
    print(title)

    analysis = TextBlob(title)
    print(analysis.sentiment)
    polara.append(analysis.sentiment.polarity)
    subje.append(analysis.sentiment.subjectivity)
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

# for i in answer:
#     print(i)
#     titles[counts] = title
# for title in titles:
#     print(title)

# mainTitle = content.find("h3", class_ = "indicate-hover css-vip0cf")
# print(mainTitle.text)

app = FastAPI()

@app.get("/")
def index():
    return {"name": "First Data"}