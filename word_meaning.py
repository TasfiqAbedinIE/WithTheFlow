import requests

word = input("Enter Word: ")

def fetch_word_meaning():
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Failed to fetch data")
        return None

word_meaning = fetch_word_meaning()

print(word_meaning)
print(len(word_meaning))

definitions = []
f_def = []

for entry in word_meaning:
    word = entry['word']
    meanings = entry["meanings"]
    for meaning in meanings:
        pos = meaning['partOfSpeech']
        definitions.append(meaning['definitions'])
        for all in definitions:
            f_def.append(all[0]['definition'])
        # for definition in definitions:
        #     f_def = definition["definition"]

print(word)
print(definitions)
print(f_def[0])

