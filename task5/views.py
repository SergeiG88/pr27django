from django.shortcuts import render
from .forms import UserRegister


users = ["existing_user1", "existing_user2"]


def handle_registration(form):
    username = form.cleaned_data['username']
    password = form.cleaned_data['password']
    repeat_password = form.cleaned_data['repeat_password']
    age = form.cleaned_data['age']

    if password != repeat_password:
        return {'error': "Пароли не совпадают", 'form': form}
    elif age < 18:
        return {'error': "Вы должны быть старше 18", 'form': form}
    elif username in users:
        return {'error': "Пользователь уже существует", 'form': form}
    else:
        users.append(username)
        return {'message': f"Приветствуем, {username}!", 'form': UserRegister()}


def sign_up_by_django(request):
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            result = handle_registration(form)
            return render(request, 'fifth_task/registration_page.html', result)
    else:
        form = UserRegister()


    return render(request, 'fifth_task/registration_page.html', {'form': form})


def sign_up_by_html(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')


        try:
            age = int(age)
        except ValueError:
            age = None

        if password != repeat_password:
            info = {'error': "Пароли не совпадают", 'form': UserRegister(request.POST)}
        elif age is None or age < 18:
            info = {'error': "Вы должны быть старше 18", 'form': UserRegister(request.POST)}
        elif username in users:
            info = {'error': "Пользователь уже существует", 'form': UserRegister(request.POST)}
        else:
            users.append(username)
            info = {'message': f"Приветствуем, {username}!", 'form': UserRegister()}

        return render(request, 'fifth_task/registration_page.html', info)

    return render(request, 'fifth_task/registration_page.html', {'form': UserRegister()})

