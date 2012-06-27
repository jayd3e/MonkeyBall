(function(Game) {

    term = "";

    AvailableUsers = Backbone.Collection.extend({
        url: function() {
            return "/users?s=" + term;
        }
    });

    available_users = new AvailableUsers();

    Game.Views.Creator = Backbone.View.extend({
        events: {
            "click .options > .singles": "singles",
            "click .options > .doubles": "doubles",
            "keyup .player_input input": "search"
        },
        initialize: function() {
            this.$('.player_input input').autocomplete({
                source: function(request, auto_comp_response) {

                    available_users.fetch({
                        success: function(collection, response) {

                            auto_comp_response($.map(collection, function( user ) {
                                return {
                                    label: user.name,
                                    value: user.name
                                };
                            }));

                        }
                    });

                }
            });
        },
        singles: function() {
            this.$(".creator > .singles").show();
            this.$(".creator > .doubles").hide();
        },
        doubles: function() {
            this.$(".creator > .doubles").show();
            this.$(".creator > .singles").hide();
        },
        search: function(event) {

        }
    });

})(monkeyball.module("game"));