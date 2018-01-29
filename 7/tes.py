import re

phone_num_regex = re.compile(r'[0-9]{3}-\d{4}-\d{4}')
mo = phone_num_regex.search('私の電話番号は090-1234-5678です。')
print('私の電話番号は: ' + mo.group())