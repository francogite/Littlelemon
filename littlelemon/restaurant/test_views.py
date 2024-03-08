from django.test import TestCase
from restaurant.views import MenuItemView
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuItemViewTest(TestCase):
    def setUp(self):
        self.menu1 = Menu("Sweep Pea Pesto", 2, 20)
        self.menu2 = Menu("Mozzarella & tomato", 3, 30)
        self.menu3 = Menu("Antipasto", 4, 40)
        
    def test_getall(self):
        item = self.menu1
        serializer = MenuSerializer(data=item)
        self.assertTrue(serializer.is_valid)     
