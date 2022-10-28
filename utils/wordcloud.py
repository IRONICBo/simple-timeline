import jieba
import imageio
from wordcloud import WordCloud

sw_path = "utils/stop_words.txt"

class word_spliter():
    def __init__(self, text, stop_path = sw_path):
        self.text = text
        self.stop_word = stop_path

    def get_stopwords(self):
        stopwords = {}.fromkeys([line.rstrip() for line in open(self.stop_word, encoding='utf-8')])
        return stopwords

    def text_wash(self):
        self.text = self.text.encode(encoding="utf-8",errors='ignore').decode("utf-8")
        return self.text

    def split_word(self):
        seq = ''
        sw_words = self.get_stopwords()
        text = self.text_wash()
        segs = jieba.cut(text, cut_all=False)
        for seg in segs:
            if seg not in sw_words:
                seq = seq + seg + " "
        return seq


class wordclouder():
    def __init__(self, text, save_path):
        self.text = text
        self.save_path = save_path

    def word_cloud(self):
        word_pic = WordCloud(
            # font_path = 'XXX',
            max_words=100,
            background_color = 'white',
            mask = imageio.imread("static/cloud.png")
        ).generate(self.text)
        imageio.imsave(self.save_path, word_pic)
