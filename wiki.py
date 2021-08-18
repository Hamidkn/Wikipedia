import wikipedia
import numpy as np

# lang = wikipedia.set_lang("fr")

# wiki = wikipedia.summary("Iran", sentences=4)

# print(wiki)
cache = dict()


for i in range(10):
    lang = input("Please choose your language(e.g: fr for French, en for English) :\n")
    wikipedia.set_lang(lang)

    input_text = input("Enter your article: \n")
    result = wikipedia.search(input_text)

    # if( len(result) > 2):
    #     res = result[0]
    # for term in res:

    try:

        if( len(result) > 1):
            if( input_text in cache.values()):
                for k in cache:
                    if input_text in cache[k]:
                        search = k
                wiki = wikipedia.summary(cache[search], sentences=4)
                print(f'fetched from the cache : \n{wiki}\n')
            else:
                wiki = wikipedia.summary(input_text, sentences=4)
                print(f'{wiki}\n')
                cache[i] = input_text
        
        else:
            sugg = wikipedia.suggest(input_text)
        # print(sugg)
            print(f'No article with the name {input_text} was found. Inputted text is mentioned in the following articles: {sugg}\n')
            cont = input("Do you want to continue: \n")
            if(cont == "Yes" or cont == "yes"):
                continue
            else:
                break

    except wikipedia.exceptions.DisambiguationError as error:
        # pass
        sugg = wikipedia.suggest(input_text)
        print(f'\nNo article with the name {input_text} was found. Inputted text is mentioned in the following articles: {sugg}\n')
        print(f'{error.options}\n')
    except wikipedia.exceptions.PageError as error:
         print(error)


# print(cache)


