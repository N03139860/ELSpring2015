
var app = angular.module('app', []).controller('IndexController', ['$scope', '$http', '$templateCache',
function($scope, $http, $templateCache) {
  $http.get('temperatures-db.php').success(function(data, status, headers, config) {
    $scope.data = data.reverse();
  }).error(function(data, status, headers, config) {
    console.log("Some error ocurried while trying to get db contents from php.");
  });
}]);