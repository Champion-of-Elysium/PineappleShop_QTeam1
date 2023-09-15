from django.test import TestCase
from django.urls import reverse
from pineapple.models import Subscription, Seller, Pineapple, Order, Comment


class TemplateTestCase(TestCase):
    def setUp(self) -> None:
        # Create test data for the models
        self.seller = Seller.objects.create(
            name="TestSeller",
            address="29334 Hester Ranch Address",
            certificate_code="123456"
        )
        
        self.pineapple = Pineapple.objects.create(
            price_toman=100,
            seller=self.seller
        )
        
        self.order = Order.objects.create(
            pineapple=self.pineapple,
            name="Test Order",
            weight_kg=1.5
        )
        
        self.comment = Comment.objects.create(
            seller=self.seller,
            name="Test Comment",
            text="This is a test comment."
        )
        
        self.subscription = Subscription.objects.create(
            name="Test Subscriber",
            phone_number="12345678901"
        )
    
    # Subscription
    def test_subscription_create(self):
        response = self.client.get(reverse('pineapple:subscription-create'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'ثبت نام در خبرنامه')
        self.assertContains(response, 'submit')

    def test_subscription_list(self):
        response = self.client.get(reverse('pineapple:subscription-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'لیست خبرنامه')
        self.assertContains(response, self.subscription.phone_number)

    # AH/Pineapple
    def test_pineapple_update(self):
        response = self.client.get(reverse('pineapple:pineapple-update',args=[self.pineapple.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'بروزرسانی آناناس')
        self.assertContains(response, 'submit')
    
    def test_pineapple_detail(self): 
        response=self.client.get(reverse('pineapple:pineapple-detail', args=[self.pineapple.pk]))  
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'صفحه‌ی داخلی آناناس')
        self.assertContains(response, self.pineapple.price_toman)
        self.assertContains(response, self.pineapple.seller.certificate_code)        


    #AK/Order
    def test_order_list(self):
        response = self.client.get(reverse('pineapple:order-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "لیست سفارشات")
        self.assertContains(response, self.order.pineapple.seller.name)
        self.assertContains(response, self.order.name)
        self.assertContains(response, self.order.weight_kg)
 
    def test_order_detail(self):
        response = self.client.get(reverse('pineapple:order-detail',args=[self.order.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "صفحه داخلی سفارش")
        self.assertContains(response, self.order.pineapple.seller.name)
        self.assertContains(response, self.order.name)
        self.assertContains(response, self.order.weight_kg)

    def test_order_create(self):
        response = self.client.get(reverse('pineapple:order-create'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,"ثبت سفارش")
        self.assertContains(response,"submit")
