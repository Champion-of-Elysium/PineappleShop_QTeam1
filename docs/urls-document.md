# Pineapple Django Web Application URLs Configuration 🍍

## Introduction
This document provides an overview of the URL configuration for the Pineapple Django Web Application. The application defines URL patterns for managing subscriptions, sellers, pineapples, orders, and comments.

## URL Configuration
In the Pineapple Django Web Application, URL patterns are defined in the `urls.py` file. This file is responsible for mapping URLs to view functions, allowing users to navigate and interact with different parts of the application. Below is a breakdown of the URL patterns defined in the application:

### Subscriptions
- `/subscription-create/` - This URL pattern maps to the `subscription_create_view` function and is used for creating subscriptions.
- `/subscription-list/` - This URL pattern maps to the `subscription_list_view` function and is used for listing subscriptions.

### Sellers
- `/seller/` - This URL pattern maps to the `seller_list_view` function and is used for listing sellers.
- `/seller-create/` - This URL pattern maps to the `seller_create_view` function and is used for creating sellers.
- `/seller/<str:certificate_code>/` - This URL pattern maps to the `seller_detail_view` function and is used for displaying details of a specific seller based on their certificate code.
- `/seller-update/<str:certificate_code>/` - This URL pattern maps to the `seller_update_view` function and is used for updating the details of a specific seller based on their certificate code.

### Pineapples
- `/pineapple-list/` - This URL pattern maps to the `pineapple_list_view` function and is used for listing pineapples.
- `/pineapple-detail/<int:pk>/` - This URL pattern maps to the `pineapple_detail_view` function and is used for displaying details of a specific pineapple based on its primary key.
- `/pineapple-create/` - This URL pattern maps to the `pineapple_create_view` function and is used for creating pineapples.
- `/pineapple-update/<int:pk>/` - This URL pattern maps to the `pineapple_update_view` function and is used for updating the details of a specific pineapple based on its primary key.
- `/seller-pineapple-list/<int:seller_id>/` - This URL pattern maps to the `seller_pineapple_list_view` function and is used for listing pineapples associated with a specific seller.

### Orders
- `/order-list/` - This URL pattern maps to the `order_list_view` function and is used for listing orders.
- `/order-detail/<int:pk>` - This URL pattern maps to the `order_detail_view` function and is used for displaying details of a specific order based on its primary key.
- `/order-create/` - This URL pattern maps to the `order_create_view` function and is used for creating orders.
- `/order-update/<int:pk>/` - This URL pattern maps to the `order_update_view` function and is used for updating the details of a specific order based on its primary key.

### Comments
- `/comment-create/` - This URL pattern maps to the `comment_create_view` function and is used for creating comments.
- `/seller/<str:certificate_code>/comments/` - This URL pattern maps to the `seller_comment_list_view` function and is used for listing comments associated with a specific seller based on their certificate code.

## Static Files (DEBUG Mode)
In addition to the main URL patterns, the application also serves static files in DEBUG mode. These static files include JavaScript, CSS, and other assets required for the frontend of the application.

### Serving Static Files
- `/static/` - This URL pattern serves static files such as CSS and JavaScript.
- `document_root=settings.STATIC_ROOT` - The `settings.STATIC_ROOT` directory is used as the document root for serving static files.

Please note that the ability to serve static files is typically enabled in DEBUG mode for development purposes and should be configured differently for production deployments.

This concludes the URL configuration for the Pineapple Django Web Application, allowing users to access various features of the application through the defined URL patterns.
