# **DialogFlow** unary tests app

## Route:  
  
Route| Method| Content Type |Parameters|
-----|-------|--------------|----------|
/correct/ | POST | JSON | { "bearer" : "*YOUR_DIALOGFLOW_BEARER*","exercice": "*EXERCICE_NUMBER*" }|


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
