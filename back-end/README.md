Docker service used to do unitary tests on your **DialogFlow** app

Route| Method| Content Type |Parameters|
-----|-------|--------------|----------|
/correct/ | POST | JSON | { "bearer" : "*YOUR_DIALOGFLOW_BEARER*","exercice": "*EXERCICE_NUMBER*" }|
	
* To get More info about available exercice, see here : https://github.com/SCcagg5/DialogFlowModule
* To get correction for the first exercice, your `*EXERCICE_NUMBER*` will be `1`

```
curl -X POST http://localhost:5001/correct/ 
        -H 'Content-Type: application/json' 
        -d '{ 
          "bearer" : "*YOUR_DIALOGFLOW_BEARER*", 
          "exercice": "*EXERCICE_NUMBER*"
        }'
```
