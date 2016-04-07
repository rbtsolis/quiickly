angular.module('quiickly.controllers', ['ngOpenFB', 'ngStorage'])

.controller('AppCtrl', function($scope, $ionicModal, $timeout) {

  // With the new view caching in Ionic, Controllers are only called
  // when they are recreated or on app start, instead of every page change.
  // To listen for when this page is active (for example, to refresh data),
  // listen for the $ionicView.enter event:
  //$scope.$on('$ionicView.enter', function(e) {
  //});
})

.controller('MenuCtrl', function($scope, $state, serviceProduct) {
  $scope.goToV = function(inicio, perfil){
    console.log(inicio);
    if (inicio === "inicio") {
      $state.go('app.map');
    }else{
      $state.go('app.profile');
    }
  }

  serviceProduct.getProducts()
  .then(function(data){
    $scope.menuNombre = data[0];
  })

})

.controller('AddrCtrl', function($scope, $state){
  $scope.addressNew = "";
  $scope.nameAddress = "";

  direcciones = [
    {
      addressNew: "Calle 22 #5-56, Cali",
      nameAddress: "Casa Buitrera"
    },
    {
      addressNew: "Calle la escopeta",
      nameAddress: "Oficina Quiickly"
    }
  ]

  $scope.registerAddress = function(){
    //$scope.addressNew.set(direcciones[0]);
    //$scope.nameAddress.set(direcciones[0]);
    console.log(direcciones[0]);
    $scope.addressUser = direcciones[0];
    console.log(direcciones)
  }


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

      /*datas = [
        {
          name: "Miguel Rengifo",
          email: "m@quiickly.co"
        }
      ]
      $scope.user = datas[0];
      console.log($scope.user)
      $scope.urlImage = 'img/pp.jpg';*/
    }
  })

.controller('ProductCtrl', function($scope, $ionicModal){})

.controller('InServiceCtrl', function($scope, $location, $cordovaGeolocation, StorageUbication){
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
    $scope.dataQ = quiickler [0];
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

.controller('MapCtrl', function($scope, $http, $location, $state, $cordovaGeolocation, $ionicModal, StorageUbication, serviceProduct, $ionicPopup, $timeout) {

  var urlOrder = 'http://localhost:1337quiickly.co/api/v1/orders/?format=json'

  $scope.order = function(){
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
    headers: {'Content-Type': 'application/json'}
    }).success(function (response, error, status, headers, config) {
      $state.go('app.inservice')
    }).error(function (data, error, status, headers, config) {
      console.log("no funciona" + '' + error);
    });
  }

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

  $ionicModal.fromTemplateUrl('templates/modal-credit-card.html', {
    scope: $scope,
    animation: 'slide-in-up',
    focusFirstInput: true
  }).then(function(modal) {
    $scope.modal = modal
  })

  $scope.openModal = function() {
    var popupCredit = $ionicPopup.show({
      cssClass: 'modalCredit',
      templateUrl: 'templates/modal-credit-card.html',
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

  }

  serviceProduct
    .getProducts()
    .then(function(products){
      $scope.Products = products;
      $scope.InfoProduct = products[0];
    }).catch(function(err) {
      console.log('No se ha podido obtener los productos')
    })



  $scope.loadInfoProduct = function($index){
    $scope.InfoProduct = json[$index];
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
