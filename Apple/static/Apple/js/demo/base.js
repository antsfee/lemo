define('base',function(require,exports){

var App= exports.App || {};
	
	 App.Model=App.Model || {};
	 App.View=App.View || {};
	 App.Collection=App.Collection || {};
	 App.Routers=App.Routers || {};

	App.Model.Item = Backbone.Model.extend({title:'1',userId:'2',userPic:'3'});

});