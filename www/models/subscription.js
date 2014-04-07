define([
  'jquery',
  'underscore',
  'backbone'
], function($, _, Backbone) {
  'use strict';
  var SubscriptionModel = Backbone.Model.extend({
    defaults: {
      'license': null,
      'card': null,
      'email': null,
      'active': null,
      'status': null,
      'period_end': null,
      'cancel_at_period_end': null
    },
    url: function() {
      return '/subscription';
    }
  });

  return SubscriptionModel;
});