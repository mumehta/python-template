
import unittest


from app.workers.tasks import add


class TestPythonTemplateApp(unittest.TestCase):

    def test_task(self):
        result = add(2, 3)
        self.assertEqual(5, result)
