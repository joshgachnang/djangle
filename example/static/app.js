'use strict';

// Declare app level module which depends on views, and components
angular.module('example', [
  'ngResource',
  'django_forms',
])
  .controller('ExampleCtrl', ['$scope', '$http', 'Form', function ($scope, $http, Form) {
    $scope.submit = function() {
      var formData = {};
      for (var field in $scope.todo.fields) {
        formData[field] = $scope.todo.fields[field].value;
        $scope.todo.fields[field].value = null;
      }
      console.log('Submitting', formData);
      $http.post('/api/todos/', formData);
    };

    var forms = Form.list();
    forms.$promise.then(function(result) {
      $scope.todo = result.todo;
    })

  }]);