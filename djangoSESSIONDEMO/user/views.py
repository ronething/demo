from django.shortcuts import render, redirect


# Create your views here.


def login(request):
    """登录函数"""
    if request.method == "POST":
        name = request.POST.get('name')
        request.session["is_login"] = True  # 在session中增加键值对
        request.session["user"] = name

        return redirect("/user/index")

    return render(request, "login.html")


def index(request):
    """主页面"""
    if request.session.get("is_login", None):
        name = request.session.get("user", None)
        return render(request, "index.html", dict(name=name))
    else:
        return redirect("/user/login")

def test(request):
    """test"""
    from django.http import JsonResponse
    res = dict(data=render(request,"test.html").content.decode())
    return JsonResponse(res)