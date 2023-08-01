import requests

# word = 'word'

def fetch_word_meaning(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return "Failed to fetch data"

