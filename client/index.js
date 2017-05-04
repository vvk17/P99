/* global angular, nodered, express, openwhisk */

angular.module('template', [])
.controller('MainCtrl', function($scope, $http){
    // BEGIN CODE HERE
   $scope.x = 3;
   $scope.y = "sponge bob";
   $scope.nums = [4,5,6,7];
   $scope.expr = 5+8;
   $scope.expr_01 = "5"+"8";
   $scope.id_01 = ["раз","два","три","четыре"];

    $scope.add = function() {
       $scope.nums.push($scope.numb);
   };

  $scope.addone = function() {
    $scope.id_01.push($scope.idchr);
   };

   $scope.twitch = function() {
     $http.get('https://api.twitch.tv/kraken/games/top?client_id=e9amddb6brnearv3y2w60udmrurr6m')
     .then(function(rsp){
       $scope.games = rsp.data.top;
       console.log($scope.games);
     });
   };

    // END CODE
});
