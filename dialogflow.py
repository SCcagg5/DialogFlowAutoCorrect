import requests
import json as JSON
import urllib

class dialogflowapi:
    def __init__(self, bearer = None):
        self.bearer = bearer

    def test(self, exercice):
        ret = {}
        test = requests.get("https://raw.githubusercontent.com/SCcagg5/DialogFlowModule/master/exo"+exercice+".json")
        if test.status_code != 200:
            return [False, "invalid exercice number: " + exercice, 404]
        try:
            test = JSON.loads(test.text)
        except:
            return [False, "invalid json on ex0" + exercice, 500]
        return self.__test(test)

    def __test(self, test):
        ret = {"waited": [], "got": [], "succes": False}
        id = 12345
        for i in test.keys():
            lang = i
            n = 0
            for i2 in test[i]["queries"]:
                for i3 in i2:
                    rep = self.__query(lang, i3, id)
                    if not rep[0]:
                        return rep
                    ret["got"].append(rep[1])
                    ret["waited"].append(test[i]["waited"][n])
                    if rep[1] not in test[i]["waited"][n]:
                        return [True, ret, 500]
                n += 1
        ret["succes"] = True
        return [True, ret, 500]


    def __query(self, lang, query, id):
        url = "https://api.dialogflow.com/v1/query?v=20150910"
        url += "&lang=" + str(lang)
        url += "&query=" + urllib.parse.urlencode(query)
        url += "&sessionId=" + str(id)
        res = requests.get(url, headers={'Authorization': 'Bearer ' + self.bearer})
        if res.status_code != 200:
            return [False, "invalid bearer ", 401]
        return [True, JSON.loads(res.text)["result"]["fulfillment"]["speech"], None]
