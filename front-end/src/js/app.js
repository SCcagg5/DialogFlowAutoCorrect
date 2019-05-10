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
        this.exercice = this.exercice.trim().replace(/exo/g, '').replace(/\.json/g, '')
        this.lastexo = this.exercice;
        this.ajaxRequest = true;
        data = {
          "bearer": this.bearer,
	        "exercice": this.exercice
        }
        url = "http://localhost:5002/correct/"
        axios.post(url, data)
             .then(response => {this.setup_return(response.data)})
             .catch(error => console.log(error));
      },
      setup_return: function(response) {
        if (response.status != 200){
        this.success = false;
        this.error = JSON.stringify(response.error, undefined, 2).replace(/\n/g, '<br>');
        this.error = "<pre>" +this.error+ "</pre>"
        return;
        }

        this.success = response.data.succes
        console.log(response);
        delete response.data.succes
        response.data["errorcode"] = "WGW"
        this.error = JSON.stringify(response.data, undefined, 2).replace(/\n/g, '<br>');
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
      this.exercice = this.lastexo;
      this.error = localStorage.error
      }
    }
})
