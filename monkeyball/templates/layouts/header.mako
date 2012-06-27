<%def name="header(here)">
    <a class="logo" href="/">MonkeyBall</a>
    <ul class="main_nav horiz-list">
        <li>
            <a class="primary" href="/game/create">Start</a>
        </li>
        <li>
            <a class="primary" href="#">Queue</a>
        </li>
    </ul>
    <ul class="account horiz-list">
        <li>
            <a href="/">
                <img src="/static/img/avatar.png"/>
            </a>
        </li>
        <li>
            <a href="/">${ request.player.name }</a>
        </li>
    </ul>
</%def>
