var monkeyball = {
    module: function() {
        var modules = {};

        return function(name) {
            if (modules[name]) {
                return modules[name];
            }

            return modules[name] = { Views: {}, Models: {} };
        };
    }(),

    app: _.extend({}, Backbone.Events)
};

/*
*
* Called at run-time
*
*/

$(function() {
    var app = monkeyball.app;

    /*
    *
    * Main Router
    *
    */

    var Router = Backbone.Router.extend({

        routes: {
            "game/create": "create",
            "queue": "queue"
        },

        create: function() {
            var Game = monkeyball.module("game");
            var game = new Game.Views.Creator({el: $(".create_game")});
        },

        queue: function() {
            var Queue = monkeyball.module("queue");
            var queue = new Queue.Views.QueueMe();

            $(".main").prepend(queue.render().el);
        }

    });

    app.router = new Router();
    Backbone.history.start({pushState: true});
});