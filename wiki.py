import wikipedia

class wiki(object):
    def __init__(self, lang='en'):
        self.language = lang
        self.sentence = 4
        self.cache = dict()
        self.summ = dict()
        
    def run(self):
        for i in range(10):

            wikipedia.set_lang(self.language)
            self.input_text = input("Enter your article: \n")
            self.result = self.search(self.input_text)

            try:
                if( len(self.result) > 1):
                    if( self.input_text in self.cache.values()):
                        for k in self.cache:
                            if self.input_text in self.cache[k]:
                                search = k
                            wiki = self.summ[search]
                            print(f'fetched from the cache : \n{wiki}\n')
                    else:
                        wiki = self.summary(self.input_text, sentences=self.sentence)
                        print(f'{wiki}\n')
                        self.cache[i] = self.input_text
                        self.summ[i] = wiki
                else:
                    sugg = self.suggest(self.input_text)
                    print(f'No article with the name {self.input_text} was found. Inputted text is mentioned in the following articles: {sugg}\n')

            except wikipedia.exceptions.DisambiguationError as error:
                sugg = self.suggest(self.input_text)
                print(f'\nNo article with the name {self.input_text} was found. Inputted text is mentioned in the following articles: {sugg}\n')
    
    def search(self, input_text):
        return wikipedia.search(input_text)
    
    def summary(self, input_text, sentences):
       return wikipedia.summary(input_text, sentences=sentences)
    
    def suggest(self, input_text):
        return wikipedia.suggest(input_text)