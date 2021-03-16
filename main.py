import json
import requests
import hashlib


class Search_countries:

    def __init__(self, file_path):
        self.file_path = file_path
        with open(file_path, encoding='utf-8') as f:
            json_data = json.load(f)
            self.countrie_list = [countrie["name"]["common"] for countrie in json_data]
            self.quantity_countrie = len(self.countrie_list)

    def __iter__(self):
        return self

    def __next__(self):
        self.quantity_countrie -= 1
        if self.quantity_countrie == -1:
            raise StopIteration
        url = 'https://en.wikipedia.org/wiki/' + '_'.join(self.countrie_list[self.quantity_countrie].split(' '))
        r = requests.head(url)
        if r.status_code == 200:
            return f'{self.countrie_list[self.quantity_countrie]} - {url}'
        else:
            print(f'{self.countrie_list[self.quantity_countrie]} - Ошибка')


if __name__ == '__main__':
    with open('final.txt', 'w', encoding='utf-8') as ouf:
        for i in Search_countries("countries.json"):
            ouf.write(i + '\n')



def hash_coutries(file_path):
    with open(file_path, encoding='utf-8') as f:
        for line in f:
            hash_object = hashlib.md5(line.strip().encode())
            yield hash_object.hexdigest()



if __name__ == '__main__':
    for i in hash_coutries('final.txt'):
        print(i)
