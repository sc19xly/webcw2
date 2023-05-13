from django.test import TestCase, Client
import json

from django.urls import reverse

from payerLink.models import PayerLink

class PayerLinkTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.payerlink1 = PayerLink.objects.create(link='http://localhost:8000', name='test1', username='test1')
        self.payerlink2 = PayerLink.objects.create(link='http://localhost:8001', name='test2', username='test2')

    def test_list(self):
        response = self.client.get('/payerLink/list')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertTrue(data['success'])
        self.assertEqual(len(data['data']), 2)

    def test_info(self):
        response = self.client.get('/payerLink/info?id=%d' % self.payerlink1.id)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertTrue(data['success'])
        self.assertEqual(data['data']['name'], 'test1')

    def test_delete(self):
        response = self.client.get('/payerLink/delete?id=%d' % self.payerlink1.id)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertTrue(data['success'])
        self.assertIsNone(PayerLink.objects.filter(id=self.payerlink1.id).first())

    def test_save(self):
        data = {'link': 'http://localhost:8002', 'name': 'test3', 'username': 'test3'}
        response = self.client.post('/payerLink/save', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertTrue(data['success'])
        self.assertEqual(PayerLink.objects.filter(name='test3').count(), 1)

    def test_update(self):
        data = {'id': self.payerlink1.id, 'name': 'test4'}
        response = self.client.post('/payerLink/update', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertTrue(data['success'])
        self.assertEqual(PayerLink.objects.get(id=self.payerlink1.id).name, 'test4')

    def test_page(self):
        PayerLink.objects.create(
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
        self.assertEqual(content['total'], 3)
        data = content['data']
        self.assertEqual(len(data), 3)
