#!virtualenv/bin/python
import os
import myapp
import unittest
import tempfile


class MyAppTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, myapp.app.config['DATABASE'] = tempfile.mkstemp()
        myapp.app.config['TESTING'] = True
        self.app = myapp.app.test_client()
        # myapp.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(myapp.app.config['DATABASE'])

    def test_app_resolves(self):
        rv = self.app.get('/')
        self.assertEqual(200, rv.status_code)

if __name__ == '__main__':
    unittest.main()
