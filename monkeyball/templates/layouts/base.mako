<%namespace name="header" file="header.mako"/>

<!-- base.mako -->
<!DOCTYPE html>
<html>
    <head>
        <title>MonkeyBall!</title>
        <link rel="stylesheet" type="text/css" href="${request.static_url('monkeyball:static/css/bootstrap.css')}" />
    </head>
    <body>
        <div class="top">
            <div class="container">
                <header class="header">
                    ${ header.header(here) }
                </header>
            </div>
        </div>
        <div class="main">
            <div class="container">
                ${ self.body() }
            </div>
        </div>
    </body>

    <!-- Third-Party Libraries -->
    <script type="text/javascript" charset="utf-8" src="${request.static_url('monkeyball:static/js/libs/jquery-1.7.2.min.js')}"></script>
    <script type="text/javascript" charset="utf-8" src="${request.static_url('monkeyball:static/js/libs/jquery-ui-1.8.21.custom.min.js')}"></script>
    <script type="text/javascript" charset="utf-8" src="${request.static_url('monkeyball:static/js/libs/underscore.js')}"></script>
    <script type="text/javascript" charset="utf-8" src="${request.static_url('monkeyball:static/js/libs/backbone.js')}"></script>
    <script type="text/javascript" charset="utf-8" src="${request.static_url('monkeyball:static/js/libs/handlebars.js')}"></script>

    <script type="text/javascript" charset="utf-8" src="${request.static_url('monkeyball:static/js/index.js')}"></script>
    <script type="text/javascript" charset="utf-8" src="${request.static_url('monkeyball:static/js/modules/message.js')}"></script>
    <script type="text/javascript" charset="utf-8" src="${request.static_url('monkeyball:static/js/modules/queue.js')}"></script>
    <script type="text/javascript" charset="utf-8" src="${request.static_url('monkeyball:static/js/modules/player.js')}"></script>
    <script type="text/javascript" charset="utf-8" src="${request.static_url('monkeyball:static/js/modules/game.js')}"></script>
</html>