from django.shortcuts import redirect

def handleRedirect(request):
    return redirect('posts:home')