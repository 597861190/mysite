from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.


def login(request):
    if request.method == 'GET':
        render(request, "login.html")
    user = request.POST.get('user')
    print(user)
    passwd = request.POST.get('pwd')
    print(passwd)
    if user == 'admin' and passwd == '123':
        # return HttpResponse('登陆成功')
        return redirect("https://zhuanlan.zhihu.com/p/653737243")
    return render(request, 'login.html')
