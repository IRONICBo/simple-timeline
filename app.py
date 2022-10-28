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
URL = "http://english.hust.edu.cn/info/1102/3410.htm"

@app.route("/")
def index():
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

    text = get_document_data(URL)
    generate_wordcloud(text, SAVE_PATH)
    response = make_response(send_file(SAVE_PATH))
    response.headers["Content-Disposition"] = "attachment; filename=result.jpg;"

    return render_template('index.html',data=data)

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