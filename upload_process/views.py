from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm


# Imaginary function to handle an uploaded file.
# from somewhere import handle_uploaded_file

def homePage(request):
    if request.method == 'POST':
        f = request.FILES['sentFile']  # here you get the files needed
        print(f.name)
    #     form = UploadFileForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         print(request.FILES['file'])
    #         # return HttpResponseRedirect('/success/url/')
    #     else:
    #         print(request.FILES['file'])
    #         print("Wrong")
    # else:
    #     form = UploadFileForm()
    context = {}
    return render(request, 'home.html', context)
