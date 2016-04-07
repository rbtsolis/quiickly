// Ionic Starter App

// angular.module is a global place for creating, registering and retrieving Angular modules
// 'starter' is the name of this angular module example (also set in a <body> attribute in index.html)
// the 2nd parameter is an array of 'requires'
// 'starter.controllers' is found in controllers.js
var quiickly = angular.module('quiickly', [
  'ionic',
  'ionic.service.core',
  'quiickly.controllers',
  'quiickly.services',
  'ngCordova',
  'ngOpenFB',
  'ngStorage'
 ])

.run(function($ionicPlatform, ngFB) {
  $ionicPlatform.ready(function() {
    
    // Hide the accessory bar by default (remove this to show the accessory bar above the keyboard
    // for form inputs)
    ngFB.init({appId: '1484517898520984'})

    if (window.cordova && window.cordova.plugins.Keyboard) {
      cordova.plugins.Keyboard.hideKeyboardAccessoryBar(true);
      cordova.plugins.Keyboard.disableScroll(true);

    }
    if (window.StatusBar) {
      // org.apache.cordova.statusbar required
      StatusBar.styleDefault();
    }
  });
})


quiickly.config(function($stateProvider, $urlRouterProvider) {

  $stateProvider

  .state('app', {
    url: '/app',
    abstract: true,
    templateUrl: 'templates/menu.html',
    controller: 'MenuCtrl'
  })

  .state('app.address', {
    url: '/address',
    views: {
      'menuContent': {
        templateUrl: 'templates/address.html',
        controller: 'AddrCtrl'
      }
    }
  })

  .state('app.about', {
    url: '/about',
    views: {
      'menuContent': {
        templateUrl: 'templates/about.html',
        controller: 'AboutCtrl'
      }
    }
  })

  .state('app.modal-credit', {
    url: '/modal-credit',
    views: {
      templateUrl: 'templates/modal-credit-card.html',
      controller: 'CreditCtrl'
    }
  })

  .state('app.product', {
    url: '/product',
    views: {
      templateUrl: 'templates/product-detail.html',
      controller: 'ProductCtrl'
    }
  })

  .state('app.login', {
    url: '/login',
    views: {
      'menuContent': {
        templateUrl: 'templates/login.html',
        controller: 'LoginCtrl'
      }
    }
  })

  .state('app.profile', {
    url: '/profile',
    views: {
      'menuContent': {
        templateUrl: 'templates/profile.html',
        controller: 'ProfileCtrl'
      }
    }
  })

  .state('app.register', {
    url: '/register',
    views: {
      'menuContent': {
        templateUrl: 'templates/register.html',
        controller: 'RegisterCtrl'
      }
    }
  })

  .state('app.inservice', {
    url: '/inservice',
    views: {
      'menuContent': {
        templateUrl: 'templates/inService.html',
        controller: 'InServiceCtrl'
      }
    }
  })

  .state('app.map', {
    url: '/map',
    views: {
      'menuContent': {
        templateUrl: 'templates/map.html',
        controller: 'MapCtrl'
      }
    }
  });

  $urlRouterProvider.otherwise("/app/map");

})
