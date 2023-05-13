from django.test import TestCase, Client
from book.models import Book
import json

class BookTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.book = Book.objects.create(
            id=1,
            booAAddress='address',
            create_time='2022-01-01 12:00:00',
            status='done',
            reserve1='reserve1',
            reserve2='reserve2',
            reserve3='reserve3',
            reserve4='reserve4',
            reserve5='reserve5',
            booAtime='2022-01-01 12:00:00',
            Column1='column1',
            booFare='fare',
            booNo='no',
            booNumber='number',
            booOrderNum='order',
            booTime='2022-01-01 12:00:00',
            boobAddress='baddress',
            boobTime='2022-01-01 12:00:00',
            comCode='code',
            cusTelNumber='tel',
            flag='flag',
            flagPay='pay'
        )

    def test_list(self):
        response = self.client.get('/book/list')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()['data']), 1)
        self.assertEqual(response.json()['data'][0]['booAAddress'], 'address')

    def test_info(self):
        response = self.client.get(f'/book/info?id={self.book.id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['data']['booAAddress'], 'address')

    def test_delete(self):
        response = self.client.get(f'/book/delete?id={self.book.id}')
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())

    def test_save(self):
        data = {
            'id':1,
            'booAAddress': 'new_address',
            'create_time': '2023-05-13 18:14:34',
            'status': 'done',
            'reserve1': 'reserve1',
            'reserve2': 'reserve2',
            'reserve3': 'reserve3',
            'reserve4': 'reserve4',
            'reserve5': 'reserve5',
            'booAtime': '2023-05-13 18:14:34',
            'Column1': 'column1',
            'booFare': 'fare',
            'booNo': 'no',
            'booNumber': 'number',
            'booOrderNum': 'order',
            'booTime': '2023-05-13 18:14:34',
            'boobAddress': 'baddress',
            'boobTime': '2023-05-13 18:14:34',
            'comCode': 'code',
            'cusTelNumber': 'tel',
            'flag': 'flag',
            'flagPay': 'pay',
            'persions':''
        }
        response = self.client.post('/book/save', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {
                "success": True,
                "message": "Add Success",
                "data": data
            }
        )

    def test_update(self):
        data = {
            'id': 1,
            'booAAddress': 'new_address',
            'create_time': '2022-01-01 12:00:00',
            'status': 'done',
            'reserve1': 'reserve1',
            'reserve2': 'reserve2',
            'reserve3': 'reserve3',
            'reserve4': 'reserve4',
            'reserve5': 'reserve5',
            'booAtime': '2022-01-01 12:00:00',
            'Column1': 'column1',
            'booFare': 'fare',
            'booNo': 'no',
            'booNumber': 'number',
            'booOrderNum': 'order',
            'booTime': '2022-01-01 12:00:00',
            'boobAddress': 'baddress',
            'boobTime': '2022-01-01 12:00:00',
            'comCode': 'code',
            'cusTelNumber': 'tel',
            'flag': 'flag',
            'flagPay': 'pay'
        }
        response = self.client.post('/book/update?id={self.book.id}', json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.book.refresh_from_db()
        self.assertEqual(self.book.booAAddress, 'new_address')
