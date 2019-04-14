import requests
import json as JSON
import urllib

class exercice_maker:
    def __init__(self, num, mail, name):
        self.num = num
        self.mail = mail
        self.name = name

    def csv_to_arr(self, csv):
        data = str(csv.file.read())
        data = data.split("\\r\\n")[2:]
        n = 0
        for i in data:
            data[n] = data[n].split(',')
            n += 1
        return [True, data, None]

    def checker(self, arr):
        return [True, arr, None]

    def uploader(self, arr):
        return [True, arr, None]
