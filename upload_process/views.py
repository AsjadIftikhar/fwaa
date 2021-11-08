from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage


# Imaginary function to handle an uploaded file.
# from somewhere import handle_uploaded_file

def homePage(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['sentFile']  # here you get the files needed
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
    context = {}
    return render(request, 'home.html', context)
