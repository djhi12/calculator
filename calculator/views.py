from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    if request.method == 'POST':
        num1 = float(request.POST['num1'])
        num2 = float(request.POST['num2'])
        operation = request.POST['operation']
        if operation == 'add':
            return add(request, num1, num2)
        elif operation == 'subtract':
            return subtract(request, num1, num2)
        elif operation == 'multiply':
            return multiply(request, num1, num2)
        elif operation == 'divide':
            return divide(request, num1, num2)
    else:
        return render(request, 'home.html')


def add(request, num1, num2):
    result = num1 + num2
    return HttpResponse(f'The result of {num1} + {num2} is {result}')


def subtract(request, num1, num2):
    result = num1 - num2
    return HttpResponse(f'The result of {num1} - {num2} is {result}')


def multiply(request, num1, num2):
    result = num1 * num2
    return HttpResponse(f'The result of {num1} * {num2} is {result}')


def divide(request, num1, num2):
    if num2 == 0:
        return HttpResponse('Cannot divide by zero')
    result = num1 / num2
    return HttpResponse(f'The result of {num1} / {num2} is {result}')
