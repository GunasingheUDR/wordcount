from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def count(request):
    full_text = request.GET['full_text']

    wordlist = full_text.split()

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] +=1
        else:
            worddictionary[word] = 1


    return render(request,'count.html', {'full_text':full_text,'count':len(wordlist), 'worddictionary':sorted(worddictionary.items())})

def about(request):
    return render(request,'about.html')
