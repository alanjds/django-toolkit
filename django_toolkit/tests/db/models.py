try:
    from django.utils.unittest import TestCase
except ImportError:
    from django.test import TestCase
from django_toolkit.tests.testapp.models import ModelWithChainedQuerySet


class QuerySetManagerTestCase(TestCase):

    def test_chaining(self):
        ModelWithChainedQuerySet.objects.bulk_create([
            ModelWithChainedQuerySet(foo=False, bar=False),
            ModelWithChainedQuerySet(foo=True, bar=False),
            ModelWithChainedQuerySet(foo=False, bar=True),
            ModelWithChainedQuerySet(foo=True, bar=True),
            ModelWithChainedQuerySet(foo=True, bar=True),
        ])
        self.assertEqual(ModelWithChainedQuerySet.objects.is_foo().count(), 3)
        self.assertEqual(ModelWithChainedQuerySet.objects.is_foo().is_not_foo().count(), 0)
        self.assertEqual(ModelWithChainedQuerySet.objects.is_foo().is_not_bar().count(), 1)
        self.assertEqual(ModelWithChainedQuerySet.objects.is_foo().is_bar().count(), 2)
        self.assertEqual(ModelWithChainedQuerySet.objects.is_bar().count(), 3)
        self.assertEqual(ModelWithChainedQuerySet.objects.is_bar().is_not_bar().count(), 0)
        self.assertEqual(ModelWithChainedQuerySet.objects.is_bar().is_not_foo().count(), 1)
