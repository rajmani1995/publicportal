var app = angular.module('ChatBot', []);

app.controller('ChatScreen',['$scope',
function($scope){
   $scope.chats=["Hello, welcome to GEARS chat bot"];
   $scope.addchat=function(){
   		$scope.chats.push($scope.newchat);
   }
}]);