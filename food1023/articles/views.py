from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .scrapers import Pixnet 


def index(request):# urls.py 會呼叫 index方法

    pixnet = Pixnet(None) # 建立類別的實體

    if request.method == "POST":# 如果是以 POST 方式才處理
        pixnet = Pixnet(request.POST.get("restaurant_name"))  # 取得 scrapers.py 表單輸入資料

    context = {
        "articles": pixnet.get_articles() # 取得 get_articles 文章內容
    }

    return render(request, "articles/index.html", context) # 將資料傳遞給 articles/index.html 顯示樣版
