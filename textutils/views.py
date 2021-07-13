#i have created this file-tushuli
from django.http import HttpResponse
from django.shortcuts import render
#def index(request):
    #return HttpResponse('''<h1><a href=" https://www.youtube.com/"> Youtube </a></h1>''')
#def about(request):
    #return HttpResponse('hey tushuli!!')

def index(request):

    return render(request,'index.html')
    #return HttpResponse("Home")

def ex1(request):
    sites = ['''<h1>For Entertainment </h1><a href = "https://www.youtube.com" >youtube video</a>''',
             '''<h1>For Interaction </h1><a href = "https://www.facebook.com" >Facebook</a>''',
             '''<h1>For Insight   </h1><a href = "https://www.ted.com/talks" >Ted Talk</a>''',
             '''<h1>For Internship   </h1><a href="https://internshala.com" >Intenship</a>''',
             ]
    return HttpResponse((sites))

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    spaceremover = request.POST.get('spaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext=analyzed
        #return render(request, 'analyze.html', params)


    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed= analyzed + char.upper()
        params = {'purpose': 'Converted to Uppercase', 'analyzed_text': analyzed}
        djtext=analyzed
        #return render(request, 'analyze.html', params)
    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed = analyzed  + char
        params = {'purpose': 'New Line Removed', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)
    if (spaceremover == "on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose': 'Space Removed', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)
    if (charcount == "on"):
        analyzed = 0
        for char in djtext:
            if char.isalpha():
                analyzed=analyzed+1
        params = {'purpose': 'Total Chars', 'analyzed_text': analyzed}

    if(removepunc !="on" and newlineremover !="on" and fullcaps !="on" and spaceremover !="on" and charcount !="on"):
        return HttpResponse("Please select any operation")
        #return render(request, 'analyze.html', params)

    return render(request, 'analyze.html', params)
'''def capfirst(request):
    return HttpResponse("capitalize first")
def newlineremove(request):
    return HttpResponse("newline")
def spaceremove(request):
    return HttpResponse("space remover <a href='/'>back</a>")
def charcount(request):
    return HttpResponse("char count")'''


