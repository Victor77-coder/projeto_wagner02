from django.shortcuts import render
from django.contrib.auth import get_user_model


def criar_cliente(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = get_user_model()
        user_created = user.objects.create(
            email=email,
            username=username
        )

        user_created.set_password(password)

        user_created.save()

    return render(request, 'users/register.html')

