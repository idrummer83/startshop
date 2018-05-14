from django.shortcuts import render





def createAccount(request):
    if request.method == 'POST':
        name = request.GET['name']
        email = request.GET['email']
        password = request.GET['password']
        name.save()
        email.save()
        password.save()
        return render(request, '/')