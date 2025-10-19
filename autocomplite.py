def autocomplite(string, cloud):
    result_cloud = []
    for i in cloud:
        word = ''.join(let for let in i if let.isalpha())

        if word.lower().startswith(string.lower()):
            result_cloud.append(i)
    return result_cloud[:5]

print(autocomplite('ai', ['airplane','airport','apple','ball', 'airdrop', 'air', 'AI', 'airbus']))