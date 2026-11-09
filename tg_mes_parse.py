import json
from nltk.corpus import stopwords
from razdel import tokenize
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud

stop_words = set(stopwords.words("russian"))
stop_words.update(['это', 'ага', 'просто', 'понял', 'тебе', 'вообще', 'ещё', 'очень', 'вроде', 'сегодня', 'пока', 'завтра', 'всё', 'наверное', 'кстати', 'короче', 'давай', 'типо', 'типа', 'хотя', 'сколько', 'почему', 'вчера', 'буду', 'помню', 'окей', 'итоге', 'ща', 'ладно', 'круто', 'думаю', 'думал', 'стоит', 'прям', 'интересно', 'смотрел', 'жесть', 'точно', 'знаю', 'прикольно', 'походу', 'крутяк', 'знаешь', 'класс', 'чето', 'прямо', 'купить', 'нормально', 'взял', 'можешь', 'норм', 'ок', 'хз', 'чо', 'ваще', 'ого', 'блин', 'ахах', 'пхах', 'че'
                   'лол', 'хах', 'хаха', 'ща', 'чё', 'ну', 'ага'])

with open(r'J:\BERT\раздача\data\result_vitya.json', 'r', encoding='utf-8') as f: # put JSON's path here
    data = json.load(f)

with open(r'J:\BERT\раздача\data\stopwords-ru.txt', 'r', encoding='utf-8') as f: # don't forget about stop-words
    stops = {line.strip().lower() for line in f if line.strip()}

stop_words |= stops

def analysis(imp):

    def clean_text(text):
        if isinstance(text, str):
            return text
        if isinstance(text, list):
            return "".join(p for p in text if isinstance(p, str))
        return ""

    texts = []
    for msg in imp['messages']:
        t = clean_text(msg.get('text', '')).strip()
        if t:
            texts.append(t)

    all_text = ' '.join(texts)

    words = [t.text.lower() for t in tokenize(all_text)]
    words_count = [w for w in words if w.isalpha()]
    tokens = [w for w in words if w.isalpha() and w not in stop_words]

    most = Counter(tokens)

    print(f'Общее количество слов — {len(words_count)}')
    print(f'Количество уникальных слов — {len(set(words_count))}')
    print(f'Топ 30 самых популярных слов — {most.most_common(30)}')

    return ' '.join(tokens)

def plot_cloud(wordcloud):
    plt.figure(figsize=(16, 12))
    plt.imshow(wordcloud) 
    plt.axis("off")

wordcloud = WordCloud(width = 2000, 
                      height = 1500, 
                      random_state=1, 
                      background_color='black', 
                      margin=20, 
                      colormap='Pastel1', 
                      collocations=False).generate(analysis(data))

plot_cloud(wordcloud)
wordcloud.to_file('cloud.png')
plt.show()