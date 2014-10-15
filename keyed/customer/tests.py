import pytest

from django.test import TestCase

from model_mommy import mommy

from customer.models import Customer


class ModelTests(TestCase):

    def test_customer(self):
        c = mommy.make(Customer)
        assert isinstance(c, Customer)
        assert c.__str__() == c.name