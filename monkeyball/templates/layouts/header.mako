<%def name="header(here)">
    <a class="logo" href="/">MonkeyBall</a>
    <ul class="main_nav horiz-list">
        <li>
            <a class="regular" href="#">${ len(notifications) }</a>
            <div class="notifications">
                % for notifcation in notifications:
                    <div class="notification">

                    </div>
                % endfor
            </div>
        </li>
        <li>
            <a class="primary" href="/game/create">Start</a>
        </li>
        <li>
            <a class="primary" href="/queue">Queue</a>
        </li>
    </ul>
    <ul class="account horiz-list">
        <li>
            <a href="/">
                <img class="avatar_small" src="http://graph.facebook.com/${ request.player.id }/picture"/>
            </a>
        </li>
        <li>
            <a href="/">${ request.player.name }</a>
        </li>
    </ul>
</%def>
