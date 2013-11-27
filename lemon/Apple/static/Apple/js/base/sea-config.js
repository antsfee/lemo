seajs.config({

	base:"./static/Apple/js/" ,
    // 设置路径，方便调用
    /*path:{
    	'jQueryv1.9.1.min':'jQueryv1.9.1.min',
        'undersocre':'underscore-min',
        'Backbone':"backbone-min"
    },*/
    alias:{
    'jquery':"../base/jquery",
    '$':"../base/jquery",
    'underscore':'../base/underscore-min',
    '_':'../base/underscore-min',
    'json2':'../base/json2',
    'Backbone':"../base/backbone-min",
    'Backbone.LocalStorage':"../base/backbone-localstorage.js"
    }

})