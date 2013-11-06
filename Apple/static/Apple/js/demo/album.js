define('album',function(require,exports){

	var $ = require('base/jquery');
	var _= require('base/underscore-min');
	var Backbone = require('base/backbone-min');

	require("/base")

	
	var App= exports.App || {};
	
	 App.Model=App.Model || {};
	 App.View=App.View || {};
	 App.Collection=App.Collection || {};
	 App.Routers=App.Routers || {};

	App.Model.Album = App.Model.Item.extend({});


	App.Model.Album.prototype.initialize=function(options){


		
	}

	App.View.Item = Backbone.View.extend( {tagName:'div',tpler:'',events:{}} );


	App.View.Album = App.View.Item.extend( { tpler:_.template( $('#album_tpl').html() ) ,events:{'click .photo-cell','click .action':'action_bar'} } );


	App.View.Album.prototype.action_bar=function(event){



	}

});