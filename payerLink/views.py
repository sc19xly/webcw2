import json
from django.shortcuts import render
from django.shortcuts import HttpResponse  # 导入HttpResponse模块
from datetime import datetime
from payerLink.models import PayerLink
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
import json
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse

import requests
def list(request):
    res = PayerLink.objects.all()
    resList = [ {'id': p.id, 'link': p.link, 'name': p.name, 'username': p.username} for p in res ]
    content = {
        'success': True,
        'message': 'Search Success',
        'data': resList
    }
    return HttpResponse(content=json.dumps(content, ensure_ascii=False), content_type='application/json;charset=utf-8')

def info(request):
    id = request.GET.get('id')
    re = PayerLink.objects.get(id=id)
    newre = dict(id=re.id, link=re.link, name=re.name, username=re.username)
    content = {
        'success': True,
        'message': 'Search Success',
        'data': newre
    }
    return HttpResponse(content=json.dumps(content, ensure_ascii=False), content_type='application/json;charset=utf-8')

def delete(request):
    id = request.GET.get('id')
    PayerLink.objects.get(id=id).delete()
    content = {'success': True}
    return HttpResponse(content=json.dumps(content, ensure_ascii=False), content_type='application/json;charset=utf-8')

def save(request):
    jsonData = json.loads(request.body.decode())
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    payerLink=PayerLink()
    try:
        payerLink.link=jsonData['link']
    except Exception:
        print("link is null")
    try:
        payerLink.name=jsonData['name']
    except Exception:
        print("name is null")
    try:
        payerLink.username=jsonData['username']
    except Exception:
        print("username is null")
    payerLink.create_time=now
    payerLink.save()
    content = {
                    'success': True,
                    'message': 'Add Success',
                    'data':jsonData
                }
    return HttpResponse(content=json.dumps(content, ensure_ascii=False),
                            content_type='application/json;charset = utf-8')
def update (request):
    jsonData = json.loads(request.body.decode())
    re = PayerLink.objects.get(id=jsonData['id'])
    try:
        re.link=jsonData['link']
    except Exception:
        print("link is null")
    try:
        re.name=jsonData['name']
    except Exception:
        print("name is null")
    try:
        re.username=jsonData['username']
    except Exception:
        print("username is null")
    re.save()
    content = {
                    'success': True,
                    'message': 'Modify Success',
                    'data':jsonData
                }
    return HttpResponse(content=json.dumps(content, ensure_ascii=False),
                            content_type='application/json;charset = utf-8')


def page(request):
    data = json.loads(request.body.decode())
    pageNum = data.get('pageNum')
    pagesize = data.get('pageSize')
    search = data.get('search')

    queryset = PayerLink.objects.all()
    if search:
        queryset = queryset.filter(name__icontains=search)

    total = queryset.count()
    paginator = Paginator(queryset, pagesize)
    try:
        page = paginator.page(pageNum)
    except (PageNotAnInteger, EmptyPage):
        page = paginator.page(1)

    resList = []
    for obj in page:
        resList.append({
            'id': obj.id,
            'link': obj.link,
            'name': obj.name,
            'username': obj.username
        })

    content = {
        'success': True,
        'message': 'Search Success',
        'data': resList,
        'total': total
    }

    return JsonResponse(content, json_dumps_params={'ensure_ascii': False})
def pay(request):
    jsonData = json.loads(request.body.decode())
    name=jsonData['name']
    reserve2=jsonData['reserve2']
    payNum=jsonData['payNum']
    re=PayerLink.objects.get(username=reserve2)
    headers = {'content-type': 'application/json'}
    ress=requests.post(re.link+"/fund/pay",data=request.body,headers=headers)
    res1=json.loads(ress.text)
    print(res1)
    return HttpResponse(content=json.dumps(res1, ensure_ascii=False),
                            content_type='application/json;charset = utf-8')
def exitMoney(request):
    jsonData = json.loads(request.body.decode())
    name=jsonData['name']
    reserve2=jsonData['reserve2']
    payNum=jsonData['payNum']
    re=PayerLink.objects.get(username=reserve2)
    headers = {'content-type': 'application/json'}
    ress=requests.post(re.link+"/fund/exitMoney",data=request.body,headers=headers)
    res1=json.loads(ress.text)
    return HttpResponse(content=json.dumps(res1, ensure_ascii=False),
                            content_type='application/json;charset = utf-8')