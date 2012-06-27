(function(Game) {

    // Deps
    var Player = monkeyball.module("player");

    var term = "";

    AvailablePlayers = Backbone.Collection.extend({
        model: Player.Model,
        url: function() {
            return "/api/players?s=" + term;
        }
    });

    var available_players = new AvailablePlayers();

    Game.Views.Creator = Backbone.View.extend({
        events: {
            "click .options > .singles": "singles",
            "click .options > .doubles": "doubles",
            "mouseover .player_input.disabled": "mouseover_disabled",
            "mouseout .player_input.disabled": "mouseout_disabled",
            "click .player_input .remove": "remove",
            "click .input[type='submit']": "submit"
        },
        initialize: function() {
            _.bindAll(this, 'search', 'select');

            this.$(".player_input input[type='text']").autocomplete({
                source: this.search,
                select: this.select
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
        select: function(event, ui) {
            var player_input = $(event.target).parent();
            var input = player_input.children("input[type='text']");
            var hidden = player_input.children("input[type='hidden']");

            $(input).val(ui.item.label);
            $(input).prop("disabled", true);
            $(input).parent().addClass("disabled");

            var src = "http://graph.facebook.com/" + ui.item.value + "/picture";
            $(player_input).children("img").prop('src', src);

            $(hidden).val(ui.item.value);

            return false;
        },
        search: function(request, auto_comp_response) {
            term = request.term;
            available_players.fetch({
                success: function(collection, response) {
                    auto_comp_response(collection.map(function( player ) {
                        return {
                            label: player.get("name"),
                            value: player.get("id")
                        };
                    }));
                }
            });
        },
        mouseover_disabled: function(event) {
           $(event.target).parent().children(".remove").show();
        },
        mouseout_disabled: function(event) {
           $(event.target).parent().children(".remove").hide();
        },
        remove: function(event) {
            var player_input = $(event.target).parent();
            var input = player_input.children("input[type='text']");
            var hidden = player_input.children("input[type='hidden']");

            $(player_input).removeClass("disabled");
            $(player_input).children(".remove").hide();
            $(input).val("");
            $(input).prop("disabled", false);
            $(input).focus();

            var src = "/static/img/thumbnail_normal.jpeg";
            $(player_input).children("img").prop('src', src);

            $(hidden).val("0");
        },
        submit: function() {
            return this.validate();
        },
        validate: function() {
            return true;
        }
    });

})(monkeyball.module("game"));