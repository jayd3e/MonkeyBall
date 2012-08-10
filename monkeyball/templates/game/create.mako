<%inherit file="../layouts/base.mako" />

<%def name="own_player_input()">
    <div class="player_input readonly">
        <img src="http://graph.facebook.com/${ request.player.id }/picture"/>
        <input name="top_left_id" type="hidden" value="${ request.player.id }" />
        <input name="top_left_user" type="text" value="${ request.player.name }" readonly />
        <a class="remove">X</a>
    </div>
</%def>

<%def name="player_input(spot)">
    <div class="player_input">
        <img src="/static/img/thumbnail_normal.jpeg"/>
        <input name="${ spot }_id" type="hidden" value="0" />
        <input name="${ spot }_user" type="text" value="monkey" />
        <a class="remove">X</a>
    </div>
</%def>

<%def name="time()">
    <input name="hour" maxlength="2" type="text" value="${ hour }" autocomplete="off" />
    <input name="min" maxlength="2" type="text" value="${ min }" autocomplete="off" />
    <select name="m">
        <option value="AM"
        % if m == "AM":
            selected
        % endif
        >AM</option>
        <option value="PM"
        % if m == "PM":
            selected
        % endif
        >PM</option>
    </select>
</%def>


<%def name="body()">
    <form method="POST" action="/game/create">
        <div class="game create_game">
            <div class="inner">
                <input name="game_type" type="hidden" value="1" />
                <ul class="options horiz-list">
                    <li class="singles">
                        1v1
                    </li>
                    <li class="doubles">
                        2v2
                    </li>
                </ul>
                <div class="error"></div>
                <div class="creator">
                    <div class="doubles">
                        <div class="left_players">
                            ${ own_player_input() }
                            <div class="divider">-- and --</div>
                            ${ player_input("bottom_left") }
                        </div>
                        <div class="middle">
                            <div class="time">
                                ${ time() }
                            </div>
                            <div class="versus">vs</div>
                        </div>
                        <div class="right_players">
                            ${ player_input("top_right") }
                            <div class="divider">-- and --</div>
                            ${ player_input("bottom_right") }
                        </div>
                    </div>
                    <div class="singles">
                        <div class="left_players">
                            ${ own_player_input() }
                        </div>
                        <div class="middle">
                            <div class="time">
                                ${ time() }
                            </div>
                            <div class="versus">vs</div>
                        </div>
                        <div class="right_players">
                            ${ player_input("top_right") }
                        </div>
                    </div>
                </div>
                <div class="actions">
                    <input class="primary" name="submit" type="submit" />
                    <input class="primary" name="cancel" value="Cancel" type="submit" />
                </div>
            </div>
        </div>
    </form>
</%def>
