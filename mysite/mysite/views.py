#this view file created by own
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):

    djtext          = request.POST.get('text','default')
    removepunc      = request.POST.get('removepunc','off')
    uppercase       = request.POST.get('uppercase', 'off')
    newlinermv      = request.POST.get('newlineremove', 'off')
    Extraspacermv   = request.POST.get('Extrapaceremover', 'off')
    charcount       = request.POST.get('charcounter', 'off')


    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {"purpose": "Removed Punctations", "analyzed_text": analyzed}
        djtext = analyzed

    if uppercase == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {"purpose":"Upper case text","analyzed_text":analyzed}
        djtext = analyzed

    if newlinermv == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

        params = {"purpose":"New Line Remove text","analyzed_text":analyzed}
        djtext = analyzed

    if Extraspacermv == "on":
        analyzed = ""
        for index,char in enumerate(djtext):
            if not (djtext[index]==" " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {"purpose":"Extra space Remove text","analyzed_text":analyzed}
        djtext = analyzed


    if charcount == "on":
        #analyzed = len(djtext)
        count = 0
        for i in djtext:
            count = count + 1
        params = {"purpose":"Character count of text","analyzed_text":count}

    if removepunc != "on" and uppercase != "on" and newlinermv != "on" and Extraspacermv != "on" and charcount !="on":
        return HttpResponse("Please select any operation")


    return render(request,'analyze.html',params)



