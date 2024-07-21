from django.shortcuts import render

# Create your views here.
def platform(request):
    return render(request, 'third_task/platform.html')

def games(request):
    t1 = 'Atomic Heart'
    t2 = 'Cyberpunk 2075'
    t3 = 'PayDay 2'
    context = {
        't1': t1,
        't2': t2,
        't3': t3,
    }
    return render(request, 'third_task/games.html', context)

def cart (request):

    return render(request, 'third_task/cart.html')