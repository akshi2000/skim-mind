import os

mostUsedWords = []

def loadWords():
    if(len(mostUsedWords) > 0):
        return
    try:
        print(os.getcwd())
        with open('mostUsedWords.txt', 'r') as text_file:
            data = list(text_file.read().replace('\n', ' ').split())
            for word in data:
                mostUsedWords.append(word)
    except:
        print("Couldn't Load Words")

def getReturnResponse(text):
    data = list(text.replace('\n', ' ').split())
    resp = []
    loadWords()
    for word in data:
        if word in mostUsedWords:    
            resp.append({'word': word, 'factor' : 0.4}) 
        else:
            extra = 0
            if(word[-1] == '.'):
                extra = 0.2
            if(word[-1] == ','):
                    extra = 0.1
            resp.append({'word': word, 'factor' : 0.5 + extra})
    return resp
