var modern_thread = angular.module('modern_thread', ['ngRoute', 'ngAnimate']);

modern_thread.controller('modern_controller', function($scope, $http){
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
});

