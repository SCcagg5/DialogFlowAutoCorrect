new Vue({
    el: '#app',
    data: {
      error : null,
      success: null,
      lastexo: null,
      bearer: null,
      exercice: null
    },
    methods: {
      correct: function(){
        if (!this.bearer || !this.exercice)
          return;
        this.lastexo = this.exercice;
        this.ajaxRequest = true;
        data = {
          "bearer": this.bearer,
	        "exercice": this.exercice
        }
        url = "http://localhost:5002/correct/"
        axios.post(url, data)
             .then(response => {this.setup_return(response.data.data, response.data.data.succes)})
             .catch(error => console.log(error));
      },
      setup_return: function(response, suc) {
        this.success= suc
        delete response.succes
        this.error["errorcode"] = "WGW"
        this.error = JSON.stringify(response, undefined, 2).replace(/\n/g, '<br>');
        this.error = "<pre>" +this.error+ "</pre>"
        localStorage.history = true;
        localStorage.bearer = this.bearer;
        localStorage.success = this.success;
        localStorage.error = this.error;
        localStorage.exercice = this.exercice;
      }
    },
    mounted(){
      if(localStorage.history) {
      this.bearer = localStorage.bearer;
      this.success = JSON.parse(localStorage.success);
      this.lastexo = localStorage.exercice;
      this.error = localStorage.error
      }
    }
})
