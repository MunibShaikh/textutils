from django.http import HttpResponse
from django.shortcuts import render

# index function's
def index(request):
    return HttpResponse(render(request,'index.html'))


def analyze(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    removeline=request.POST.get('removeline','off')
    uppercase=request.POST.get('uppercase','off')
    spaceremover=request.POST.get('spaceremover','off')
    count=request.POST.get('count','off')


    # remove punctuations
    if removepunc=='on':
        punctuations = '''+=`!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyze=''
        for char in djtext:
            if not char in punctuations:
                analyze=analyze+char
        djtext=analyze
        params = {'analyzed': analyze}
        print(analyze)

    # remove lines
    analyze=''
    if removeline=='on':
        for char in djtext:
            if char!='\n' and char !='\r':
                analyze=analyze+char
        djtext=analyze
        params = {'analyzed': analyze}

    # UPPERCASE
    analyze=''
    if uppercase=='on':
        for char in djtext:
            cap=char.upper()
            analyze=analyze+cap
        djtext=analyze
        params = {'analyzed': analyze}

    # remove extra space
    if spaceremover=='on':
        analyze=''
        for index,char in enumerate(djtext):
            if not (djtext[index]==' ' and djtext[index+1]==' '):
                analyze=analyze+char
        djtext=analyze
        params = {'analyzed': analyze}
        print(analyze)

    # count words in text area
    if count=='on':
        analyze=len(djtext)
        params = {'analyzed': analyze}

    # return render(request, 'analyze.html',params)

    # if all close
    if removepunc != 'on' and removeline != 'on' and uppercase != 'on' and spaceremover != 'on' and count != 'on':
        analyze='sorry! you cant open swtich'
        params = {'analyzed': analyze}

    if len(djtext)<=0:
        analyze = 'sorry! enter somthing'
        params = {'analyzed': analyze}

    return render(request,'analyze.html',params)

def contactus(request):
    return render(request,'contactus.html')

def aboutus(request):
    return render(request,'aboutus.html')