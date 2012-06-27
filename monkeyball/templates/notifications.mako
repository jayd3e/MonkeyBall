<%def name="notification(notification)">
    <%
        from monkeyball.models.notification import GameInviteNotification
        from monkeyball.models.notification import GameStartNotification
    %>
    <div class="notification">
        % if isinstance(notification, GameInviteNotification):
            ${ notification.inviter.name } has invited you to a game.
            <a href="/game/join/${ notification.game.id }" class="primary">Join</a>
        % elif isinstance(notification, GameStareNotification):
            IT'S ON NOW!!
            <a href="/game/${ notification.game.id }" class="primary">Go To</a>
        % endif
    </div>
</%def>