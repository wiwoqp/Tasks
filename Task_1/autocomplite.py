def autocomplite(string, words):
    result_words = []
    for i in words:
        word = ''.join(letter for letter in i if letter.isalpha())

        if word.lower().startswith(string.lower()):
            result_words.append(i)
    return result_words[:5]

print(autocomplite('ai', ['airplane','airport','apple','ball', 'airdrop', 'air', 'AI', 'airbus']))