import json
from django.test import TestCase, RequestFactory, Client
from django.urls import reverse
from airLink.models import AirLink


class AirLinkListViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

        self.airLink = AirLink.objects.create(
            link='link',
            name='name',
            username='username'
        )

    def test_list_view(self):
        request = self.client.get('/airLink/list')

        self.assertEqual(request.status_code, 200)
        data = json.loads(request.content)
        self.assertTrue(data['success'])
        self.assertEqual(data['message'], 'Search Success')
        res_list = data['data']
        self.assertEqual(len(res_list), AirLink.objects.count())
        for p, res in zip(AirLink.objects.all(), res_list):
            self.assertEqual(res['id'], p.id)
            self.assertEqual(res['link'], p.link)
            self.assertEqual(res['name'], p.name)
            self.assertEqual(res['username'], p.username)

    def test_airLink_info(self):
        response = self.client.get('/airLink/info', {'id': self.airLink.id})
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content)
        self.assertEqual(content['success'], True)

    def test_book_delete(self):
        response = self.client.get('/airLink/delete', {'id': self.airLink.id})
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content)
        self.assertEqual(content['success'], True)

    def test_save(self):
        data = {
            'id':1,
            'link': 'link',
            'name': 'name',
            'username': 'username'
        }
        response = self.client.post('/airLink/save', json.dumps(data),content_type='application/json')
        self.assertEqual(response.status_code, 200)
        updated_user = AirLink.objects.get(id=1)
        self.assertTrue(updated_user,1)

    def test_update(self):
        response = self.client.post('/airLink/update', json.dumps(
            {"id": 1, "link": "updated_link", "name": "updated_name", 'username': 'updated_username'}),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('success' in response.json())
        self.assertTrue('message' in response.json())
        self.assertTrue('data' in response.json())

        updated_user = AirLink.objects.get(id=1)
        self.assertEqual(updated_user.link, 'updated_link')
        self.assertEqual(updated_user.name, 'updated_name')

    def test_page(self):
        AirLink.objects.create(
            link='link',
            name='name',
            username='username'
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