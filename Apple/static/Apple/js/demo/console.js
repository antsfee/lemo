define('console',function(require,exports){
	
    exports.log=function(msg){
    
    	if(window.console && console.log){
        
            console.log(msg);
        
        }else{
        
        alert(msg);
        
        }
        
    };


	 // __________________________________________________________

	   Person = Backbone.Model.extend({
                  
                  defaults:{
              	
                  	name:'fetus',
              		age:0,
                  	children:[]
              
              		},
              
                  initialize:function(){
                  
                  //alert("Welcome to this world!");
                  
                  this.bind("change:name",function(){
                  
                  	var nameb = this.get("name");
                      
                    var childrens = this.get("children");
                      
                     /* if(typeof name =='object'){
                      
                          for(var i in name){
                          
                              console.log("i : "+name);
                              console.log("i valueis : "+name[i]);
                          
                          }
                      
                      }*/
                      
                  //   alert("change my name to"+nameb['name']);
                      
                     console.log(this.name);
                      console.log(childrens[0]);
                  
                  	});
                      
                  },
                      
                   replaceNameAttr:function(name){
                    this.set({name:name});
                    
                    
                    }
              
              });
              
            var person = new Person({name:'3223',age:23,children:['Ryan']});
            
            person.replaceNameAttr({name:'stewie Griffin'});
            
              SearchView = Backbone.View.extend({
              
                  initialize:function(){
                  
                  	//alert('Alerts suck');
                    this.render();
                  
                  }
                  ,
                  render:function(){
                  	// Compile the template using underscore
                      console.log("current underscore : "+_);
                      var variables = {search_label:"My Search"};
                  var template = _.template($('#search_tpl').html(),variables);
                      console.log(template);
                  $(this.el).html(template);
                  
                  }
                  ,
                  events:{
                  	
                      "click input[type=button]":"doSearch"
                  
                  }
                  ,
                  doSearch:function(event){
                  
                  alert("search for : " + $('#search_input').val());
                  
                  
                  
                  }
              
              
              });
              
              var search_view= new SearchView({el:$('#search_container')});
              
              var Song = Backbone.Model.extend({
              
              	defaults:{
              
                  		name:"NO",
                  		artist:"NO"
                  
              			},
                                               
                 initialize:function(){ console.log("music answer"); }
                    
              
              });
            
            var Album = Backbone.Collection.extend({
            
            model:Song
            
            		});
            
            var song1=new Song({name:"N1",artist:"A1"});
            var song2=new Song({name:"N2",artist:"A2"});
            var song3=new Song({name:"N3",artist:"A3"});

        var myAl= new Album([song1,song2,song3]);
        
        
           		console.log(myAl.models);




              var ff =Backbone.Model.extend({

                defaults:{

                  title:'txt',
                  named:'name'

                } ,


                initialize:function(){

                  this.bind('click name',modifyName);


                },

                modifyName:function(){

                  console.log('modify name');


                }


              })


              var son = Backbone.Model.extend({




              });

    //________________________________________________________________-------------




});