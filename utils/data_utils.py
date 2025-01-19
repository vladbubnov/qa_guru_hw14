import csv


def load_test_data_from_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return [(int(row['dropdown_id']), row['expected_dropdown_text'], row['expected_dropdown_value_text']) for row in
                reader]
