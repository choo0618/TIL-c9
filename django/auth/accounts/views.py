from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

def signup(request):
    # 로그인이 되어있을때 post 로 이동
    if request.user.is_authenticated:
        return redirect('posts:list')
        
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():  # 검증
            user = form.save()
            auth_login(request, user)   # 회원가입 후 바로 로그인
            return redirect('posts:list')
    else:
        form = UserCreationForm()
    
    return render(request, 'signup.html', {'form': form})
    
def login(request):
    # 로그인이 되어있을때 post 로 이동
    if request.user.is_authenticated:
        return redirect('posts:list')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'posts:list')
    else:
        form = AuthenticationForm()
    
     # => /posts/new/
    return render(request, 'login.html', {'form': form})
    
def logout(request):
    auth_logout(request)
    return redirect('posts:list')