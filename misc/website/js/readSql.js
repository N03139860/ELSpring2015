// var xhr = new XMLHttpRequest();
// xhr.open('GET', '../../local.db', true);
// xhr.responseType = 'arraybuffer';
//
// var $dataSet = null;
//
// xhr.onload = function(e) {
// dbCallback(this.response);
// };
// xhr.send();
//
// function dbCallback(response){
// var uInt8Array = new Uint8Array(response);
// var db = new SQL.Database(uInt8Array);
// var contents = db.exec("SELECT * FROM temperature");
// $dataSet = contents[0].values;
// }

var app = angular.module('app', []).controller('IndexController', ['$scope', '$http', '$templateCache',
function($scope, $http, $templateCache) {
  $http.get('temperatures-db.php').success(function(data, status, headers, config) {
    $scope.data = data;
  }).error(function(data, status, headers, config) {
    console.log("Some error ocurried while trying to get db contents from php.");
  });
}]);

$(document).ready(function() {
    $('#temperatureTable').dataTable();
} );

// $(document).ready(function() {
//
  // $('#demo').html('<table cellpadding="0" cellspacing="0" border="0" class="display" id="example"></table>');
//
  // $('#example').dataTable({
    // "data" : $dataSet,
    // "columns" : [{
      // "title" : "Datetime"
    // }, {
      // "title" : "Celsius"
    // }, {
      // "title" : "Farenheit"
    // }]
  // });
// });