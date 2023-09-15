# Pineapple Django Web Application Forms Configuration 🍍

## Introduction
This module contains Django forms for different models used in various applications within our project. Each form includes validation methods for specific fields to ensure data consistency and integrity. These forms are essential for creating and updating information related to sellers, pineapples, orders, subscriptions, and comments.

## Available Forms

### 1. SellerForm
- **Purpose:** Form for creating and updating seller information.
- **Model:** Seller (imported from .models)
- **Fields:** All fields from the Seller model
- **Custom Validation:**
  - `clean_address`: Ensures that the address provided is at least 10 characters long.
  - `clean_certificate_code`: Validates that the certificate code consists of uppercase letters.

### 2. PineappleForm
- **Purpose:** Form for creating and updating pineapple information.
- **Model:** Pineapple (imported from .models)
- **Fields:** All fields from the Pineapple model
- **Custom Validation:**
  - `clean_price_toman`: Validates that the price of a pineapple is not less than 1000 toman and not greater than 1,000,000 toman.

### 3. OrderForm
- **Purpose:** Form for creating and updating order information.
- **Model:** Order (imported from .models)
- **Fields:** All fields from the Order model
- **Custom Validation:**
  - `clean_weight_kg`: Ensures that the weight of an order does not exceed 100 kilograms.

### 4. SubscriptionForm
- **Purpose:** Form for creating and updating subscription information.
- **Model:** Subscription (imported from .models)
- **Fields:** All fields from the Subscription model
- **Custom Validation:**
  - `clean_phone_number`: Validates that the phone number starts with '09' and consists of 11 digits.

### 5. CommentForm
- **Purpose:** Form for creating and updating comments.
- **Model:** Comment (imported from .models)
- **Fields:** All fields from the Comment model
- **Custom Validation:**
  - `clean_text`: Ensures that the comment text is at least 10 characters long.

These forms are designed to maintain data quality and consistency throughout the application. They help prevent incorrect or invalid data from being saved to the database, ensuring a reliable and accurate system.
