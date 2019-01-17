from unittest import TestCase
from app.dict_tools import check_json_keys, check_json_types


class TestCheckJsonKeys(TestCase):
    def setUp(self):
        self.keys = [
            "name",
            "profession",
            "phone",
            "email",
            "address",
            "portfolio",
            "education",
            "experience",
            "skills",
            "languages",
        ]

    def test_check_json_keys_should_return_tuples_with_bool_and_list(self):
        boolean, missing_keys = check_json_keys({'abc': 123}, keys=self.keys)

        self.assertIsInstance(boolean, bool)
        self.assertIsInstance(missing_keys, list)

    def test_check_json_keys_should_return_false_when_key_missing(self):
        boolean, missing_keys = check_json_keys({'abc': 123}, keys=self.keys)

        self.assertEqual(boolean, False)

    def test_check_json_keys_should_return_missing_keys(self):
        boolean, missing_keys = check_json_keys({'abc': 123}, keys=self.keys)

        self.assertEqual(self.keys, missing_keys)

    def test_check_json_keys_should_return_only_name_key_name(self):
        json = {key: 1 for key in self.keys}
        json.pop('name')

        boolean, missing_keys = check_json_keys(json)

        self.assertIn('name', missing_keys)

    def test_check_json_keys_should_return_true_and_empty_list_when_recive_all_keys(self):  # NOQA
        json = {key: 1 for key in self.keys}

        boolean, missing_keys = check_json_keys(json)

        self.assertEqual(True, boolean)
        self.assertEqual([], missing_keys)


class TestCheckJsonTypes(TestCase):
    def setUp(self):
        self.keys = {
            "name": str,
            "profession": str,
            "phone": str,
            "email": str,
            "address": str,
            "portfolio": str,
            "education": dict,
            "experience": dict,
            "skills": dict,
            "languages": dict,
        }

    def test_check_json_types_should_return_wrong_keys_with_wrong_types(self):
        json = {
            "name": '',
            "profession": '',
            "phone": '',
            "email": '',
            "address": '',
            "portfolio": '',
            "education": '',
            "experience": '',
            "skills": '',
            "languages": '',
        }
        status, keys = check_json_types(json, keys=self.keys)

        self.assertFalse(status)
        self.assertEqual(
            ['education', 'experience', 'skills', 'languages'], keys
        )

    def test_check_json_types_should_return_true_and_blank_lines_when_iput_correct_json(self):  # NOQA
        json = {
            "name": '',
            "profession": '',
            "phone": '',
            "email": '',
            "address": '',
            "portfolio": '',
            "education": [],
            "experience": [],
            "skills": [],
            "languages": [],
        }
        status, keys = check_json_types(json, keys=self.keys)

        self.assertEqual([], keys)
        self.assertTrue(status)
