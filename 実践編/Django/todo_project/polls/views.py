# from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    		return HttpResponse("Hello, world!")
def home(request):
    		return render(request, 'polls/home.html')
def mypage(request):
    		return render(request, 'polls/mypage.html')
def home(request):
    # 辞書データを用意し渡す
    data = {
        'name':"suzuki taro",
        'address':'Tokyo'
        }
    return render(request, 'polls/home.html', data)

# polls/formで呼び出される関数
def form(request):
    return render(request, 'polls/form.html')

# polls/confirmformで呼び出される関数
def confirmform(request):
    # form method='POST'で送信されたデータを取得
    message = request.POST['message']
    data = {'message':message}
    return render(request, 'polls/confirmform.html', data)
