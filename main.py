'''
В работе используется простое учебное Python-приложение для хранения информации о книге.
Приложение умеет: 
	- сохранять информацию о книге в файл 
	- читать информацию о книге из файла 
	- работать с каталогом /app/data, в котором хранятся данные 
'''
import os

class Book:
    def __init__(self, title: str, author: str, status: str):
        self.title = title
        self.author = author
        self.status = status

    def to_dict(self):
        return {
            'title': self.title,
            'author': self.author,
            'status': self.status
        }

    def save_to_file(self, filename):
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"Title: {self.title}\n")
            f.write(f"Author: {self.author}\n")
            f.write(f"Status: {self.status}\n")

    @staticmethod
    def load_from_file(filename: str):
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()

            title = lines[0].split(": ")[1].strip()
            author = lines[1].split(": ")[1].strip()
            status = lines[2].split(": ")[1].strip()
            return Book(title, author, status)


