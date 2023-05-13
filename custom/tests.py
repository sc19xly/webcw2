import self
from django.test import TestCase, Client
from django.urls import reverse

from custom.models import Custom
from datetime import datetime
import json

class CustomTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.custom = Custom.objects.create(
            cusAccount="test_account",
            create_time=datetime.now().strftime('2022-01-01 12:00:00'),
            status="active",
            reserve1="reserve1",
            reserve2="reserve2",
            reserve3="reserve3",
            reserve4="reserve4",
            reserve5="reserve5",
            cusEmail="test_email@test.com",
            cusId="test_id",
            cusName="Test User",
            cusNames="Test User Name",
            cusPwd="test_password",
            cusSex="Male",
            cusTelNumber="1234567890",
            seccode="abcd"
        )

    def test_list_customs(self):
        response = self.client.get('/custom/list')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {
                "success": True,
                "message": "Search Success",
                "data": [{
                    "id": 1,
                    "cusAccount": "test_account",
                    "create_time": self.custom.create_time,
                    "status": "active",
                    "reserve1": "reserve1",
                    "reserve2": "reserve2",
                    "reserve3": "reserve3",
                    "reserve4": "reserve4",
                    "reserve5": "reserve5",
                    "cusEmail": "test_email@test.com",
                    "cusId": "test_id",
                    "cusName": "Test User",
                    "cusNames": "Test User Name",
                    "cusPwd": "test_password",
                    "cusSex": "Male",
                    "cusTelNumber": "1234567890",
                    "seccode": "abcd"
                }]
            }
        )

    def test_get_custom_by_id(self):
        response = self.client.get('/custom/info?id=1')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {
                "success": True,
                "message": "Search Success",
                "data": {
                    "id": 1,
                    "cusAccount": "test_account",
                    "create_time": self.custom.create_time,
                    "status": "active",
                    "reserve1": "reserve1",
                    "reserve2": "reserve2",
                    "reserve3": "reserve3",
                    "reserve4": "reserve4",
                    "reserve5": "reserve5",
                    "cusEmail": "test_email@test.com",
                    "cusId": "test_id",
                    "cusName": "Test User",
                    "cusNames": "Test User Name",
                    "cusPwd": "test_password",
                    "cusSex": "Male",
                    "cusTelNumber": "1234567890",
                    "seccode": "abcd"
                }
            }
        )

    def test_delete_custom_by_id(self):
        response = self.client.get('/custom/delete?id=1')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {
                "success": True,
                "message": "Delete Success"
            }
        )

    def test_save_custom(self):
        data = {
            "cusAccount": "new_test_account",
            "status": "inactive",
            "reserve1": "new_reserve1",
            "reserve2": "new_reserve2",
            "reserve3": "new_reserve3",
            "reserve4": "new_reserve4",
            "reserve5": "new_reserve5",
            "cusEmail": "new_test_email@test.com",
            "cusId": "new_test_id",
            "cusName": "New Test User",
            "cusNames": "New Test User Name",
            "cusPwd": "new_test_password",
            "cusSex": "Female",
            "cusTelNumber": "0987654321",
            "seccode": "efgh"
        }
        response = self.client.post('/custom/save', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {
                "success": True,
                "message": "Add Success",
                "data": data
            }
        )

    def test_update_custom(self):
        data = {
            "id": 1,
            "cusAccount": "updated_test_account",
            "status": "inactive",
            "reserve1": "updated_reserve1",
            "reserve2": "updated_reserve2",
            "reserve3": "updated_reserve3",
            "reserve4": "updated_reserve4",
            "reserve5": "updated_reserve5",
            "cusEmail": "updated_test_email@test.com",
            "cusId": "updated_test_id",
            "cusName": "Updated Test User",
            "cusNames": "Updated Test User Name",
            "cusPwd": "updated_test_password",
            "cusSex": "Female",
            "cusTelNumber": "0987654321",
            "seccode": "ijkl"
            }
        response = self.client.post('/custom/update', json.dumps(data), content_type='application/json')
        self.assertEqual.__self__.maxDiff = None
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {
                "success": True,
                "message": "Modify Success",
                "data": data
            }
        )

    def test_page(self):
        Custom.objects.create(
            cusAccount='test_account',
            status='active',
            reserve1='reserve1',
            reserve2='reserve2',
            reserve3='reserve3',
            reserve4='reserve4',
            reserve5='reserve5',
            cusEmail='test@example.com',
            cusId='1',
            cusName='Test User',
            cusNames='Test',
            cusPwd='password',
            cusSex='male',
            cusTelNumber='1234567890',
            seccode='1234'
        )
        data = {
            'pageNum': 1,
            'pageSize': 10,
            'search': ''
        }
        response = self.client.post(reverse('pag'), data=data, content_type='application/json')

        self.assertEqual(response.status_code, 200)
        content = response.json()
        self.assertTrue(content['success'])
        self.assertEqual(content['message'], 'Search Success')
        self.assertEqual(content['total'], 0)
        data = content['data']
        self.assertEqual(len(data), 0)