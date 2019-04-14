import requests
import json as JSON
import urllib

class exercice_maker:
    def __init__(self, num, mail, name):
        self.num = num
        self.mail = mail
        self.name = name

    def csv_to_arr(self, csv):
        data = str(csv.file.read())[2:-1]
        data = data.split("\\r\\n")[:-1]
        n = 0
        for i in data:
            data[n] = data[n].split(',')
            n += 1
        return [True, data, None]

    def checker(self, arr):
        n = 0
        t = {}
        for i in arr[1:]:
            n2 = 0
            lang = ""
            for i2 in i:
                key = arr[0][n2]
                if key == "lang":
                    lang = arr[n][n2] if arr[n][n2] is not "" else lang
                    print(lang)
                    if t[lang] is None:
                        t[lang] = {"queries":[], "waited":[], "value":[]}
                else:
                    if t[lang][key][n] is None:
                        t[lang][key][n] = []
                    if arr[n][n2] is not "":
                        t[lang][key][n].append(arr[n][n2])
                n2 += 1
            n += 1
        return [True, t, None]

    def uploader(self, arr):
        return [True, arr, None]
