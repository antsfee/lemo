define(function(require,exports){

	
	var $ = require('base/jquery');
	var _= require('base/underscore-min');
	var Backbone = require('base/backbone-min');
	console.log();
	
	var App= exports.App || {};
	
	 App.Model=App.Model || {};
	 App.View=App.View || {};
	 App.Collection=App.Collection || {};
	 App.Routers=App.Routers || {};


	 // App.Model.Item is ancient node of the Article , MArticle, Album  as the same time ! It is a cell for show 

	App.Model.Item = Backbone.Model.extend({title:'1',userId:'2',userPic:'3'});

	

	App.Model.Article = App.Model.Item.extend(
		{
		  desc:'>>>>>>>><<<<<<<<',
		  createtime:'0000-00-00',
		  type:'0'
		}

	);

	App.Collection.Article= Backbone.Collection.extend({

		model:App.Model.Article,

		url:'/Articles',

		getIds:function(){

			return _(this.model).map(function(model){

				return model.id;

			}).join(',');

		},

		createAll:function(options){

			return Backbone.sync.call(this,'create',this,options);

		},

		updateAll:function(options){

			return Backbone.sync.call(this,'update',this,options);

		},


		deleteAll:function(options){

			return  Backbone.sync.call(this,'delete',this, _.extend({url:this.url+'/'+this.getIds()},options));

		}



	});









	

	

	


var demoA = new App.Model.Article;

console.dir(demoA);
/*
console.log(demoA.title);
console.log(demoA.desc);*/

App.View.Item = Backbone.View.extend(

	{
		tagName:'div',
		tpler:''
	}
);



	// app item article inherits base view  set attribute

	App.View.Article = App.View.Item.extend( 

		{

			
		 tpler:_.template( $('#article_tpl').html() ) ,

		 events:{'click .action':'action_bar'} ,

		 action_bar:function(event){

		},


		// 构造方法
		initialize:function(options){


			this.render();

		},


		render:function(){



			
		}

	}

);

	
	

var viewA = new App.View.Article;

console.dir(viewA);


	// Ablum Model typeId 2   the type controll the show template 


	App.Model.Album = App.Model.Item.extend();


	App.Model.Album.prototype.initialize=function(options){

		
	}



	
	
// album 相册 定义

	

	var album = new App.Model.Album;


	// app item base view  set attribute



	App.View.Album = App.View.Item.extend( 

		{ 

			tpler:_.template( $('#album_tpl').html() ) ,

			events:{'click .photo-cell':'wget-show','click .action':'action_bar'} 


		}

	 );


	App.View.Album.prototype.action_bar=function(event){



	}




//  router  
/*
通过 backbone 自动开启 全局 路径监听  开启history 配合每个 模块以及集合中的URL路径配置来

操纵restful */

App.Routers.Main = Backbone.Router.extend({

	routes:{
		"":'index',
		"articles/":'getArticles',
		"article/:articleId":"getArticle",
		"*error":"fourOfour"

	},

	index:function(){

		// home page


	}
	,

	getArticle:function(articleId){

		// get the all info  of article by articleId

	},

	getArticles:function(){

		// a list of articles

	},

	fourOfour:function(error){

		// 404 page

	}


	});



// 

 var router = new App.Routers.Main();
    Backbone.history.start({pushState : true});


});