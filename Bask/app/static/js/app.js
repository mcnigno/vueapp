
/*
Vue.component('code-item', {
    // The todo-item component now accepts a
    // "prop", which is like a custom attribute.
    // This prop is called todo.
    props: ['codeitem'],
    template: '<div class="card mb-4 box-shadow"><h1 class="card-title">{{ codeitem.catname }} {{ codeitem.code }} </h1></div>'
  })

  Vue.component('code-composer', {
    // The todo-item component now accepts a
    // "prop", which is like a custom attribute.
    // This prop is called todo.
    props: ['code'],
    template: '<div class="card mb-4 box-shadow"><h1 class="card-title">{{ code.catname }}{{ code.id }} </h1><p> row msg {{this.message}}</p></div>'
  })

var app = new Vue({
    el: '#app_',
    data: {
        
        message: '',
        units: [],
        fabunits: [],
        doctypes: [],
        codeItems: [],
        codeComposer: [],
        

        computed: {
          itemsCount () {
              // itemsFilters is computed 
              return this.itemsFilters.length
              // or a method
              return this.itemsFilters().length
            }
          },
        
      },
    delimiters: ['[[',']]'],
    methods: {
        
          getCodeItem() {
            const path = 'http://localhost:8080/codeitemview/api/read';
            axios.get(path)
              .then((res) => {
  
                this.codeItems = res.data.result;
              })
              .catch((error) => {
                // eslint-disable-next-line
                console.error(error);
              });
          },
          getCodeComposer() {
            const path = 'http://localhost:8080/codecomposerview/api/read';
            axios.get(path)
              .then((res) => {
  
                this.codeComposer = res.data.result;
              })
              .catch((error) => {
                // eslint-disable-next-line
                console.error(error);
              });

          },
          checkCode(item) {
            console.log('CheckCode Function',item.id);
            
            //console.log(this.message);
            //console.log(this.codeComposer);
            console.log(this.codeItems[item.id-1].composerpos, item.composerpos) ;
            /*
            this.codeComposer.forEach(element => {
              //console.log(element)
              var tmpcode = this.message.split('-')[element.position-1];
              console.log(element.position) ;
              //console.log(item.composerpos) ;
              console.log(this.codeItems[item.id].composerpos) ;
              //console.log(this.codeItems[100]);
              //console.log(element.position);
              
            });
              
          },
          checkCode2() {
            console.log( $( ".codeitems" ).length === this.codeComposer.length );
            
          }

      },
      created() {
        
        this.getCodeItem();
        this.getCodeComposer();
      },
  });


Vue.component('code-field', {
  props: ['field'],
  templates: '<input id="inputcode" v-model="message" class="form-control form-control-lg" type="text" placeholder="Type Your Code">'
});
*/
var app = new Vue({
  el: '#app2',
  delimiters: ['[[',']]'],

  data: {
    codeComposer : []
  },

  methods: {
    getCodeComposer () {
      const path = 'http://localhost:8080/codecomposerview/api/read';
      axios.get(path)
        .then((res) => {this.codeComposer = res.data.result;})
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });

    },
    checkCode () {
      
      const path = 'http://localhost:8080/codecomposerview/api/read?_flt_0_code=A';

    }

  }
});
