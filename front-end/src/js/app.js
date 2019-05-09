new Vue({
    el: '#app',
    data: {
      error : null,
      success: null,
      lastexo: null,
      bearer: null,
    },
    methods: {
      correct: function(){
        this.ajaxRequest = true;
        data = {
          "bearer": this.bearer,
	        "exercice": this.exercice
        }
        url = "http://localhost:5002/correct/"
        axios.post(url, data)
             .then(response => {console.log(response)})
             .catch(error => console.log(error));
      }
    }
})
