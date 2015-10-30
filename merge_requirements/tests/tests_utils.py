#!/usr/bin/env python
# encoding: utf-8

from unittest import TestCase
from unittest.mock import MagicMock
from utils import remove_comments

class TestUtils(TestCase):

    @patch('package.module.attribute', sentinel.attribute)
    def test_remove_comments(self):

        text_file = '''#COMENTARIOS\nCherryPy==3.2.4\nDjango==1.4.13\nIPTCInfo==1.9.5-6\nIon==0.6.4.2\n#COMENTARIO2\nJinja2==2.7\nMarkupSafe==0.18\nMySQL-python==1.2.3\nPIL==1.1.7-1\nPillow==2.1.0\nRoutes==2.0\nSQLAlchemy==0.5.8\nSouth==0.7.3\n'''

        expected_text_file = '''CherryPy==3.2.4\nDjango==1.4.13\nIPTCInfo==1.9.5-6\nIon==0.6.4.2\nJinja2==2.7\nMarkupSafe==0.18\nMySQL-python==1.2.3\nPIL==1.1.7-1\nPillow==2.1.0\nRoutes==2.0\nSQLAlchemy==0.5.8\nSouth==0.7.3\n'''

        self.assertEqual(
            remove_comments(text_file),
            expected_text_file,
        )

    def test_merge_dict(self):

        bdict = {
            'CherryPy': '3.2.4',
            'Django': '1.4.13',
            'MySQL-python': '1.2.3',
            'Pillow': '2.1.0',
            'MarkupSafe': '0.18'
        }

        mdict = {
            'CherryPy': '3.2.0',
            'Django': '1.4.13',
            'MySQL-python': '1.2.3',
            'Pillow': '2.1.0',
            'MarkupSafe': '0.18',
            'SQLAlchemy': '0.5.8'
        }

        res_dict = merge_dict(bdict, mdict)

        merge_dict = {
            'CherryPy': '3.2.4',
            'Django': '1.4.13',
            'MySQL-python': '1.2.3',
            'Pillow': '2.1.0',
            'MarkupSafe': '0.18',
            'SQLAlchemy': '0.5.8'
        }

        self.assertDictEqual(res_dict, merge_dict)

if __name__ == '__main__':
    unittest.main()
