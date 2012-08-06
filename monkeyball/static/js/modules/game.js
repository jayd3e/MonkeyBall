(function(Game) {

    // Deps
    var Player = monkeyball.module("player");
    var Message = monkeyball.module("message");

    var term = "";

    AvailablePlayers = Backbone.Collection.extend({
        model: Player.Model,
        url: function() {
            return "/api/players?s=" + term;
        }
    });

    Messages = Backbone.Collection.extend({
        model: Message.Model,
        initialize: function(settings) {
            this.game_id = settings.game_id;
        },
        url: function() {
            return "/api/messages?game_id=" + this.game_id;
        }
    });

    Game.Views.Creator = Backbone.View.extend({
        game_type: 1,

        events: {
            "click .options > .singles": "singles",
            "click .options > .doubles": "doubles",
            "mouseover .player_input.readonly": "mouseover_readonly",
            "mouseout .player_input.readonly": "mouseout_readonly",
            "click .player_input .remove": "remove",
            "click input:submit": "submit"
        },
        initialize: function() {
            _.bindAll(this, 'search', 'select');
            this.available_players = new AvailablePlayers();

            this.$(".player_input input[type='text']").autocomplete({
                source: this.search,
                select: this.select
            });
        },
        singles: function() {
            this.game_type = 0;

            this.$(".creator > .singles").show();
            this.$(".creator > .doubles").hide();
            this.$(".creator > .doubles input").prop("disable", true);
        },
        doubles: function() {
            this.game_type = 1;

            this.$(".creator > .doubles").show();
            this.$(".creator > .singles").hide();
            this.$(".creator > .singles input").prop("disable", true);
        },
        select: function(event, ui) {
            var player_input = $(event.target).parent();
            var input = player_input.children("input[type='text']");
            var hidden = player_input.children("input[type='hidden']");

            $(input).val(ui.item.label);
            $(input).attr("readonly", true);
            $(input).parent().addClass("readonly");

            var src = "http://graph.facebook.com/" + ui.item.value + "/picture";
            $(player_input).children("img").prop('src', src);

            $(hidden).val(ui.item.value);

            return false;
        },
        search: function(request, auto_comp_response) {
            term = request.term;
            this.available_players.fetch({
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
        mouseover_readonly: function(event) {
           $(event.target).parent().children(".remove").show();
        },
        mouseout_readonly: function(event) {
           $(event.target).parent().children(".remove").hide();
        },
        remove: function(event) {
            var player_input = $(event.target).parent();
            var input = player_input.children("input[type='text']");
            var hidden = player_input.children("input[type='hidden']");

            $(player_input).removeClass("readonly");
            $(player_input).children(".remove").hide();
            $(input).val("");
            $(input).removeAttr("readonly");
            $(input).focus();

            var src = "/static/img/thumbnail_normal.jpeg";
            $(player_input).children("img").prop('src', src);

            $(hidden).val("0");
        },
        submit: function() {
            error = this.validate();

            if (error === true) {
                this.$("input[name='game_type']").val(this.game_type);

                if(this.game_type === 0) {
                    this.$(".doubles input").prop("disabled", true);
                }
                else {
                    this.$(".singles input").prop("disabled", true);
                }

                return true;
            }
            else {
                this.$('.error').html(error);
            }

            return false;
        },
        validate: function() {
            if (this.game_type === 0) {
                type = ".singles";
            }
            else {
                type = ".doubles";
            }

            var hour = this.$(type + " .time input[name='hour']").val();
            var min = this.$(type + " .time input[name='min']").val();

            hour = parseInt(hour);
            min = parseInt(min);

            if (! (1 <= hour && hour <= 12) ) {
                return "Specify an hour between 1 and 12.";
            }

            if (! (0 <= min && min <= 60) ) {
                return "Specify a minute between 1 and 60.";
            }

            return true;
        }
    });

    Game.Views.Lobby =  Backbone.View.extend({
        el: $('.game_lobby'),

        events: {
            'keypress .chat .message_input input': 'keypress'
        },
        initialize: function(settings) {
            this.game_id = settings.game_id;
            _.bindAll(this, 'submit', 'reset', 'add_all', 'add_one', 'scroll');

            this.messages = new Messages({game_id: this.game_id});
            this.messages.fetch();
            this.messages.on('add', this.reset);

            this.chat_el = this.$('.chat');
            this.messages_el = this.chat_el.children('.messages');
            this.message_input = this.chat_el.children('.message_input');
            this.input = this.message_input.children('input');

            this.scroll();
            window.setInterval(this.reset, 2000);
        },
        scroll: function() {
            this.messages_el.scrollTop(this.messages_el.prop("scrollHeight"));
        },
        keypress: function(e) {
            if (e.which == 13) {
                this.submit();
                return false;
            }
        },
        submit: function() {
            var val = this.input.val();
            this.messages.create({'game_id': this.game_id,
                                  'body': val},
                                 {'wait': true});
            this.input.val('');
        },
        reset: function() {
            this.messages.fetch({'success': this.add_all});
        },
        add_all: function() {
            var scroll = false;
            if (this.messages_el.outerHeight() == (this.messages_el.scrollHeight - this.messages_el.scrollTop())) {
                scroll = true;
            }

            this.messages_el.empty();
            this.messages.each(function(message) {
                this.add_one(message);
            }, this);

            if (scroll) { this.scroll(); }
        },
        add_one: function(message) {
            message_el = this.make("div", {"class": "message"}, '<span class="username">' +
                                                                message.get('player_name') + '</span>' +
                                                                message.get('body'));
            this.messages_el.append(message_el);
        }
    });

})(monkeyball.module("game"));