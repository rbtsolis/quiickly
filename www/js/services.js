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

.factory('serviceProduct', function ($http, $q) {
  var urlProducts= 'http://localhost:1337/quiickly.co/api/v1/products/?format=json';
  var urlOrder = ''

  return {
    getProducts: getProducts,
    postOrder: postOrder
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

  function postOrder (){
    // POST de orden

    $http({
      url: urlOrder,
      method: "POST",
      data: JSON.stringify({
        address: $scope.dataAddress,
        latitude: $scope.latOrder,
        longitude: $scope.lngOrder,
        pay_method: 1,
        user: $scope.mailUser,
        branch_office: 1,
        quiickler: $scope.mailUser,
        product: 1
      }),
      headers: {'Content-Type': 'application/json', 'Authorization': 'Token 8c3444e5f1718201985db0fb5cb4af1366208886'}
      }).success(function (response, error, status, headers, config) {
        $state.go('app.inservice')
      }).error(function (data, error, status, headers, config) {
        console.log("no funciona" + '' + error);
      });
  }
})

.factory('serviceLoginRegister', function ($$http, $q){
  var urlLogin = ''
  var urlRegister = ''

  return {
    postLogin: postLogin,
    postRegister: postRegister
  }

  function postLogin (){

  }

  function postRegister (){

  }
})

.factory('serviceUser', function ($http, $q){
  var urlAddress = 'http://localhost:1337/www.mocky.io/v2/5708278d13000010007237a6'
  var urlProfile = ''

  return {
    getAddress: getAddress,
    postAddress: postAddress,
    getProfile: getProfile,
    postCreditCard: postCreditCard,
    postPromoCode: postPromoCode
  }

  function getAddress (){
    var defered = $q.defer()
    var promise = defered.promise;

    $http.get(urlAddress)
      .success(function(addresses){
        defered.resolve(addresses);
      }).error(function(err){
        //console.log(addresses);
        defered.reject(err)
      })
    return promise;
  }

  function postAddress (){

  }

  function getProfile (){

  }

  function postCreditCard (){

  }

  function postPromoCode (){

  }

})

.factory('InService', function ($$http, $q){
  var urlService = ''

  return {
    getInfoService: getInfoService,
    postCancel: postCancel
  }

  function getInfoService (){

  }

  function postCancel (){

  }

})
