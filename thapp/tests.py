from django.test import TestCase


class TestMyModel(TestCase):
    def test__name(self):
        from thapp.models import MyModel
        MyModel.objects.create(name='test')
        actual = MyModel.objects.first()
        self.assertEqual(actual.name, 'test')


class TestChild(TestCase):
    def test__mymodel(self):
        from thapp.models import Child
        from thapp.models import MyModel
        mymodel = MyModel.objects.create(name='test')
        Child.objects.create(mymodel=mymodel)

        actual = Child.objects.first()
        self.assertEqual(actual.mymodel, mymodel)

