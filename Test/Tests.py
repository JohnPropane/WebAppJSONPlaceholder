import unittest
from unittest.mock import patch
from flask import request
import web_functions
from main import app


class Tests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    @patch('web_functions.generate2')
    def test_posts_route(self, mock_generate2):
        mock_generate2.return_value = [{'title': 'Post 1', 'content': 'Content 1'},
                                       {'title': 'Post 2', 'content': 'Content 2'}]
        response = self.app.post('/posts', data={'max-posts': '10', 'min-len': '5', 'max-len': '10'})
        self.assertEqual(response.status_code, 200)

    @patch('web_functions.generate_photos')
    def test_photos_route(self, mock_generate_photos):
        mock_generate_photos.return_value = [{'title': 'Photo 1'}, {'title': 'Photo 2'}]
        response = self.app.post('/albums/photos/1', data={'max-posts': '10'})
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
