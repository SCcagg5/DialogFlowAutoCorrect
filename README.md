# **DialogFlow** unary tests app

## Route:  
  
Route| Method| Content Type |Parameters| Description |
-----|-------|--------------|----------|-|
/test/ | POST, GET |  |  | return an empty response pattern
/correct/ | POST | JSON | bearer, exercice| return data **waited** and **got** until error if there is one

### Parameters:
```javascript
{ "bearer" : "*YOUR_DIALOGFLOW_BEARER*","exercice": "*EXERCICE_NUMBER*" } 
```
### Return example:
**True**
```javascript
{
    "succes": true,
    "queryInfos": {
        "route": "/correct/",
        "params": {
            "exercice": "1",
            "bearer": "2f5583ceb8904df4a35d434a139709b2"
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

**False**
```javascript
{
    "succes": true,
    "queryInfos": {
        "route": "/correct/",
        "params": {
            "exercice": "1",
            "bearer": "2f5583ceb8904df4a35d434a139709b2"
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

## Launching the App:  
  

 * `docker build -t dialogCorrect_img .`
 * `docker run --detach --name dialogCorrect -p5000:5000 -it dialogCorrect_img`

## More
* To get More info about available exercice, see here : https://github.com/SCcagg5/DialogFlowModule
* To get correction for the first exercice, your `EXERCICE_NUMBER` will be `1`

## crul exemple
```shell
curl -X POST http://localhost:5000/correct/ 
        -H 'Content-Type: application/json' 
        -d '{ 
          "bearer" : "YOUR_DIALOGFLOW_BEARER", 
          "exercice": "EXERCICE_NUMBER"
        }'
```
