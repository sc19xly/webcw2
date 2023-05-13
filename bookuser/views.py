import json
from django.shortcuts import HttpResponse
from datetime import datetime
from bookuser.models import BookUser
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def list(request):
    books = BookUser.objects.all()
    book_list = [{'id': b.id, 'cusAccount': b.cusAccount, 'create_time': b.create_time, 'status': b.status, 'reserve1': b.reserve1, 'reserve2': b.reserve2, 'reserve3': b.reserve3, 'reserve4': b.reserve4, 'reserve5': b.reserve5, 'cusId': b.cusId, 'booBerth': b.booBerth, 'comCode': b.comCode, 'cusTelNumber': b.cusTelNumber, 'fliYfare': b.fliYfare} for b in books]
    content = {'success': True, 'message': 'Search Success', 'data': book_list}
    return HttpResponse(content=json.dumps(content, ensure_ascii=False), content_type='application/json;charset=utf-8')


def info(request):
    query_dict = request.GET
    id = query_dict.get('id')

    try:
        re = BookUser.objects.get(id=id)
    except BookUser.DoesNotExist:
        content = {
            'success': False,
            'message': 'No corresponding BookUser was found',
            'data': None
        }
        return HttpResponse(content=json.dumps(content, ensure_ascii=False),
                            content_type='application/json;charset=utf-8', status=404)

    newre = {
        'id': re.id,
        'cusAccount': re.cusAccount,
        'create_time': re.create_time,
        'status': re.status,
        'reserve1': re.reserve1,
        'reserve2': re.reserve2,
        'reserve3': re.reserve3,
        'reserve4': re.reserve4,
        'reserve5': re.reserve5,
        'cusId': re.cusId,
        'booBerth': re.booBerth,
        'comCode': re.comCode,
        'cusTelNumber': re.cusTelNumber,
        'fliYfare': re.fliYfare,
    }

    content = {
        'success': True,
        'message': 'Search Success',
        'data': newre
    }
    return HttpResponse(
        content=json.dumps(content, ensure_ascii=False),
        content_type='application/json;charset=utf-8'
    )


def delete(request):
    query_dict = request.GET
    id = query_dict.get('id')

    try:
        BookUser.objects.get(id=id).delete()
    except BookUser.DoesNotExist:
        content = {
            'success': False,
            'message': 'No corresponding BookUser was found',
        }
        return HttpResponse(content=json.dumps(content, ensure_ascii=False),
                            content_type='application/json;charset=utf-8', status=404)

    content = {
        'success': True,
        'message': 'Delete Success',
    }
    return HttpResponse(
        content=json.dumps(content, ensure_ascii=False),
        content_type='application/json;charset=utf-8'
    )


def save(request):
    jsonData = json.loads(request.body.decode())
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    bookUser=BookUser()
    try:
        bookUser.cusAccount=jsonData['cusAccount']
    except Exception:
        print("cusAccount is null")
    try:
        bookUser.status=jsonData['status']
    except Exception:
        print("status is null")
    try:
        bookUser.reserve1=jsonData['reserve1']
    except Exception:
        print("reserve1 is null")
    try:
        bookUser.reserve2=jsonData['reserve2']
    except Exception:
        print("reserve2 is null")
    try:
        bookUser.reserve3=jsonData['reserve3']
    except Exception:
        print("reserve3 is null")
    try:
        bookUser.reserve4=jsonData['reserve4']
    except Exception:
        print("reserve4 is null")
    try:
        bookUser.reserve5=jsonData['reserve5']
    except Exception:
        print("reserve5 is null")
    try:
        bookUser.cusId=jsonData['cusId']
    except Exception:
        print("cusId is null")
    try:
        bookUser.booBerth=jsonData['booBerth']
    except Exception:
        print("booBerth is null")
    try:
        bookUser.comCode=jsonData['comCode']
    except Exception:
        print("comCode is null")
    try:
        bookUser.cusTelNumber=jsonData['cusTelNumber']
    except Exception:
        print("cusTelNumber is null")
    try:
        bookUser.fliYfare=jsonData['fliYfare']
    except Exception:
        print("fliYfare is null")
    bookUser.create_time=now
    bookUser.save()
    content = {
                    'success': True,
                    'message': 'Add Success',
                    'data':jsonData
                }
    return HttpResponse(content=json.dumps(content, ensure_ascii=False),
                            content_type='application/json;charset = utf-8')
def update (request):
    jsonData = json.loads(request.body.decode())
    re = BookUser.objects.get(id=jsonData['id'])
    try:
        re.cusAccount=jsonData['cusAccount']
    except Exception:
        print("cusAccount is null")
    try:
        re.status=jsonData['status']
    except Exception:
        print("status is null")
    try:
        re.reserve1=jsonData['reserve1']
    except Exception:
        print("reserve1 is null")
    try:
        re.reserve2=jsonData['reserve2']
    except Exception:
        print("reserve2 is null")
    try:
        re.reserve3=jsonData['reserve3']
    except Exception:
        print("reserve3 is null")
    try:
        re.reserve4=jsonData['reserve4']
    except Exception:
        print("reserve4 is null")
    try:
        re.reserve5=jsonData['reserve5']
    except Exception:
        print("reserve5 is null")
    try:
        re.cusId=jsonData['cusId']
    except Exception:
        print("cusId is null")
    try:
        re.booBerth=jsonData['booBerth']
    except Exception:
        print("booBerth is null")
    try:
        re.comCode=jsonData['comCode']
    except Exception:
        print("comCode is null")
    try:
        re.cusTelNumber=jsonData['cusTelNumber']
    except Exception:
        print("cusTelNumber is null")
    try:
        re.fliYfare=jsonData['fliYfare']
    except Exception:
        print("fliYfare is null")
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
    pageNum = data['pageNum']
    pagesize = data['pageSize']
    search = data['search']
    res1=[]
    if search:
        res1=BookUser.objects.filter(name=search)
    else:
        res1=BookUser.objects.filter()
    total = res1.count()
    p = Paginator(res1, pagesize)
    page=[]
    try:
        page = p.page(pageNum)
    except PageNotAnInteger:
        page = p.page(pageNum)
    except EmptyPage:
        page = p.page(pageNum)
    resList=[]
    for p in page:
        college = {}
        college['id'] =p.id
        college['cusAccount'] =p.cusAccount
        college['create_time'] =p.create_time
        college['status'] =p.status
        college['reserve1'] =p.reserve1
        college['reserve2'] =p.reserve2
        college['reserve3'] =p.reserve3
        college['reserve4'] =p.reserve4
        college['reserve5'] =p.reserve5
        college['cusId'] =p.cusId
        college['booBerth'] =p.booBerth
        college['comCode'] =p.comCode
        college['cusTelNumber'] =p.cusTelNumber
        college['fliYfare'] =p.fliYfare
        resList.append(college)
    content = {
                    'success': True,
                    'message': 'Search Success',
                    'data':resList,
                    'total':total
                }
    return HttpResponse(content=json.dumps(content, ensure_ascii=False),
                            content_type='application/json;charset = utf-8')