define(['$','_','Backbone'],function(require,exports){

	var App= exports.App || {};
	
	 App.Model=App.Model || {};
	 App.View=App.View || {};
	 App.Collection=App.Collection || {};
	 App.Routers=App.Routers || {};

	App.Model.User = Backbone.Model.extend({

		defaults:{

			nickName:'',
			loginState:false,
		},

		initialize:function(){

			this.bind('click user-action-quite',doQuite);


		},

		doQuite:function(event){

			if(!this.get('loginState')){

				var mkcert = confirm("确定退出吗？");

				if(mkcert){

					// 删除 COOKIE 登录状态的字符串

					$.cookie("login_sid", null, { path: '/' }); 

				}


			}


		}


	})

// article model  defaults title and desc shortcut , owner identify , article id

	App.Model.Article = Backbone.Model.extend({

		defaults:{

			npic:'' ,// 显示头像

			nickName:'',//昵称

			timeMap:'',// 创建时间

			title:'' ,//文章标题

			identity:'',  //文章ID

			desc:'' ,	//正文表述 截取

			owner:'',//所有者ID

			typeId:'' //文章前端显示类型

		},

		initialize:function(){




		}



	});

	App.View.Article = Backbone.View.extend();




// inheritance object



	App.View.Panel = Backbone.View.extend({

		

			_abb:'Article',

		initialize:function(options){

			console.log('Panel initialize');

			this.foo = 'bar';

		}
	});

	App.View.PanelAdvanced = App.View.Panel.extend({

		

	_abb:'ArticlePhoto',
		
		initialize:function(options){

			App.View.Panel.prototype.initialize.call(this,[options]);
			this.foo= 'cc';
			console.log('PanelAdvanced initialize');
			console.log(this.foo);

		}

	});

	App.View.PanelAdvancedExtra = App.View.PanelAdvanced.extend({

	

		_abb:'Album',

		initialize:function(options){

			App.View.PanelAdvanced.prototype.initialize.call(this,[options]);

			console.log('PanelAdvancedExtra initialize');



		}

	});

	var ff = new App.View.Panel();
	var ss = new App.View.PanelAdvanced();
	var gg = new App.View.PanelAdvancedExtra();
console.log(ff);
console.log(ss);
console.log(gg);



	// ** inhert another way 

	App.View.NPanel  = function(options){

		console.log('Panel initialize');

		this.foo = 'bar';

		Backbone.View.apply(this,[options]);


	}


	_.extend( App.View.NPanel.prototype , Backbone.View.prototype,{

		sayHi:function(){

			console.log('hello from Panel');

	}
});

	App.View.NPanel.extend = Backbone.View.extend;

	App.View.NPanelAdvanced=App.View.NPanel.extend({

		initialize:function(options){

			console.log('APP VIEW NPanelAdvanced initialize');

			console.log(this.foo);

		}


	});

	var www_1= new App.View.NPanel({foo:'ssbb'});

	var www_2= new App.View.NPanelAdvanced();
	www_1.sayHi();
	www_2.sayHi();
	

});