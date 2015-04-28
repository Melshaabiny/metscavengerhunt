var modern_thread = angular.module('modern_thread', ['ngRoute', 'ngAnimate', 'ngCookies']);
modern_thread.config(function($locationProvider){
	$locationProvider.html5Mode({
		enabled:true,
		requireBase:false
	});
});
modern_thread.controller('modern_controller', function($scope, $http, $cookies, $location){
	var load = function(){
		$scope.posts = {}
		$http.get('load_data/')
			 .success(function(data){
			 	$scope.posts = data.json;
			 	$scope.templateurl = "modern/"
			 	$scope.title = "Modern Hunt"
			 });		
	}
	load();

	$scope.create = function(){
		$scope.templateurl = "create/"
		$scope.title = "Create Post"
	}

	$scope.submit = function(data){
		//assume that is at least one post data.
		data['username'] = $scope.posts[0]['logged_user'];
		data['thread'] = $scope.posts[0]['thread'];
		$http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
		$http({
			method : "POST",
			url : "submit/",
			data : data })
			 .success(function(data){
			 	load();
			 });

	}

});

