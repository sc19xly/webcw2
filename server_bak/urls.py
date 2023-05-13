from django.contrib import admin
from django.urls import path

from book import views as book
from bookuser import views as BookUser
from custom import views as custom
from payerLink import views as payerLink
from airLink import views as airLink

urlpatterns = [
    path('admin/', admin.site.urls),
    path('custom/info',custom.info,name='info'),
    path('custom/delete',custom.delete,name='delete'),
    path('custom/list',custom.list,name='list'),
    path('custom/save',custom.save,name='save'),
    path('custom/update',custom.update,name='update'),
    path('custom/page',custom.page,name='pag'),
    path('custom/login',custom.login,name='login'),
    path('book/info',book.info,name='info'),
    path('book/delete',book.delete,name='delete'),
    path('book/list',book.list,name='list'),
    path('book/save',book.save,name='save'),
    path('book/update',book.update,name='update'),
    path('book/page',book.page,name='pag'),
    path('bookUser/info',BookUser.info,name='info'),
    path('bookUser/delete',BookUser.delete,name='delete'),
    path('bookUser/list',BookUser.list,name='list'),
    path('bookUser/save',BookUser.save,name='save'),
    path('bookUser/update',BookUser.update,name='update'),
    path('bookUser/page',BookUser.page,name='pag'),
    path('airLink/info',airLink.info,name='info'),
    path('airLink/delete',airLink.delete,name='delete'),
    path('airLink/list',airLink.list,name='list'),
    path('airLink/save',airLink.save,name='save'),
    path('airLink/update',airLink.update,name='update'),
    path('airLink/page',airLink.page,name='pag'),
    path('airLink/airList',airLink.airList,name='airList'),
    path('payerLink/exitMoney',payerLink.exitMoney,name='exitMoney'),
    path('payerLink/pay',payerLink.pay,name='pay'),
    path('payerLink/info',payerLink.info,name='info'),
    path('payerLink/delete',payerLink.delete,name='delete'),
    path('payerLink/list',payerLink.list,name='list'),
    path('payerLink/save',payerLink.save,name='save'),
    path('payerLink/update',payerLink.update,name='update'),
    path('payerLink/page',payerLink.page,name='pag'),

]
