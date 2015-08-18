var app = angular.module('ChatBot', ['ngCookies']);

app.config(function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
});

app.controller('ChatScreen',['$scope','$http','$cookies',
function($scope,$http,$cookies){
   $http.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
   $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
   $scope.chats=[{'message':"Hello, welcome to GEARS chat bot",'uid':0},{'message':"Whazzup",'uid':0}];
   $scope.addchat=function(){
   	    var newchat={'message':$scope.newchat,'uid':1};
   		$scope.chats.push(newchat);
   		var in_data = jQuery.param({'content': $scope.newchat,'csrfmiddlewaretoken': $cookies.csrftoken});
   		var url='http://127.0.0.1:8000/livechatbot';
   		var my_data={test: 'data'};
   		$http.post(url, in_data)
          .success(function(out_data) {
            // Reset the form in case of success.
            $scope.chats.push(out_data);
        });
   };
}]);