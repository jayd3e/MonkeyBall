(function(Queue) {

    var monkeyball_queueme_source = $("#monkeyball_queueme_template").html();
    var monkeyball_queueme_template = Handlebars.compile(monkeyball_queueme_source);

    Queue.Views.QueueMe = Backbone.View.extend({
        events: {},
        initialize: function(settings) {
            _.bindAll(this, 'poll', 'success');
            this.player_id = settings.player_id;
            window.setInterval(this.poll, 2000);
        },
        render: function() {
            this.$el.html(monkeyball_queueme_template({'msg': 'Queueing...'}));
            return this;
        },
        poll: function() {
            $.ajax({
                'url': '/api/queueme',
                'data': {
                    'player_id': this.player_id
                },
                'success': this.success
            });
        },
        success: function(data) {
            if (data.success) {
                this.$el.html(monkeyball_queueme_template({'msg': 'Queued'}));
            }
        }
    });

})(monkeyball.module("queue"));