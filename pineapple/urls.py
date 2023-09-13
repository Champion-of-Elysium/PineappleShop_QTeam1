"""
URL Configuration for the Pineapple Django Web Application

Defines URL patterns for managing subscriptions, sellers, pineapples, orders, and comments.

"""

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "pineapple"

urlpatterns = [

    # AJ/subscription-urls
    path('subscription-create/', views.views_subscription.subscription_create_view, name="subscription-create"),
    path('subscription-list/', views.views_subscription.subscription_list_view, name="subscription-list"),

    # AK/seller-urls
    path('seller/', views.seller_list_view, name='seller-list'),
    path('seller-create/', views.seller_create_view, name='seller-create'),
    path('seller/<str:certificate_code>/', views.seller_detail_view, name='seller-detail'),
    path('seller-update/<str:certificate_code>/', views.seller_update_view, name='seller-update'),

    # Kia/pineapple-Urls
    path("pineapple-list/", views.views_pineapple.pineapple_list_view, name="pineapple-list"),
    path("pineapple-detail/<int:pk>/", views.views_pineapple.pineapple_detail_view, name="pineapple-detail"),
    path("pineapple-create/", views.views_pineapple.pineapple_create_view, name="pineapple-create"),
    path("pineapple-update/<int:pk>/", views.views_pineapple.pineapple_update_view, name="pineapple-update"),
    path("seller-pineapple-list/<int:seller_id>/", views.views_pineapple.seller_pineapple_list_view,
         name="seller-pineapple-list"),

    # AH/order-urls
    path('order-list/', views.order_list_view, name='order-list'),
    path('order-detail/<int:pk>', views.order_detail_view, name='order-detail'),
    path('order-create/', views.order_create_view, name='order-create'),
    path('order-update/<int:pk>/', views.order_update_view, name='order-update'),

    # IDA/comment-urls
    path('comment-create/', views.comment_create_view, name='comment-create'),
    path('seller/<str:certificate_code>/comments/', views.seller_comment_list_view, name='seller-comment-list'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
