import json
from django.shortcuts import HttpResponse
from datetime import datetime
from airLink.models import AirLink
import requests
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
airapis=["http://101.43.132.23:8001"]
def list(request):
    links = AirLink.objects.all()
    res_list = []

    for link in links:
        res_list.append({
            'id': link.id,
            'link': link.link,
            'name': link.name,
            'username': link.username
        })

    content = {
        'success': True,
        'message': 'Search Success',
        'data': res_list
    }
    return HttpResponse(
        content=json.dumps(content, ensure_ascii=False),
        content_type='application/json;charset=utf-8'
    )

def info(request):
    id = request.GET.get('id')
    try:
        link = AirLink.objects.get(id=id)
    except AirLink.DoesNotExist:
        content = {
            'success': False,
            'message': 'No corresponding Airlink was found'
        }
        return HttpResponse(
            content=json.dumps(content, ensure_ascii=False),
            content_type='application/json;charset=utf-8',
            status=404
        )

    data = {
        'id': link.id,
        'link': link.link,
        'name': link.name,
        'username': link.username
    }

    content = {
        'success': True,
        'message': 'Search Success',
        'data': data
    }
    return HttpResponse(
        content=json.dumps(content, ensure_ascii=False),
        content_type='application/json;charset=utf-8'
    )

def delete(request):
    link_id = request.GET.get('id')
    try:
        link = AirLink.objects.get(id=link_id)
    except AirLink.DoesNotExist:
        content = {
            'success': False,
            'message': 'No corresponding Airlink was found'
        }
        return HttpResponse(
            content=json.dumps(content, ensure_ascii=False),
            content_type='application/json;charset=utf-8',
            status=404
        )

    link.delete()

    content = {
        'success': True,
        'message': '删除成功'
    }
    return HttpResponse(
        content=json.dumps(content, ensure_ascii=False),
        content_type='application/json;charset=utf-8'
    )


def save(request):
    jsonData = json.loads(request.body.decode())
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    airLink=AirLink()
    try:
        airLink.link=jsonData['link']
    except Exception:
        print("link is null")
    try:
        airLink.name=jsonData['name']
    except Exception:
        print("name is null")
    try:
        airLink.username=jsonData['username']
    except Exception:
        print("username is null")
    airLink.create_time=now
    airLink.save()
    content = {
                    'success': True,
                    'message': 'Add Success',
                    'data':jsonData
                }
    return HttpResponse(content=json.dumps(content, ensure_ascii=False),
                            content_type='application/json;charset = utf-8')
def update(request):
    json_data = json.loads(request.body.decode())
    link_id = json_data.get('id')

    try:
        air_link = AirLink.objects.get(id=link_id)
    except AirLink.DoesNotExist:
        content = {
            'success': False,
            'message': 'No corresponding Airlink was found',
        }
        return HttpResponse(
            content=json.dumps(content, ensure_ascii=False),
            content_type='application/json;charset=utf-8',
            status=404
        )

    link = json_data.get('link')
    name = json_data.get('name')
    username = json_data.get('username')

    if any([link is not None, name is not None, username is not None]):
        if link is not None:
            air_link.link = link
        if name is not None:
            air_link.name = name
        if username is not None:
            air_link.username = username

        air_link.save()

    data = {
        'id': air_link.id,
        'link': air_link.link,
        'name': air_link.name,
        'username': air_link.username
    }

    content = {
        'success': True,
        'message': 'Modify Success',
        'data': data
    }
    return HttpResponse(
        content=json.dumps(content, ensure_ascii=False),
        content_type='application/json;charset=utf-8'
    )

def page(request):
    data = json.loads(request.body.decode())
    page_num = data.get('pageNum', 1)
    page_size = data.get('pageSize', 10)
    search = data.get('search')

    if search:
        links = AirLink.objects.filter(name=search)
    else:
        links = AirLink.objects.all()


    total = links.count()
    paginator = Paginator(links, page_size)

    try:
        page = paginator.page(page_num)
    except (PageNotAnInteger, EmptyPage):
        page = paginator.page(1)

    res_list = [
        {
            'id': link.id,
            'link': link.link,
            'name': link.name,
            'username': link.username
        } for link in page.object_list
    ]

    content = {
        'success': True,
        'message': 'Search Success',
        'data': res_list,
        'total': total
    }
    return HttpResponse(
        content=json.dumps(content, ensure_ascii=False),
        content_type='application/json;charset=utf-8'
    )
def airList(request):
    data = json.loads(request.body.decode())
    pageNum = data['pageNum']
    pagesize = data['pageSize'] 
    result =requestAirApi("/flight/page1",request.body)
    return HttpResponse(content=json.dumps(result, ensure_ascii=False),
                            content_type='application/json;charset = utf-8')
def requestAirApi(url,data):
    res=AirLink.objects.filter().all()    
    list=[]
    for airapi in res:
        headers = {'content-type': 'application/json'}
        wb_data = requests.post(airapi.link+url,data=data,headers=headers)
        result = wb_data.json()
        list=list+result['data']
    return list

