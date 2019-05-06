# **DialogFlow** unary tests app

[![CodeFactor](https://www.codefactor.io/repository/github/sccagg5/dialogflowautocorrect/badge)](https://www.codefactor.io/repository/github/sccagg5/dialogflowautocorrect)
[![codebeat badge](https://codebeat.co/badges/d6039fda-1105-46b6-8edc-9583b6d697b4)](https://codebeat.co/projects/github-com-sccagg5-dialogflowautocorrect-master)
[![BCH compliance](https://bettercodehub.com/edge/badge/SCcagg5/DialogFlowAutoCorrect?branch=master)](https://bettercodehub.com/)

# The App:

To launch the app use: `docker-compose up -d --build` from inside the git directory

 * *There is two mode **PROD** and **DEV** :*
   * _**PROD** clone and run the actual git repo_
   * _**DEV** is using your locals files to run_
 * *By default, the mode is set to **PROD** in the `docker-compose.yml` file, to change it set `- PROD=1` to `- PROD=0`*

### Next features:

 * Add variable value check
 * Return error code
 * Add setting file
 * error code doc

### Tech :
 
  * **APP**: Docker
  * **FRONT**: VueJS
  * **END**: Python3
  
  
---

# Front End:

### Launching the App:

From inside the `front-end` dir:

 * `docker build -t dialogcorrect_front_img .`
 * `docker run --detach --name dialogcorrect -p80:8080 -it dialogcorrect_front_img`


---

# Back end:

### Route:  

Route| Method| Content Type |Parameters| Description |
:-|:-:|:-:|:-:|:-|
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

### Launching the App:  

From inside the `back-end` dir:

 * `docker build -t dialogcorrect_back_img .`
 * `docker run --detach --name dialogCorrect -p5000:8080 -it dialogcorrect_back_img`

---

# More

* To get More info about available exercice, see here : https://github.com/SCcagg5/DialogFlowModule
* To get correction for the first exercice, your `EXERCICE_NUMBER` will be `354b876f4b404af2abc6e0b0d6b06f45`
* To upload a new exercice it'll have to be formated:

  #|lang|queries|queries|waited|waited|value|
  :-:|:-:|:-:|:-:|:-:|:-:|:-:|
  1st test |your_lang | query_1 | query_2 | waited_pos1 |waited_pos2|value_get1|

  - *Here when inputing to dialogflow in language `your_lang` ('fr' / 'us') dialogflow will expect one of the waited possibilities and all value set to be retrieve*
  - *You can leave queries, waited and value empty to not be computed*
  - *One lang column, as many queries, waited, value as you want*
