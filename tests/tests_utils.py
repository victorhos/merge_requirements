import unittest

from merge_requirements.utils import clean_text, merge_dict


class TestUtils(unittest.TestCase):
    def test_clean_text_should_remove_white_spaces_and_commented_lines(self):
        text_file = (
            '#COMENTARIOS\nCherryPy==3.2.4\nDjango==2.1.7\nIPTCInfo==1.9.5-6\nIon==0.6.4.2\n#COMENTARIO2\n'
            'Jinja2==2.7\nMarkupSafe==0.18\nMySQL-python==1.2.3\nPIL==1.1.7-1\nPillow==2.1.0\nRoutes==2.0\n'
            'SQLAlchemy==0.5.8\nSouth==0.7.3\n'
        )

        expected_text_file = (
            'CherryPy==3.2.4\nDjango==2.1.7\nIPTCInfo==1.9.5-6\nIon==0.6.4.2\nJinja2==2.7\nMarkupSafe==0.18\n'
            'MySQL-python==1.2.3\nPIL==1.1.7-1\nPillow==2.1.0\nRoutes==2.0\nSQLAlchemy==0.5.8\nSouth==0.7.3'
        )

        self.assertEqual(
            clean_text(text_file),
            expected_text_file,
        )

    def test_merge_dict_should_successfully(self):
        first_requirements = {
            'CherryPy': '3.2.4',
            'Django': '1.4.13',
            'MySQL-python': '1.2.3',
            'Pillow': '2.1.0',
            'MarkupSafe': '0.18'
        }

        second_requirements = {
            'CherryPy': '3.2.0',
            'Django': '1.4.14',
            'MySQL-python': '1.2.3',
            'Pillow': '2.1.0',
            'MarkupSafe': '0.18',
            'SQLAlchemy': '0.5.8'
        }

        merged_expected = {
            'Django': '1.4.14',
            'MarkupSafe': '0.18',
            'MySQL-python': '1.2.3',
            'Pillow': '2.1.0',
            'SQLAlchemy': '0.5.8',
            'CherryPy': '3.2.4'
        }

        new_requirements, error_requirements = merge_dict(bdict, mdict)

        self.assertDictEqual(
            new_requirements,
            merged_expected
        )


if __name__ == '__main__':
    unittest.main()
