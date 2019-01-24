from django.shortcuts import render
import random

# Create your views here.
def index(request):
    return render(request, 'index.html')

# Template variable    
def dinner(request):
    menu = ["족발", "햄버거", "치킨", "초밥"]
    pick = random.choice(menu)
    return render(request, 'dinner.html', {'dinner': pick})
    
# Variable routing
def hello(request, name):
    return render(request, 'hello.html', {'name': name})
    
def burger(request):
    name = ["맘터", "롯데리아", "버걸킹", "맥도날드", "케에프씨"]
    pick = random.choice(name)
    return render(request, 'burger.html', {'burger': pick})
    
def id(request, num):
    return render(request, 'id.html', {'n': num})
    
def smile(request):
    happy = ["하하하", "히히히", "헤헤헤", "호호호"]
    pick = random.choice(happy)
    return render(request, 'smile.html', {'smile': pick})
    
def say(request, name):
    return render(request, 'say.html', {'say': name})
    
def coffee(request):
    menu = ["아아", "뜨아", "라떼", "카페모카", "카마"]
    pick = random.choice(menu)
    return render(request, 'coffee.html', {'coffee': pick})
    
# Form tag
def throw(request):
    return render(request, 'throw.html')
    
def catch(request):
    message = request.GET.get('message')
    return render(request, 'catch.html', {'message': message})
    
# Form 외부로 요청
def naver(request):
    return render(request, 'naver.html')
    
# Bootstrap
def bootstrap(request):
    return render(request, 'bootstrap.html')
