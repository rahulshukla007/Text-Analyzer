#this view file created by own
from django.http import HttpResponse
from django.shortcuts import render


# def index(request):
#     with open("/home/rashi/Desktop/mysite/mysite/one.txt") as f:
#         a = f.read()
#         return HttpResponse(a)


# # view file code
# from django.http import HttpResponse
# def index(request):
#     sites = [ '''<h1>For Entertainment </h1><a href = "https://www.youtube.com" >youtube video</a>''',
#               '''<h1>For Interaction </h1><a href = "https://www.facebook.com" >Facebook</a>''',
#               '''<h1>For Insight   </h1><a href = "https://www.ted.com/talks" >Ted Talk</a>''',
#              '''<h1>For Internship   </h1><a href="https://internshala.com" >Intenship</a>''',
#               '''<a  href = "http://127.0.0.1:8000/removepunc" >Back button </a>'''
#              ]
#     return HttpResponse((sites))
# #<a href="http://google.com" class="button">Go to Google</a>
#
#
# def About(request):
#     return HttpResponse('''<a  href = "https://www.youtube.com" >Back button </a>''')

# def index(request):
#     return render(request,'index.html')
#
# def removepunc(request):
#     #get the text
#     djtext = request.GET.get('text','default')
#     print(djtext)
#     #analyzise the text
#     return HttpResponse("remove punc")
#
# def capatlizefirst(request):
#     return HttpResponse("capatlize first")
#
# def newlineremove(request):
#     return HttpResponse("newline remove<a href='/'> back </a>")
#
# def spaceremove(request):
#     return HttpResponse("space remove")
#
# def charcount(request):
#     return HttpResponse("charcount")



djtext = "we are going"

#analyzed = ""
for index,char in enumerate(djtext):
    print(index,char)
#    if not (djtext[index]== " " and djtext[index+1]== " "):
 #       analyzed = analyzed + char

#print(analyzed)