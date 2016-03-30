angular.module('quiickly.controllers', [])

.controller('AppCtrl', function($scope, $ionicModal, $timeout) {

  // With the new view caching in Ionic, Controllers are only called
  // when they are recreated or on app start, instead of every page change.
  // To listen for when this page is active (for example, to refresh data),
  // listen for the $ionicView.enter event:
  //$scope.$on('$ionicView.enter', function(e) {
  //});

  // Form data for the login modal
  $scope.loginData = {};

  // Create the login modal that we will use later
  $ionicModal.fromTemplateUrl('templates/login.html', {
    scope: $scope
  }).then(function(modal) {
    $scope.modal = modal;
  });

  // Triggered in the login modal to close it
  $scope.closeLogin = function() {
    $scope.modal.hide();
  };

  // Open the login modal
  $scope.login = function() {
    $scope.modal.show();
  };

  // Perform the login action when the user submits the login form
  $scope.doLogin = function() {
    console.log('Doing login', $scope.loginData);

    // Simulate a login delay. Remove this and replace with your login
    // code if using a login system
    $timeout(function() {
      $scope.closeLogin();
    }, 1000);
  };
})

.controller('MenuCtrl', function($scope) {

})

.controller('CreditCtrl', function($scope, $ionicModal){

})

.controller('ProductoCtrl', function($scope, $ionicModal){

})

.controller('MapCtrl', function($scope, $http, $state, $cordovaGeolocation, $ionicModal) {

  $ionicModal.fromTemplateUrl('templates/producto.html', {
    scope: $scope,
    animation: 'slide-in-up',
    focusFirstInput: true
  }).then(function(modalProducto) {
    $scope.modal = modalProducto
  })

  $scope.openProduct = function() {
    $scope.modal.show()
  }


  $ionicModal.fromTemplateUrl('templates/producto.html', {
    scope: $scope,
    animation: 'slide-in-up',
    focusFirstInput: true
  }).then(function(modal) {
    $scope.modal = modal
  })

  $scope.openModal = function() {
    $scope.modal.show()
  }

  $scope.closeModal = function() {
    $scope.modal.hide();
  };

  $scope.$on('$destroy', function() {
    $scope.modal.remove();
  })

  // Productos
  var urlProductos = 'http://localhost:1337/quiickly.co/api/v1/products/?format=json';

  var json =
  [
     {
        "id":1,
        "name":"Extra Seguro",
        "brand":1,
        "type":1,
        "stock":10,
        "state":"1",
        "price":8200.0,
        "image":"/img/extra-seguro.png"
     },
     {
        "id":2,
        "name":"Sensitivo Delgado",
        "brand":1,
        "type":1,
        "stock":20,
        "state":"1",
        "price":10000.0,
        "image":"/img/sensitivo-delgado.png"
     },
     {
        "id":3,
        "name":"Placer Prolongado",
        "brand":1,
        "type":1,
        "stock":20,
        "state":"1",
        "price":11000.0,
        "image":"/img/placer-prolongado.png"
     }
  ];

  $scope.cargarProductos = function(){
    //$scope.Productos = json;
    //$scope.Info = json [0];
    $http.get(urlProductos).success(function(products){
      console.log(products);
      $scope.Productos = products;
      $scope.Info = products[0];
    })
  }

  $scope.cargarInfo = function($index){
    $scope.Info = json[$index];
    console.log($scope.Info);
  }

  // Slide de productos
  var options = {timeout: 10000, enableHighAccuracy: true};

  // Google Maps
  $cordovaGeolocation.getCurrentPosition(options).then(function(position){

    $scope.latLng = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);

    var styles = [
      {
        stylers: [
          { hue: "#673AB7" },
          { saturation: -10 }
        ]
      }
    ];

    var styledMap = new google.maps.StyledMapType(styles,
    {name: "Styled Map"});

    var mapOptions = {
      center: $scope.latLng,
      zoom: 15,
      disableDefaultUI: true,
      mapTypeControlOptions: {
        mapTypeIds: [google.maps.MapTypeId.ROADMAP, 'map_style']
      }
    };

    $scope.map = new google.maps.Map(document.getElementById("map"), mapOptions);

    $scope.map.setZoom(17);
    $scope.map.mapTypes.set('map_style', styledMap);
    $scope.map.setMapTypeId('map_style');

    $scope.geocoder = new google.maps.Geocoder();

    var infoWnd = new google.maps.InfoWindow({
      content :  $scope.map.getCenter().toUrlValue(),
      position : $scope.map.getCenter(),
      disableAutoPan: true
    });

    $scope.marker = new google.maps.Marker({
      map: $scope.map,
      animation: google.maps.Animation.DROP,
      position: $scope.map.getCenter(),
      icon: '../img/punto-central.png'
    });

    //infoWnd.open($scope.map, $scope.marker);
    function geopasar(map, geocoder){
      $scope.geocoder.geocode({'location': $scope.map.getCenter()}, function(results) {
        console.log(results[0].formatted_address);
        document.getElementById("direccion_field").value = results[0].formatted_address;
      })
    };

    //Retrive the center location
      google.maps.event.addListener($scope.map, "center_changed", function() {
        //marker.setContent($scope.map.getCenter().toUrlValue());
        $scope.marker.setPosition($scope.map.getCenter());
        //marker.open($scope.map);
        geopasar($scope.geocoder, $scope.map);
      });

  }, function(error){
    console.log("Could not get location");
  });

})

.controller('DashCtrl', function($scope) {

  var deploy = new Ionic.Deploy();

  // Update app code with new release from Ionic Deploy
  $scope.doUpdate = function() {
    deploy.update().then(function(res) {
      console.log('Ionic Deploy: Update Success! ', res);
    }, function(err) {
      console.log('Ionic Deploy: Update error! ', err);
    }, function(prog) {
      console.log('Ionic Deploy: Progress... ', prog);
    });
  };

  // Check Ionic Deploy for new code
  $scope.checkForUpdates = function() {
    console.log('Ionic Deploy: Checking for updates');
    deploy.check().then(function(hasUpdate) {
      console.log('Ionic Deploy: Update available: ' + hasUpdate);
      $scope.hasUpdate = hasUpdate;
    }, function(err) {
      console.error('Ionic Deploy: Unable to check for updates', err);
    });
  }

});
