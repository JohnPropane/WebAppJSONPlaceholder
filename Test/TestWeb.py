import unittest
from unittest.mock import patch
import web_functions as web


class TestWeb(unittest.TestCase):

    @patch('web_functions.requests.get')
    def test_generate_post(self, mock_get):

        mock_response_posts = [{"id": 1, "title": "Title 1", "body": "Body 1"},
                               {"id": 2, "title": "Title 2", "body": "Body 2"}]

        mock_response_comments = [{"postId": 1, "email": "email1@example.com", "body": "Comment 1", "name": "Name 1"},
                                  {"postId": 2, "email": "email2@example.com", "body": "Comment 2", "name": "Name 2"}]

        mock_get.side_effect = [
            unittest.mock.Mock(json=unittest.mock.Mock(return_value=mock_response_posts)),
            unittest.mock.Mock(json=unittest.mock.Mock(return_value=mock_response_comments))
        ]

        generated_posts = web.generate_posts(2)

        expected_posts = [
            ["Title 1", "Body 1", [["email1@example.com", "Comment 1", "Name 1"]], 1],
            ["Title 2", "Body 2", [["email2@example.com", "Comment 2", "Name 2"]], 2]
        ]

        self.assertEqual(generated_posts, expected_posts)

    @patch('web_functions.generate_posts')
    def test_generate2(self, mock_generate_posts):
        mock_generate_posts.return_value = [
            ["Title 1", "Body 1", [["email1@example.com", "Comment 1", "Name 1"]], 1],
            ["Title 2", "Body 2", [["email2@example.com", "Comment 2", "Name 2"]], 2]
        ]
        self.assertEqual(web.generate2(10, 1001, 1000), "Error1")
        self.assertEqual(web.generate2(101, 0, 1000), "Error2")

        expected_posts = [
            ["Title 1", "Body 1", [["email1@example.com", "Comment 1", "Name 1"]], 1],
            ["Title 2", "Body 2", [["email2@example.com", "Comment 2", "Name 2"]], 2],
            2
        ]
        self.assertEqual(web.generate2(2, 0, 1000), expected_posts)

        expected_posts = [
            ["Title 1", "Body 1", [["email1@example.com", "Comment 1", "Name 1"]], 1],
            ["Title 2", "Body 2", [["email2@example.com", "Comment 2", "Name 2"]], 2],
            2
        ]
        self.assertEqual(web.generate2(3, 0, 1000), expected_posts)

    @patch('web_functions.requests.get')
    def test_generate_albums(self, mock_get):
        mock_response = [{"id": 1, "title": "Album 1"},
                         {"id": 2, "title": "Album 2"},
                         {"id": 3, "title": "Album 3"}]

        mock_get.return_value.json.return_value = mock_response
        result = web.generate_albums(3)
        expected = [[1, "Album 1"], [2, "Album 2"], [3, "Album 3"]]
        self.assertEqual(result, expected)

    @patch('web_functions.requests.get')
    def test_generate_photos(self, mock_get):
        mock_response = [
            {"albumId": 1, "title": "Photo 1", "url": "url1", "thumbnailUrl": "thumbnail1"},
            {"albumId": 1, "title": "Photo 2", "url": "url2", "thumbnailUrl": "thumbnail2"},
            {"albumId": 2, "title": "Photo 3", "url": "url3", "thumbnailUrl": "thumbnail3"}
        ]

        mock_get.return_value.json.return_value = mock_response

        album_id = 1
        num_of_photos = 2
        expected_photos = [
            ["Photo 1", "url1", 1, "button0", "thumbnail1"],
            ["Photo 2", "url2", 1, "button1", "thumbnail2"]
        ]

        result = web.generate_photos(album_id, num_of_photos)
        self.assertEqual(result, expected_photos)

