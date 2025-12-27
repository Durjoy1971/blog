from django.shortcuts import redirect

def handleRedirect(request):
    return redirect('post_list')