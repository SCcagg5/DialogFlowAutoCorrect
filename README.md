# **DialogFlow** unary tests app

## Route:  
  
Route| Method| Content Type |Parameters| Description |
-----|-------|--------------|----------|-|
/test/ | POST, GET |  |  | return an empty response pattern
/correct/ | POST | JSON | bearer, exercice| return data **waited** and **got** until error if there is one
/add_exo/\<mail\>/\<name\>/ | POST | multipart | upload | return **upload** converterd into exercice array, link to git uploaded version and exercice number

### Parameters:
```javascript
{ 
  "bearer" : "*YOUR_DIALOGFLOW_BEARER*",
  "exercice": "*EXERCICE_NUMBER*",
  "upload": YOUR_FILE.csv
} 
```
### Return example:

:::succes

**`/correct/` True**
```javascript
{
    "succes": true,
    "queryInfos": {
        "route": "/correct/",
        "params": {
            "exercice": "354b876f4b404af2abc6e0b0d6b06f45",
            "bearer": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        }
    },
    "error": null,
    "data": {
        "succes": true,
        "got": [
            "Bonjour !"
        ],
        "waited": [
            [
                "Bienvenue !",
                "Salutations !",
                "Salut !",
                "Bonjour !"
            ]
        ]
    },
    "status": 200
}
```
:::


:::danger
**`/correct/` False**
```javascript
{
    "succes": true,
    "queryInfos": {
        "route": "/correct/",
        "params": {
            "exercice": "354b876f4b404af2abc6e0b0d6b06f45",
            "bearer": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        }
    },
    "error": null,
    "data": {
        "succes": false,
        "got": [
            "Hello"
        ],
        "waited": [
            [
                "Bienvenue !",
                "Salutations !",
                "Salut !",
                "Bonjour !"
            ]
        ]
    },
    "status": 200
}
```
:::

:::succes
**`/add_exo/` True**
```javascript
{
    "succes": true,
    "status": 200,
    "error": null,
    "queryInfos": {
        "params": {
            "name": "eliot courtel"
        },
        "route": "/add_exo/<mail>/<name>/"
    },
    "data": {
        "link": "https://github.com/SCcagg5/DialogFlowModule/blob/master/exo354b876f4b404af2abc6e0b0d6b06f45.json",
        "number": "354b876f4b404af2abc6e0b0d6b06f45",
        "exercice": {
            "fr": {
                "value": [],
                "queries": [
                    [
                        "Bonjour",
                        "Salut"
                    ]
                ],
                "waited": [
                    [
                        "Bienvenue !",
                        "Salutations !",
                        "Salut !",
                        "Bonjour !"
                    ]
                ]
            }
        }
    }
}
```
:::


## Launching the App:  
  

 * `docker build -t dialogCorrect_img .`
 * `docker run --detach --name dialogCorrect -p5000:5000 -it dialogCorrect_img`

## More
* To get More info about available exercice, see here : https://github.com/SCcagg5/DialogFlowModule
* To get correction for the first exercice, your `EXERCICE_NUMBER` will be `354b876f4b404af2abc6e0b0d6b06f45`
* To upload a new exercice it'll have to be formated:

  #|lang|queries|queries|waited|waited|value|
  -|-|-|-|-|-|-|
  1st test |your_lang | query_1 | query_2 | waited_pos1 |waited_pos2|value_get1|
  
  - *Here when inputing to dialogflow in language `your_lang` ('fr' / 'us') dialogflow will expect one of the waited possibilities and all value set to be retrieve*
  - *You can leave queries, waited and value empty to not be computed*
  - *One lang column, as many queries, waited, value as you want*

## Curl examples
```shell
curl -X POST http://localhost:5000/correct/ 
        -H 'Content-Type: application/json' 
        -d '{ 
          "bearer" : "YOUR_DIALOGFLOW_BEARER", 
          "exercice": "EXERCICE_NUMBER"
        }';

curl -X POST 'http://localhost:5000/add_exo/mail/name/' \
        -H 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
        -F 'upload=@YOUR_FILE.csv';
```
