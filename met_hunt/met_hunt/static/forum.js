var modern_thread = angular.module('modern_thread', ['ngRoute', 'ngAnimate', 'ngCookies']);

modern_thread.controller('modern_controller', function($scope, $http, $cookies){
	$http.get('load_data/')
		 .success(function(data){
		 	$scope.posts = data.json;
		 	$scope.templateurl = "modern/"
		 	$scope.title = "Modern Hunt"
		 });

	$scope.create = function(){
		$scope.templateurl = "create/"
		$scope.title = "Create Post"
	}

	$scope.submit = function(){
		$http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
		$http({
			method : "POST",
			url : "submit/",
			data : "test=data"
		})
			 .success(function(data){
			 	alert("succeed!");
			 });
	}

});

