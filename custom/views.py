import json
from django.shortcuts import get_object_or_404
from django.shortcuts import HttpResponse
from datetime import datetime
from custom.models import Custom
from django.core.paginator import Paginator,  EmptyPage, InvalidPage
from django.forms.models import model_to_dict
from django.http import JsonResponse


def list(request):
    colleges = Custom.objects.all()
    resList = []
    for college in colleges:
        college_dict = {
            'id': college.id,
            'cusAccount': college.cusAccount,
            'create_time': college.create_time,
            'status': college.status,
            'reserve1': college.reserve1,
            'reserve2': college.reserve2,
            'reserve3': college.reserve3,
            'reserve4': college.reserve4,
            'reserve5': college.reserve5,
            'cusEmail': college.cusEmail,
            'cusId': college.cusId,
            'cusName': college.cusName,
            'cusNames': college.cusNames,
            'cusPwd': college.cusPwd,
            'cusSex': college.cusSex,
            'cusTelNumber': college.cusTelNumber,
            'seccode': college.seccode,
        }
        resList.append(college_dict)

    content = {
        'success': True,
        'message': 'Search Success',
        'data': resList
    }

    return JsonResponse(content, json_dumps_params={'ensure_ascii': False})


def info(request):
    id = request.GET.get('id')
    re = get_object_or_404(Custom, id=id)
    newre = re.__dict__.copy()
    del newre['_state']
    content = {'success': True, 'message': 'Search Success', 'data': newre}
    return HttpResponse(content=json.dumps(content, ensure_ascii=False), content_type='application/json;charset=utf-8')
def delete(request):
    id = request.GET.get('id')
    re = get_object_or_404(Custom, id=id).delete()
    content = {'success': True, 'message': 'Delete Success'}
    return HttpResponse(content=json.dumps(content, ensure_ascii=False), content_type='application/json;charset=utf-8')

def save(request):
    data = json.loads(request.body.decode())
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    custom = Custom(create_time=now, **{k: v for k, v in data.items() if k != 'id'})
    custom.save()
    content = {'success': True, 'message': 'Add Success', 'data': data}
    return HttpResponse(content=json.dumps(content, ensure_ascii=False), content_type='application/json;charset=utf-8')

def update(request):
    data = json.loads(request.body.decode())
    custom = Custom.objects.get(id=data['id'])
    fields = ['cusAccount', 'status', 'reserve1', 'reserve2', 'reserve3', 'reserve4', 'reserve5', 'cusEmail', 'cusId', 'cusName', 'cusNames', 'cusPwd', 'cusSex', 'cusTelNumber', 'seccode']
    for field in fields:
        if field in data:
            setattr(custom, field, data[field])
    custom.save()
    content = {'success': True, 'message': 'Modify Success', 'data': data}
    return HttpResponse(content=json.dumps(content, ensure_ascii=False), content_type='application/json;charset=utf-8')


def page(request):
    data = json.loads(request.body.decode())
    pageNum = data['pageNum']
    pageSize = data['pageSize']
    search = data['search']

    customs = Custom.objects.all()
    if search:
        customs_filtered = customs.filter(name=search)
    else:
        customs_filtered = customs

    paginator = Paginator(customs_filtered, pageSize)
    try:
        page = paginator.page(pageNum)
    except (EmptyPage, InvalidPage):
        page = paginator.page(1)

    results = []
    for custom in page.object_list:
        custom_dict = model_to_dict(custom)
        results.append(custom_dict)

    response_data = {
        'success': True,
        'message': 'Search Success',
        'data': results,
        'total': customs_filtered.count(),
    }

    return JsonResponse(response_data, json_dumps_params={'ensure_ascii': False})
def login(request):
    jsonData = json.loads(request.body.decode())
    res1=Custom.objects.filter(cusAccount=jsonData['cusAccount']).all()
    content={}
    if  len(res1)>0:
        res2=Custom.objects.filter(cusAccount=jsonData['cusAccount'],cusPwd=jsonData['cusPwd'])
        res3={
            "username":res1[0].cusAccount,
             "name":res1[0].cusName,
             "payPwd":  res1[0].reserve1


        }
        if len(res2)>0:
            content = {
                    'success': True,
                    'message': 'Log In Success',
                    'data':res3
                }
        else:
            content = {
                    'success': False,
                    'message': 'Wrong Password'
                }
    else:
        content = {
                    'success': False,
                    'message': 'The user does not exist.'
                }
    return HttpResponse(content=json.dumps(content, ensure_ascii=False),
                            content_type='application/json;charset = utf-8')