import json
from django.test import TestCase, RequestFactory
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from bookuser.models import BookUser
from django.urls import reverse
from django.shortcuts import HttpResponse
from bookuser.views import info

class BookUserListViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.book_user = BookUser.objects.create(
            cusAccount='test',
            create_time='2023-05-12',
            status='active',
            reserve1='reserve1',
            reserve2='reserve2',
            reserve3='reserve3',
            reserve4='reserve4',
            reserve5='reserve5',
            cusId='cusId',
            booBerth='booBerth',
            comCode='comCode',
            cusTelNumber='cusTelNumber',
            fliYfare='fliYfare'
        )

    def test_info_view(self):
        request = self.factory.get('/bookUser/info', {'id': 2})

        bookuser = BookUser.objects.create(
            id = 2,
            cusAccount='test',
            create_time='2023-05-12',
            status='active',
            reserve1='reserve1',
            reserve2='reserve2',
            reserve3='reserve3',
            reserve4='reserve4',
            reserve5='reserve5',
            cusId='cusId',
            booBerth='booBerth',
            comCode='comCode',
            cusTelNumber='cusTelNumber',
            fliYfare='fliYfare'
        )

        response = info(request)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertTrue(data['success'])
        self.assertEqual(data['message'], 'Search Success')
        new_re = data['data']
        self.assertEqual(new_re['id'], 2)
        self.assertEqual(new_re['cusAccount'], bookuser.cusAccount)
        self.assertEqual(new_re['create_time'], bookuser.create_time)
        self.assertEqual(new_re['status'], bookuser.status)
        self.assertEqual(new_re['reserve1'], bookuser.reserve1)
        self.assertEqual(new_re['reserve2'], bookuser.reserve2)
        self.assertEqual(new_re['reserve3'], bookuser.reserve3)
        self.assertEqual(new_re['reserve4'], bookuser.reserve4)
        self.assertEqual(new_re['reserve5'], bookuser.reserve5)
        self.assertEqual(new_re['cusId'], bookuser.cusId)
        self.assertEqual(new_re['booBerth'], bookuser.booBerth)
        self.assertEqual(new_re['comCode'], bookuser.comCode)
        self.assertEqual(new_re['cusTelNumber'], bookuser.cusTelNumber)
        self.assertEqual(new_re['fliYfare'], bookuser.fliYfare)

    def test_list_view(self):
        response = self.client.get('/bookUser/list', {'id': self.book_user.id})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertTrue(data['success'])
        self.assertEqual(len(data['data']), 1)



    def test_delete(self):
            response = self.client.get('/bookUser/delete', {'id': self.book_user.id})
            self.assertEqual(response.status_code, 200)
            content = json.loads(response.content)
            self.assertEqual(content['success'], True)

    def test_book_save(self):
            data = {
            'cusAccount':'test',
            'create_time':'2023-05-12',
            'booBerth':'booBerth',
            'comCode':'comCode',
            'cusTelNumber':'cusTelNumber',
            'fliYfare':'fliYfare'
            }
            response = self.client.post('/bookUser/save', data=json.dumps(data), content_type='application/json')
            self.assertEqual(response.status_code, 200)