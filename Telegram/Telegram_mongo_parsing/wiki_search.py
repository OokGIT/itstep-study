import wikipedia
wikipedia.set_lang("uk")


def wiki_search_summary(message):
    result = wikipedia.summary(f'{message}')
    return result

# print(wiki_search_summary("Зеленський"))