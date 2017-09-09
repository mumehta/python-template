
import unittest
from invoke import task


@task
def test():
    print('this is test')
    all_tests = unittest.TestLoader().discover("app")
    result = unittest.TextTestRunner().run(all_tests)
