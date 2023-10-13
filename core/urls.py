from django.urls import path, include
from rest_framework import routers
from .views import ProductView, OrderItemView, OrderView, CategoryView, TableView, ReviewView
from users.views import UsersView, GroupView, PermissionsView
router = routers.DefaultRouter()

router.register(r'products', ProductView)
router.register(r'categories', CategoryView)
router.register(r'orders', OrderView)
router.register(r'orderitems', OrderItemView)
router.register(r'users', UsersView)
router.register(r'groups', GroupView)
router.register(r'permissions', PermissionsView)
router.register(r'tables', TableView)
router.register(r'reviews', ReviewView)


urlpatterns = [
    path('', include(router.urls)),
]
