import httpx

URLS = ['https://raw.githubusercontent.com/stopwords-iso/stopwords-ru/master/stopwords-ru.txt']

def save_from_url(urls: str):
    stopwords = set()
    for url in URLS:
        r = httpx.request('GET', url)
        current_stopwords = r.text.split('\n')
        stopwords |= set(current_stopwords)
    
    with open ('data/stop_words.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(stopwords))


def load_stopwords(path: str = "data/stop_words.txt") -> set[str]:
    stopwords = set()
    
    with open(path, encoding="utf-8") as f:
        for line in f:
            stopwords.add(line.rstrip())
    return stopwords

def without_stopwords(words: list[str]) -> list[str]:
    stopwords = load_stopwords()
    # return list(filter(lambda word: word not in stopwords, words))
    return[word for word in words if word.lower() not in stopwords]



if __name__ == "__main__":
    save_from_url(URLS)
