import re


class PracticalClassLists():
    def init(self):
        super().__init__()

    def convert_numbers(phone):
        result = re.sub('(?<!\S)(\d{3})', r'(\1) ', phone)
        return result

    phone_number = 'Please call to 9157675453'
    print(convert_numbers(phone_number))
