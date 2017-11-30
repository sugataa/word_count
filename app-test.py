import unittest
import app
from werkzeug.datastructures import ImmutableMultiDict

class BasicTestCase(unittest.TestCase):

    def test_index(self):
        """initial test. ensure flask was set up correctly"""
        tester = app.app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

class WordCountTestCase(unittest.TestCase):

    def setUp(self):
        """Set up a blank temp database before each test"""
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()

    def tearDown(self):
        """Destroy blank temp database after each test"""
        pass

    # assert functions

    def test_word_count(self):
        """Ensure that word count and unique word count is sent on valid text input"""
        data = ImmutableMultiDict([('text_block', 'test')])
        rv = self.app.post('/', data=data)
        assert b'Word Count: 1' in rv.data
        assert b'Unique Words: 1' in rv.data

    def test_word_count_duplicate(self):
        """Ensure that unique word count is correct on valid text input"""
        data = ImmutableMultiDict([('text_block', 'Boys will be boys.')])
        rv = self.app.post('/', data=data)
        assert b'Word Count: 4' in rv.data
        assert b'Unique Words: 3' in rv.data

    def test_word_count_punctuation(self):
        """Ensure that unique word count is correct on valid text input"""
        data = ImmutableMultiDict([('text_block', 'Boys.... will be????? boys.!!!!!')])
        rv = self.app.post('/', data=data)
        assert b'Word Count: 4' in rv.data
        assert b'Unique Words: 3' in rv.data

    def test_word_count_empty(self):
        """Ensure that error is sent when on empty text input"""
        data = ImmutableMultiDict([('text_block', '')])
        rv = self.app.post('/', data=data)
        assert b'Error! Text input is required.' in rv.data


if __name__ == '__main__':
    unittest.main()
