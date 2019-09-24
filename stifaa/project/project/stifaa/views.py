from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # from django.utils import translation
    # # user_language = 'en'
    # # translation.activate(user_language)
    # # request.session[translation.LANGUAGE_SESSION_KEY] = user_language
    # if  translation.LANGUAGE_SESSION_KEY in REQUEST.SESSION:
    #     del request.session[translation.LANGUAGE_SESSION_KEY]
    return render(request ,'index.html')


