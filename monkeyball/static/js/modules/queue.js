(function(Queue) {

    var monkeyball_queueme_source = $("#monkeyball_queueme_template").html();
    var monkeyball_queueme_template = Handlebars.compile(monkeyball_queueme_source);

    Queue.Views.QueueMe = Backbone.View.extend({
        events: {
            'click .activate_link': 'activate'
        },
        initialize: function(settings) {
            _.bindAll(this, 'poll', 'success', 'redirect');
            this.player_id = settings.player_id;
            this.interval_id = window.setInterval(this.poll, 2000);
        },
        render: function() {
            this.$el.html(monkeyball_queueme_template({'msg': 'Queueing...'}));
            return this;
        },
        poll: function() {
            $.ajax({
                'url': '/api/queueme',
                'success': this.success
            });
        },
        success: function(data) {
            if (data.status == 'success') {
                this.$el.html(monkeyball_queueme_template({'msg': 'Game Found.',
                                                           'game_id': data.game_id}));
                this.game_id = data.game_id;
                this.game_spot = data.game_spot;
            }
        },
        activate: function() {
            clearInterval(this.interval_id);

            $.ajax({
                'url': '/api/queueme/activate?game_id=' + this.game_id + '&game_spot=' + this.game_spot,
                'success': this.redirect
            });
        },
        redirect: function(data) {
            if (data.status == 'success') {
                window.location = '/game/' + data.game_id;
            } else {
                this.$el.html(monkeyball_queueme_template({'msg': 'Too slow.  Someone else took your spot.'}));
            }

        }
    });

})(monkeyball.module("queue"));