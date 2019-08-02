from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'index.html')

def analyze(request):
    #Get the text
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','default')
    fullcaps = request.POST.get('fullcaps','default')
    newlineremover = request.POST.get('newlineremover','default')
    spaceremover = request.POST.get('spaceremover','default')
    # charcount = request.POST.get('charcount','default')
    # analyzed = djtext
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text':analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Change to uppercase', 'analyzed_text':analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose':'Removed New Lines', 'analyzed_text':analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if spaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed +char
        params = {'purpose': 'Space Remover', 'analyzed_text': analyzed}

    # if charcount == "on":
    #     analyzed =len(djtext)
    #     params = {'purpose': 'Character Counter', 'analyzed_text': analyzed}

    if (removepunc != "on" and fullcaps != "on" and newlineremover != "on" and spaceremover != "on"):
        return HttpResponse("Please select any of the choices!")

    return render(request, 'analyze.html', params)

    # else:
    #     return HttpResponse("Error")

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

# def capfirst(request):
#     return HttpResponse("capitalize first")
#
# def newlineremove(request):
#     return HttpResponse("newline remove")
#
# def spaceremove(request):
#     return HttpResponse("space remove")
#
# def charcount(request):
#     return HttpResponse("character count")
