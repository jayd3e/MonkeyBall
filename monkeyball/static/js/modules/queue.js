(function(Queue) {

    var monkeyball_queueme_source = $("#monkeyball_queueme_template").html();
    var monkeyball_queueme_template = Handlebars.compile(monkeyball_queueme_source);

    Queue.Views.QueueMe = Backbone.View.extend({
        events: {},
        initialize: function() {
            _.bindAll(this, 'poll');
        },
        render: function() {
            this.$el.html(monkeyball_queueme_template({}));
            return this;
        },
        poll: function() {

        }
    });

})(monkeyball.module("queue"));