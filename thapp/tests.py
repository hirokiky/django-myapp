from django.test import TestCase


class TestMyModel(TestCase):
    def test__name(self):
        from thapp.models import MyModel
        MyModel.objects.create(name='test')
        actual = MyModel.objects.first()
        self.assertEqual(actual.name, 'test')
