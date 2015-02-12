var xhr = new XMLHttpRequest();
xhr.open('GET', '../../local.db', true);
xhr.responseType = 'arraybuffer';

var $data = null;

xhr.onload = function(e) {
  var uInt8Array = new Uint8Array(this.response);
  var db = new SQL.Database(uInt8Array);
  var contents = db.exec("SELECT * FROM temperature");
  $data = contents[0].values;
};
xhr.send();

var app = angular.module('app', [])
  .controller('IndexController', ['$scope', function($scope) {
  $scope.data = $data;

}]);
