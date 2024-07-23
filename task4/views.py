from django.shortcuts import render

# Create your views here.
def platform(request):
    return render(request, 'fourth_task/platform.html')

def games(request):
    list = ['Atomic Heart',
     'Cyberpunk 2075',
    'PayDay 2']
    context = {
        'list': list
    }
    return render(request, 'fourth_task/games.html', context)

def cart (request):

    return render(request, 'fourth_task/cart.html')