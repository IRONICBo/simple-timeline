# save this as app.py
from flask import Flask
from flask import render_template
from flask import make_response,send_file

from utils.wordcloud import wordclouder,word_spliter

from urllib.request import urlopen

from bs4 import BeautifulSoup


app = Flask(__name__)

SAVE_PATH = "./static/result.jpg"
# URL = "http://english.hust.edu.cn/info/1102/3415.htm"
URL = "https://arxiv.org/"

@app.route("/")
def index():
    # 1. get data from static file
    data = [
        {
            "timestamp": "2022/10/27",
            "title": "HUST",
            "info": "咿咿呀呀嗷嗷",
        },
        {
            "timestamp": "2022/10/27",
            "title": "HUST",
            "info": "咿咿呀呀嗷嗷",
        },
        {
            "timestamp": "2022/10/27",
            "title": "HUST",
            "info": "咿咿呀呀嗷嗷",
        },
        {
            "timestamp": "2022/10/27",
            "title": "HUST",
            "info": "咿咿呀呀嗷嗷",
        }
    ]
    
    # 2. get data from local api
    # import requests
    # url = "http://127.0.0.1:5000/random"
    # response = requests.get(url)
    # data = response.json()
    
    text = get_document_data(URL)
    generate_wordcloud(text, SAVE_PATH)
    response = make_response(send_file(SAVE_PATH))
    response.headers["Content-Disposition"] = "attachment; filename=result.jpg;"

    return render_template('index.html',data=data)

@app.route("/random")
def random():
    import time
    dataItem = {
        "timestamp": "",
        "title": "",
        "info": "",
    }
    
    # generate random data with dataItem structure
    dataList = []
    for i in range(10):
        dataItem["timestamp"] = time.strftime("%Y/%m/%d", time.localtime())
        dataItem["title"] = "title" + str(i)
        dataItem["info"] = "info" + str(i)
        
        dataList.append(dataItem)
    
    return dataList

def generate_wordcloud(text, save_path):
    """
    : Generate wordcloud from text to save_path
    """
    sp_word = word_spliter(text)
    words = sp_word.split_word()
    g_word = wordclouder(words, save_path)
    g_word.word_cloud()

def get_document_data(url):
    """
    : Extract data from raw html document
    """
    html = urlopen(url).read()
    soup = BeautifulSoup(html, features="html.parser")

    # delete script and style
    for script in soup(["script", "style"]):
        script.extract()    # rip it out

    # get text
    text = soup.get_text()

    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)

    return text