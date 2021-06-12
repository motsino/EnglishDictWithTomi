from django.shortcuts import render
from PyDictionary import PyDictionary
# Create your views here.


def index(request):
    return render(request, 'index.html')


def word(request):
    search = request.GET.get('search')
    dictionary = PyDictionary()
    meaning = dictionary.meaning(search)
    synonyms = dictionary.synonym(search)
    antonyms = dictionary.antonym(search)
    context = {
        'meaning': meaning['Noun'][0],
        'synonyms': synonyms,
        'antonyms': antonyms,
    }
    # syns = []
    # ants = []
    # for synonym in synonyms:
    #     syns.append(synonym)
    # for antonym in antonyms:
    #     ants.append(antonym)

    # context = {
    #     'syns': syns,
    #     'ants': ants,
    #     'meaning': meaning['Noun'][0],
    #     }
    return render(request, 'word.html', context)
