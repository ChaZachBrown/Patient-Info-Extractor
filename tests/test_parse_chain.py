import json
import os
import unittest
from collections import defaultdict
from chains.import_patient_data import parse_data

""" This POC testing framework allows for the testing of multiple prompts an X number of times and logs the results
    for import into BI tools for review. """

NUM_TEST_RUNS = 5


class TestDataService(unittest.TestCase):
    test_counter = 0

    @classmethod
    def setUpClass(cls):
        """ Set prompts to be testing and logging file structure """

        cls.file_data = {
            '': defaultdict(
                lambda: {"total_tests": 0, "total_pass": 0, "total_fail": 0, "errors": []}),
            '': defaultdict(
                lambda: {"total_tests": 0, "total_pass": 0, "total_fail": 0, "errors": []})
        }

        cls.data_json_list = []
        cls.data_dict_list = []

        for path in cls.file_data.keys():
            for _ in range(NUM_TEST_RUNS):
                data_json = parse_data(path)
                cls.data_json_list.append(data_json)
                cls.data_dict_list.append(json.loads(data_json))

    def setUp(self):
        """ Set expected test results """

        self.schema = {
            "PatientID": "string",
            "FirstName": "string",
            "LastName": "string",
            "DateOfBirth": "string",
            "Gender": "string",
            "Address": "string",
            "ContactNumber": "string",
            "Email": "string",
            "MedicalHistory": "string",
            "Allergies": "string",
            "Medications": "string",
            "InsuranceDetails": {
                "provider": "string",
                "policy_number": "string"
            },
            "EmergencyContact": {
                "name": "string",
                "contact": "string"
            }
        }
        self.expected_data = {
            "PatientID": "8c7ee3e8-ca60-4871-b479-6484891c364e",
            "FirstName": "Karen",
            "LastName": "Luis",
            "DateOfBirth": "1906-05-11",
            "Gender": "Female",
            "Address": "PSC 6923, Box 7215 APO AA 49931",
            "ContactNumber": "223-515-8119x123",
            "Email": "goodwintrevor@anderson-gamble.net",
            "MedicalHistory": "Patient has a history of diabetes. Regular check-ups are advised.",
            "Allergies": "Patient has severe reactions to shellfish, medical attention required. Dairy products.",
            "Medications": "Patient is currently taking Lisinopril for hyperlipidemia. Topiramate 50mg once daily, Gabapentin 300mg twice daily.",
            "InsuranceDetails": {
                "provider": "Patterson-Hayes",
                "policy_number": "PH12345678"
            },
            "EmergencyContact": {
                "name": "Nancy Lewis",
                "contact": "(456) 789-0123"
            }
        }

    # test wrapper methods
    def test_valid_json(self):
        self.generic_test_handler(self.data_json_list, self.validate_json, "test_valid_json")

    def test_keys(self):
        self.generic_test_handler(self.data_dict_list, self.validate_keys, "test_keys")

    def test_values(self):
        self.generic_test_handler(self.data_dict_list, self.validate_values, "test_values")

    # Actual tests
    def validate_json(self, data_json):
        json.loads(data_json)

    def validate_keys(self, data_dict):
        schema_keys = set(self.schema.keys())
        data_keys = set(data_dict.keys())
        self.assertEqual(schema_keys, data_keys, "JSON keys do not match schema")

    def validate_values(self, data_dict):
        for key in self.schema:
            if isinstance(self.schema[key], dict):
                for nested_key in self.schema[key]:
                    self.assertEqual(data_dict[key][nested_key], self.expected_data[key][nested_key],
                                     f"Field {key}.{nested_key} does not match expected value")
            else:
                self.assertEqual(data_dict[key], self.expected_data[key], f"Field {key} does not match expected value")

    # Test handler for results tracking
    def generic_test_handler(self, data_list, validation_method, test_name):
        for index, data in enumerate(data_list):
            current_file = list(self.file_data.keys())[index // NUM_TEST_RUNS]
            with self.subTest(i=index):
                try:
                    validation_method(data)
                    self.file_data[current_file][test_name]["total_pass"] += 1
                except Exception as e:
                    self.file_data[current_file][test_name]["total_fail"] += 1
                    self.file_data[current_file][test_name]["errors"].append(str(e))
                self.file_data[current_file][test_name]["total_tests"] += 1

    @classmethod
    def get_test_methods(cls):
        exclude_methods = {'setUp', 'tearDown', 'setUpClass', 'tearDownClass', 'get_test_methods', 'log_results',
                           'generic_test_handler', 'validate_json', 'validate_keys', 'validate_values', 'test_counter'}
        return [method for method in dir(cls) if method.startswith('test_') and method not in exclude_methods]

    def tearDown(self):
        self.__class__.test_counter += 1
        total_tests = self.get_test_methods()
        if self.__class__.test_counter == len(total_tests):
            self.log_results()

    # Log results to file
    @classmethod
    def log_results(cls):
        log_dir = "test_logs"
        os.makedirs(log_dir, exist_ok=True)

        for filepath, data in cls.file_data.items():
            filename = os.path.basename(filepath)
            log_output = f"File: {filename}\n"

            total_failures = sum(test_data['total_fail'] for test_data in data.values())
            total_passes = sum(test_data['total_pass'] for test_data in data.values())
            total_tests_run = sum(test_data['total_tests'] for test_data in data.values())

            log_output += f"Overall Results: failed: {total_failures}, passed: {total_passes}, ran: {total_tests_run}\n"

            for test_name, test_data in data.items():
                log_output += f"\n{test_name}: failed: {test_data['total_fail']}, passed: {test_data['total_pass']}, ran: {test_data['total_tests']}\n"
                for error in test_data['errors']:
                    log_output += f"{error}\n____________________________________________________________________________\n"

            sanitized_filename = filename.replace('/', '_').replace(':', '').replace('\\', '_')
            log_file_name = os.path.join(log_dir, f'test_log_{sanitized_filename}.log')

            with open(log_file_name, 'w') as log_file:
                log_file.write(log_output)


if __name__ == '__main__':
    unittest.main()

