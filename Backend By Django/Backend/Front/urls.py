from django.urls import path
from django.urls.conf import include
from rest_framework_nested import routers
from . import views


router = routers.DefaultRouter()
router.register('parents', views.ParentViewSet, basename='parents')
router.register('child', views.ChildViewSet, basename= 'child')
router.register('activity', views.ActivityViewSet, basename='activity')

# products_router = routers.NestedDefaultRouter( router, 'products', lookup='product')
# products_router.register('reviews', views.ReviewViewSet, basename='product-reviews')


# URLConf
urlpatterns = router.urls # + products_router.urls + carts_router.urls
