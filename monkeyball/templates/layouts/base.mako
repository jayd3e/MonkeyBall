<%namespace name="header" file="header.mako"/>

<!-- base.mako -->
<!DOCTYPE html>
<html>
    <head>
        <title>MonkeyBall!</title>
        <link rel="stylesheet" type="text/css" href="${request.static_url('monkeyball:static/css/bootstrap.css')}" />
    </head>
    <body>
        <div id="top">
            <div class="container">
                <header id="header">
                    ${ header.header(here) }
                </header>
            </div>
        </div>
        <div id="main">
            <div class="container">
                ${ self.body() }
            </div>
        </div>
    </body>
</html>