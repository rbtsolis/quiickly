angular.module('quiickly.controllers', ['ngOpenFB', 'ngStorage'])

.controller('AppCtrl', function($scope, $ionicModal, $timeout) {

  // With the new view caching in Ionic, Controllers are only called
  // when they are recreated or on app start, instead of every page change.
  // To listen for when this page is active (for example, to refresh data),
  // listen for the $ionicView.enter event:
  //$scope.$on('$ionicView.enter', function(e) {
  //});
})

.controller('MenuCtrl', function($scope, $state, serviceProduct, ngFB) {
  $scope.goToV = function(inicio, perfil){
    console.log(inicio);
    if (inicio === "inicio") {
      $state.go('app.map');
    }else{
      $state.go('app.profile');
    }
  }

  $scope.infoMenu = function(){
    ngFB.api({
      path: '/me',
      params: {fields: 'id, name, email'},
    }).then(
    function (data) {
      console.log(data);
      $scope.user = data;
      //StorageProfile.add($scope.user);
      $scope.urlImage = 'http://graph.facebook.com/'+$scope.user.id+'/picture?width=270&height=270';
      //StorageProfile.add($scope.urlImage)
    },
    function (error) {
      alert('Facebook error: ' + error.error_description);
    })
  }

})

.controller('AddrCtrl', function($scope, $state, serviceUser){
  $scope.addressNew = "";
  $scope.nameAddress = "";

  serviceUser
    .getAddress()
    .then(function(addresses){
      $scope.Addresses = addresses;
      console.log($scope.Addresses)
    }).catch(function(err) {
      console.log('No se ha podido obtener las direcciones')
    })

})

.controller('CreditCtrl', function($scope, $ionicModal, $ionicPopup){
  $scope.saveCC = function(){
     popupCredit.close();
  }
})

.controller('AboutCtrl', function($scope, $state, $ionicSideMenuDelegate){
  $ionicSideMenuDelegate.canDragContent(false)

  $scope.salirAbout = function (){
      $state.go('app.map');
  }

})

.controller('RegisterCtrl', function ($scope, $ionicSideMenuDelegate, $state, $http) {
  $ionicSideMenuDelegate.canDragContent(false)

  $scope.salirRegistro = function (){
      $state.go('app.map');
  }

  var urlRegister = 'http://localhost:1337/quiickly.co/login/';

  $scope.register = function(){
    $http({
    url: urlRegister,
    method: "POST",
    data: JSON.stringify({
      email: $scope.emailUser,
      password: $scope.passUser,
      telefono: $scope.telUser,
      direccion: $scope.addressUser
    }),
    headers: {'Content-Type': 'application/json'}
    }).success(function (data, error, status, headers, config) {
      console.log(data + " its works")
    }).error(function (data, error, status, headers, config) {
      console.log("Its sucks" + ' ' + error);
    });
  }

})

.controller('LoginCtrl', function($scope, $location, $state, $http, $ionicSideMenuDelegate, $ionicViewSwitcher, ngFB, StorageProfile){
  $ionicSideMenuDelegate.canDragContent(false)
  //$ionicViewSwitcher.nextDirection('exit');
  $scope.salirLogin = function (){
      $state.go('app.map');
  }

  var urlLogin = 'http://localhost:1337/quiickly.co/api/v1/tokens/create/';

  $scope.emailUser = 'userdemo@gmail.com';
  $scope.passUser = 'userdemo';

  $scope.login = function(){
    $http({
    url: urlLogin,
    method: "POST",
    data: JSON.stringify({
      email:$scope.emailUser,
      password:$scope.passUser
    }),
    headers: {'Content-Type': 'application/json'}
    }).success(function (data, error, status, headers, config) {
      console.log(data.token)
      $scope.dataUser = data;
      $scope.tokenUser = data.token;
      $scope.Loged = true;
      $scope.statusFB = false;
      $state.go('app.inservice')
    }).error(function (data, error, status, headers, config) {
      console.log("no WORKS" + '' + error);
    });
  }

  $scope.fbLogin = function () {
    ngFB.login(function (response) {
      if (response.status === 'connected') {
        console.log('Facebook login succeeded');
        $scope.statusFB = true;
        $scope.Loged = false;
        $scope.closeLogin();
      } else {
        alert('Facebook login failed');
      }
    },
    {scope: 'public_profile, email'});
  }

  $scope.goToRegister = function(){
    $state.go('app.register')
  }
})

.controller('ProfileCtrl', function ($scope, ngFB, StorageProfile) {

  // Verifica que tipo de usuario es (fb, regular)
  $scope.verifTUser = function(){
    ngFB.api({
      path: '/me',
      params: {fields: 'id, name, email'},
    }).then(
    function (data) {
      console.log(data);
      $scope.user = data;
      StorageProfile.add($scope.user);
      $scope.urlImage = 'http://graph.facebook.com/'+$scope.user.id+'/picture?width=270&height=270';
      StorageProfile.add($scope.urlImage)
    },
    function (error) {
      alert('Facebook error: ' + error.error_description);
    })
  }
})

.controller('ProductCtrl', function($scope, $ionicModal){})

.controller('InServiceCtrl', function($scope, $location, $cordovaGeolocation, StorageUbication, $ionicSideMenuDelegate){
  $ionicSideMenuDelegate.canDragContent(false)
  quiickler =
  [
    {
      name: "Antonio Delgado",
      plate: "PLP-469",
      tel: "3057507225",
      image: "https://photo.isu.pub/miguelrengifo1/photo_large.jpg",
      latitude: 3.384606,
      longitude: -76.527920,
      product: "Extra Seguro",
      total: "$ 12.000"
    }
  ]

  $scope.loadInfoQ = function(){
    $scope.dataQ = quiickler[0];
    /*$http.get(urlProducts).success(function(products){
      $scope.Products = products;
      $scope.InfoProduct = products[0];
      console.log(products[0]);
    })*/
  }

  // Google Maps
  var options = {timeout: 10000, enableHighAccuracy: true};
  $cordovaGeolocation.getCurrentPosition(options).then(function(position){

      $scope.latLng = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
      $scope.positionQ = {
        lat: $scope.dataQ.latitude,
        lng: $scope.dataQ.longitude
      }

      $scope.latUser = StorageUbication.getPen();
      $scope.lngUser = StorageUbication.getLast();

      $scope.positionUser = {
        lat: $scope.latUser,
        lng: $scope.lngUser
      }

      console.log($scope.positionUser);

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
        center: $scope.positionQ,
        zoom: 15,
        disableDefaultUI: false,
        mapTypeControlOptions: {
          mapTypeIds: [google.maps.MapTypeId.ROADMAP, 'map_style']
        }
      };

      $scope.mapService = "";

      $scope.mapService = new google.maps.Map(document.getElementById("mapService"), mapOptions);
      $scope.mapService.setZoom(17);
      $scope.mapService.mapTypes.set('map_style', styledMap);
      $scope.mapService.setMapTypeId('map_style');

      $scope.markerUser = new google.maps.Marker({
        map: $scope.mapService,
        animation: google.maps.Animation.DROP,
        position: $scope.positionUser,
        icon: '../img/punto.png'
      });

      $scope.markerQuiickler = new google.maps.Marker({
        map: $scope.mapService,
        animation: google.maps.Animation.DROP,
        position: $scope.positionQ,
        icon: '../img/quiickler.png'
      });

    }, function(error){
    console.log("Could not get location");
  })


})

.controller('MapCtrl', function($scope, $http, $location, $state, $ionicSideMenuDelegate, $ionicSlideBoxDelegate, $cordovaGeolocation, $ionicModal, StorageUbication, serviceProduct, $ionicPopup, $timeout) {
  $ionicSideMenuDelegate.canDragContent(false)


  var urlOrder = 'http://localhost:1337quiickly.co/api/v1/orders/?format=json'

  $scope.goTo = function() {
    StorageUbication.add($scope.latOrder);
    StorageUbication.add($scope.lngOrder);

    if($scope.Loged == true) {
      $state.go('app.inservice')
    }else {
      var popupLogin = $ionicPopup.show({
        title: 'NO ESTAS REGISTRADO',
        cssClass: 'modalLog',
        subTitle: 'Aún no estas registrado o has iniciado sesión, selecciona una opción para continuar',
        scope: $scope,
        buttons: [
          {
            text: 'REGISTRARME',
            onTap: function() {
            $state.go('app.register');
          }},{
            text: 'INICIAR SESIÓN',
            onTap: function() {
              $state.go('app.login');
            }
          }
        ]
      })
    $timeout(function() {
       popupLogin.close();
    }, 700000);
   }
  }

  $scope.classPago = "active";
  $scope.changeClassP = function(){
     if ($scope.class === "active"){
       $scope.class = "inactive";
     }else{
       $scope.class = "active";
    }
  }

  $scope.goToProduct = function() {
    $state.go('app.product')
  }

  $scope.openModal = function() {
    var popupCredit = $ionicPopup.show({
      title: 'AGREGAR TARJETA DE CRÉDITO',
      cssClass: 'modalCredit',
      template: '<div class="list"><p>No te preocupes por tu información, contamos con el respaldo de TPaga (de los creadores de Tappsi). Tu información no sera revelada a terceros.</p><label class="item item-input"><input type="text" ng-model="credit.name" placeholder="Nombre"></label><label class="item item-input"><input type="text" ng-model="credit.lastName" placeholder="Apellido"></label><label class="item item-input"><input type="number" ng-model="credit.cardNumber" placeholder="Número de Tarjeta"></label><div class="row"><div class="col col-67"><label class="item item-input"><input type="date" ng-model="credit.expireDate" placeholder="Fecha de Expiración"></label></div><div class="col col-33"><label class="item item-input"><input type="number" ng-model="credit.CVV" placeholder="CVV"></label></div></div></div>',
      scope: $scope,
      buttons: [
        {
          text: 'CANCELAR',
          onTap: function() {
          popupCredit.close();
        }},{
          text: 'GUARDAR',
          onTap: function() {
          popupCredit.close();
          }
        }
      ]
    })
  }

    serviceProduct
      .getProducts()
      .then(function(products){
        $scope.Products = products;
        $scope.InfoProduct = products[0];
      }).catch(function(err) {
        console.log('No se ha podido obtener los productos')
      })

      $scope.onDeleteClick = function() {
        //$ionicSlideBoxDelegate.next();

       $timeout(function(){
        //$scope.InfoProduct.splice($ionicSlideBoxDelegate.currentIndex(), 1);
        $ionicSlideBoxDelegate.update();
       },200);
      };

      $scope.slideChanged= function(index){
        $ionicSlideBoxDelegate.update();
        $scope.InfoProduct = $scope.Products[index];
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
      icon: '../img/central-point.png'
    });


    //infoWnd.open($scope.map, $scope.marker);
    function geopasar(map, geocoder){
      $scope.geocoder.geocode({'location': $scope.map.getCenter()}, function(results) {
        document.getElementById("direccion_field").value = results[0].formatted_address;
      })
    };

    //Retrive the center location
      google.maps.event.addListener($scope.map, "center_changed", function() {
        //marker.setContent($scope.map.getCenter().toUrlValue());
        $scope.marker.setPosition($scope.map.getCenter());
        //marker.open($scope.map);
        $scope.latOrder = $scope.marker.getPosition().lat();
        $scope.lngOrder = $scope.marker.getPosition().lng();
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
