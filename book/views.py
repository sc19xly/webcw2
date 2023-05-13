import json
from django.shortcuts import render
from django.shortcuts import HttpResponse  # 导入HttpResponse模块
from datetime import datetime
from book.models import Book
from bookuser.models import BookUser
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage

def list(request):
    res = Book.objects.all()
    resList = []
    for p in res:
        college = {
            'id': p.id,
            'booAAddress': p.booAAddress,
            'create_time': p.create_time,
            'status': p.status,
            'reserve1': p.reserve1,
            'reserve2': p.reserve2,
            'reserve3': p.reserve3,
            'reserve4': p.reserve4,
            'reserve5': p.reserve5,
            'booAtime': p.booAtime,
            'Column1': p.Column1,
            'booFare': p.booFare,
            'booNo': p.booNo,
            'booNumber': p.booNumber,
            'booOrderNum': p.booOrderNum,
            'booTime': p.booTime,
            'boobAddress': p.boobAddress,
            'boobTime': p.boobTime,
            'comCode': p.comCode,
            'cusTelNumber': p.cusTelNumber,
            'flag': p.flag,
            'flagPay': p.flagPay,
        }
        resList.append(college)
    content = {
        'success': True,
        'message': 'Search SUccess',
        'data': resList,
    }
    return HttpResponse(
        content=json.dumps(content, ensure_ascii=False),
        content_type='application/json;charset=utf-8'
    )


def info(request):
    query_dict = request.GET
    book_id = query_dict.get('id')

    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        content = {
            'success': False,
            'message': 'No corresponding order was found',
            'data': None
        }
        return HttpResponse(content=json.dumps(content, ensure_ascii=False),
                            content_type='application/json;charset=utf-8', status=404)

    newre = {
        'id': book.id,
        'booAAddress': book.booAAddress,
        'create_time': book.create_time,
        'status': book.status,
        'reserve1': book.reserve1,
        'reserve2': book.reserve2,
        'reserve3': book.reserve3,
        'reserve4': book.reserve4,
        'reserve5': book.reserve5,
        'booAtime': book.booAtime,
        'Column1': book.Column1,
        'booFare': book.booFare,
        'booNo': book.booNo,
        'booNumber': book.booNumber,
        'booOrderNum': book.booOrderNum,
        'booTime': book.booTime,
        'boobAddress': book.boobAddress,
        'boobTime': book.boobTime,
        'comCode': book.comCode,
        'cusTelNumber': book.cusTelNumber,
        'flag': book.flag,
        'flagPay': book.flagPay,
    }

    book_users = BookUser.objects.filter(reserve1=book_id)
    resList = []
    for book_user in book_users:
        college = {
            'cusTelNumber': book_user.cusTelNumber,
            'cusId': book_user.cusId,
            'booBerth': book_user.booBerth,
            'fliYfare': book_user.fliYfare,
            'comCode': book_user.comCode,
            'cusAccount': book_user.cusAccount,
        }
        resList.append(college)

    newre['persions'] = resList

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
    book_id = query_dict.get('id')

    try:
        book = Book.objects.get(id=book_id)
        book.delete()
    except Book.DoesNotExist:
        content = {
            'success': False,
            'message': 'No corresponding order was found',
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
    book = Book()

    try:
        book.booAAddress = jsonData['booAAddress']
    except KeyError:
        pass

    try:
        book.status = jsonData['status']
    except KeyError:
        pass

    try:
        book.reserve1 = jsonData['reserve1']
    except KeyError:
        pass

    try:
        book.reserve2 = jsonData['reserve2']
    except KeyError:
        pass

    try:
        book.reserve3 = jsonData['reserve3']
    except KeyError:
        pass

    try:
        book.reserve4 = jsonData['reserve4']
    except KeyError:
        pass

    try:
        book.reserve5 = jsonData['reserve5']
    except KeyError:
        pass

    try:
        book.booAtime = jsonData['booAtime']
    except KeyError:
        pass

    try:
        book.Column1 = jsonData['Column1']
    except KeyError:
        pass

    try:
        book.booFare = jsonData['booFare']
    except KeyError:
        pass

    try:
        book.booNo = jsonData['booNo']
    except KeyError:
        pass

    try:
        book.booNumber = jsonData['booNumber']
    except KeyError:
        pass

    try:
        book.booOrderNum = jsonData['booOrderNum']
    except KeyError:
        pass

    try:
        book.booTime = jsonData['booTime']
    except KeyError:
        pass

    try:
        book.boobAddress = jsonData['boobAddress']
    except KeyError:
        pass

    try:
        book.boobTime = jsonData['boobTime']
    except KeyError:
        pass

    try:
        book.comCode = jsonData['comCode']
    except KeyError:
        pass

    try:
        book.cusTelNumber = jsonData['cusTelNumber']
    except KeyError:
        pass

    try:
        book.flag = jsonData['flag']
    except KeyError:
        pass

    try:
        book.flagPay = jsonData['flagPay']
    except KeyError:
        pass

    book.create_time = now
    book.save()

    persons = jsonData.get('persions', [])
    for per in persons:
        book_user = BookUser()
        book_user.cusAccount = per.get('cusAccount')
        book_user.cusId = per.get('cusId')
        book_user.booBerth = per.get('booBerth')
        book_user.comCode = per.get('comCode')
        book_user.fliYfare = per.get('fliYfare')
        book_user.cusTelNumber = per.get('cusTelNumber')
        book_user.reserve1 = book.id
        book_user.save()

    content = {
        'success': True,
        'message': 'Add Success',
        'data': jsonData
    }
    return HttpResponse(
        content=json.dumps(content, ensure_ascii=False),
        content_type='application/json;charset=utf-8'
    )

def update(request):
    jsonData = json.loads(request.body.decode())
    book_id = jsonData.get('id')
    if not book_id:
        content = {
            'success': False,
            'message': 'lack of parameters'
        }
        return HttpResponse(
            content=json.dumps(content, ensure_ascii=False),
            content_type='application/json;charset=utf-8',
            status=400
        )

    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        content = {
            'success': False,
            'message': 'No corresponding order was found',
        }
        return HttpResponse(
            content=json.dumps(content, ensure_ascii=False),
            content_type='application/json;charset=utf-8',
            status=404
        )

    try:
        book.booAAddress = jsonData['booAAddress']
    except KeyError:
        pass

    try:
        book.status = jsonData['status']
    except KeyError:
        pass

    try:
        book.reserve1 = jsonData['reserve1']
    except KeyError:
        pass

    try:
        book.reserve2 = jsonData['reserve2']
    except KeyError:
        pass

    try:
        book.reserve3 = jsonData['reserve3']
    except KeyError:
        pass

    try:
        book.reserve4 = jsonData['reserve4']
    except KeyError:
        pass

    try:
        book.reserve5 = jsonData['reserve5']
    except KeyError:
        pass

    try:
        book.booAtime = jsonData['booAtime']
    except KeyError:
        pass

    try:
        book.Column1 = jsonData['Column1']
    except KeyError:
        pass

    try:
        book.booFare = jsonData['booFare']
    except KeyError:
        pass

    try:
        book.booNo = jsonData['booNo']
    except KeyError:
        pass

    try:
        book.booNumber = jsonData['booNumber']
    except KeyError:
        pass

    try:
        book.booOrderNum = jsonData['booOrderNum']
    except KeyError:
        pass

    try:
        book.booTime = jsonData['booTime']
    except KeyError:
        pass

    try:
        book.boobAddress = jsonData['boobAddress']
    except KeyError:
        pass

    try:
        book.boobTime = jsonData['boobTime']
    except KeyError:
        pass

    try:
        book.comCode = jsonData['comCode']
    except KeyError:
        pass

    try:
        book.cusTelNumber = jsonData['cusTelNumber']
    except KeyError:
        pass

    try:
        book.flag = jsonData['flag']
    except KeyError:
        pass

    try:
        book.flagPay = jsonData['flagPay']
    except KeyError:
        pass

    book.save()

    content = {
        'success': True,
        'message': 'Modify Success',
        'data': jsonData
    }
    return HttpResponse(
        content=json.dumps(content, ensure_ascii=False),
        content_type='application/json;charset=utf-8'
    )

def page(request):
    data = json.loads(request.body.decode())
    pageNum = data['pageNum']
    pagesize = data['pageSize']
    search = data['search']
    air = data['air']
    res1=[]
    if search:
        res1=Book.objects.filter(reserve1=search)
    elif air:
         res1=Book.objects.filter(reserve4=air)
    else:
        res1=Book.objects.filter()
        #Pagination
    total = res1.count()
    p = Paginator(res1, pagesize) # Show 10 contacts per page.
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
        college['booAAddress'] =p.booAAddress
        college['create_time'] =p.create_time
        college['status'] =p.status
        college['reserve1'] =p.reserve1
        college['reserve2'] =p.reserve2
        college['reserve3'] =p.reserve3
        college['reserve4'] =p.reserve4
        college['reserve5'] =p.reserve5
        college['booAtime'] =p.booAtime
        college['Column1'] =p.Column1
        college['booFare'] =p.booFare
        college['booNo'] =p.booNo
        college['booNumber'] =p.booNumber
        college['booOrderNum'] =p.booOrderNum
        college['booTime'] =p.booTime
        college['boobAddress'] =p.boobAddress
        college['boobTime'] =p.boobTime
        college['comCode'] =p.comCode
        college['cusTelNumber'] =p.cusTelNumber
        college['flag'] =p.flag
        college['flagPay'] =p.flagPay
        resList.append(college)        
    content = {
                    'success': True,
                    'message': 'Search Success',
                    'data':resList,
                    'total':total
                }
    return HttpResponse(content=json.dumps(content, ensure_ascii=False),
                            content_type='application/json;charset = utf-8')