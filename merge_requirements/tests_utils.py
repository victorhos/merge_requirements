#!/usr/bin/env python
# encoding: utf-8

import mock
import unittest
import builtins

from utils import remove_comments

class TestUtils(unittest.TestCase):

    def test_remove_comments(self):

        text_file = '''
#COMENTARIOS\n'CherryPy==3.2.4\nDjango==1.4.13\nIPTCInfo==1.9.5-6\nIon==0.6.4.2\n#COMENTARIO2\nJinja2==2.7\nMarkupSafe==0.18\nMySQL-python==1.2.3\nPIL==1.1.7-1\nPillow==2.1.0\nRoutes==2.0\nSQLAlchemy==0.5.8\nSouth==0.7.3\n
        '''

        expected_text_file = '''
'CherryPy==3.2.4\nDjango==1.4.13\nIPTCInfo==1.9.5-6\nIon==0.6.4.2\nJinja2==2.7\nMarkupSafe==0.18\nMySQL-python==1.2.3\nPIL==1.1.7-1\nPillow==2.1.0\nRoutes==2.0\nSQLAlchemy==0.5.8\nSouth==0.7.3\n
        '''

        with patch.object(
            builtins,
            'open',
            mock_open(read_data=text_file)):

            with open('foo') as handle:
                self.assertEqual(
                    remove_comments(handle.read()),
                    expected_text_file
                )

if __name__ == '__main__':
    main()
