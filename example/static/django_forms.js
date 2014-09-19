angular.module('django_forms', [])
  .factory('Form', ['$resource', function ($resource) {
    return $resource('/_forms/', null,
      {
        'list': { method: 'GET' }
      });
  }])

  .directive('charfield', function () {
    return {
      restrict: 'E',
      // declare the directive scope as private
      scope: {
        form: '='
      },
      templateUrl: 'static/partials/char_field.html'
    }
  })

  .directive('datefield', function () {
    return {
      restrict: 'E',
      // declare the directive scope as private
      scope: {
        form: '='
      },
      templateUrl: 'static/partials/date_field.html'
    }
  })

  .directive('djangoform', function () {
    return {
      restrict: 'E',
      scope: {
        form: '='
      },
      templateUrl: 'static/partials/django_form.html'
    }
  });