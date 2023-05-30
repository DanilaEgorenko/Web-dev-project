from django.test import TestCase

from django.test import TestCase
from datetime import date
from apps.promocodes.models import Promocode

class PromocodeModelTest(TestCase):
    def setUp(self):
        self.promocode = Promocode.objects.create(
            name='TEST123',
            deadline=date.today(),
            count_of_uses=10
        )

    def test_promocode_creation(self):
        self.assertEqual(self.promocode.name, 'TEST123')
        self.assertEqual(self.promocode.deadline, date.today())
        self.assertEqual(self.promocode.count_of_uses, 10)

    def test_promocode_string_representation(self):
        self.assertEqual(str(self.promocode), str(self.promocode.pk))

    def test_verbose_names(self):
        self.assertEqual(
            Promocode._meta.verbose_name, 
            'Промокод')
        self.assertEqual(
            Promocode._meta.verbose_name_plural, 
            'Промокоды')
