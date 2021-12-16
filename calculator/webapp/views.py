from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index_view(request):
    if request.method == 'GET':
        return render(request, "index.html")

    else:
        try:
            n1 = int(request.POST.get('first_num'))
            n2 = int(request.POST.get('second_num'))
        except ValueError:
            return HttpResponse("It is need to input numbers")
        r = request.POST.get('operation')
        if r == 'multiply':
            s = '*'
            a = n1 * n2
        elif r == 'divide':
            s = '/'
            a = n1/n2
        elif r == 'subtract':
            s = '-'
            a = n1 - n2
        elif r == 'add':
            s = '+'
            a = n1 + n2
        else:
            return HttpResponse('It is need to choose operation')
            # s = '-+*/?'
            # a = 'mistake'

        context = {
            'first_num': n1,
            'second_num': n2,
            'sign': s,
            'result': a,
        }
        return render(request, "answer.html", context)
