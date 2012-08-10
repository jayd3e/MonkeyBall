<%namespace name="notification_" file="../notifications.mako" />

<%def name="header(here)">
    <a class="logo" href="/">MonkeyBall</a>
    <ul class="main_nav horiz-list">
        <li>
            <a class="regular" id="notifications_button" href="#">${ len(notifications) }</a>
            % if len(notifications) > 0:
            <div class="notifications">
                % for notification in notifications:
                    ${ notification_.notification(notification) }
                % endfor
            </div>
            % endif
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
