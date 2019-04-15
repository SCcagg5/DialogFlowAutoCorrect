import requests
import json as JSON
import urllib
import os
from git import Repo

class exercice_maker:
    def __init__(self, num, mail, name):
        self.num = num
        self.mail = mail
        self.name = name
        self.namefile = "exo" + num + ".json"

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
                    lang = i2 if i2 is not "" else lang
                    if lang not in t:
                        t[lang] = {"queries":[], "waited":[], "value":[]}
                else:
                    if len(t[lang][key]) < (n + 1):
                        t[lang][key].append([])
                    if i2 is not "":
                        t[lang][key][n].append(i2)
                n2 += 1
            n += 1
        return [True, t, None]

    def uploader(self, arr):
        completeName = os.path.join("home/DialogFlowModule/", self.namefile)
        file1 = open(completeName, "w")
        file1.write(JSON.dumps(arr))
        file1.close()
        repo = Repo("/home/DialogFlowModule/.git")
        repo.git.add(self.namefile)
        repo.index.commit(self.namefile + " added by " + self.name + " <" + self.mail+">")
        origin = repo.remote(name='origin')
        origin.push()
        return [True, arr, None]
