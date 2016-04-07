angular.module('quiickly.services', ['ngStorage'])

.factory ('StorageUbication', function ($localStorage) {

  $localStorage = $localStorage.$default({
    dataU: []
  });

  var _getAll = function () {
    return $localStorage.dataU;
  };

  var _add = function (dataa) {
    $localStorage.dataU.push(dataa);
  }

  var _remove = function (dataa) {
    $localStorage.dataU.splice($localStorage.dataU.indexOf(dataa), 1);
  }

  var _getLast = function (dataa) {
    return $localStorage.dataU.slice(-1)[0];
  }

  var _getPen = function (dataa) {
    return $localStorage.dataU.slice(-2, -1)[0];
  }

  return {
      getAll: _getAll,
      add: _add,
      remove: _remove,
      getLast: _getLast,
      getPen: _getPen
    };
})

.factory ('StorageProfile', function ($localStorage) {

  $localStorage = $localStorage.$default({
    dataP: []
  });

  var _getAll = function () {
    return $localStorage.dataP;
  };

  var _add = function (dataPr) {
    $localStorage.dataP.push(dataPr);
  }

  var _remove = function (dataPr) {
    $localStorage.dataP.splice($localStorage.dataP.indexOf(dataPr), 1);
  }

  var _getLast = function (dataPr) {
    return $localStorage.dataP.slice(-1)[0];
  }

  var _getPen = function (dataPr) {
    return $localStorage.dataP.slice(-2, -1)[0];
  }

  return {
      getAll: _getAll,
      add: _add,
      remove: _remove,
      getLast: _getLast,
      getPen: _getPen
    };
})

.service('serviceProduct', function ($http, $q) {
  var urlProducts= 'http://localhost:1337/quiickly.co/api/v1/products/?format=json';

  return {
    getProducts: getProducts
  }

  function getProducts (){
    var defered = $q.defer()
    var promise = defered.promise;

    $http.get(urlProducts)
      .success(function(products){
        defered.resolve(products);
      }).error(function(err){
        defered.reject(err)
      })
    return promise;
  }
});
