<%inherit file="../layouts/base.mako" />

<%def name="player_input(side)">
    <div class="player_input">
        <img src="/static/img/thumbnail_normal.jpeg"/>
        <input name="${ side }_id" type="hidden" value="0" />
        <input name="${ side }_user" type="text" value="monkey" />
        <a class="remove">X</a>
    </div>
</%def>

<%def name="time()">
    <input name="hour" maxlength="2" type="text" value="0" />
    <input name="min" maxlength="2" type="text" value="0" />
    <select name="m">
        <option value="0">AM</option>
        <option value="1">PM</option>
    </select>
</%def>


<%def name="body()">
    <form method="POST" action="/game/create">
        <div class="game create_game">
            <div class="inner">
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
                            ${ player_input("left") }
                            <div class="divider">-- and --</div>
                            ${ player_input("left") }
                        </div>
                        <div class="middle">
                            <div class="time">
                                ${ time() }
                            </div>
                            <div class="versus">vs</div>
                        </div>
                        <div class="right_players">
                            ${ player_input("right") }
                            <div class="divider">-- and --</div>
                            ${ player_input("right") }
                        </div>
                    </div>
                    <div class="singles">
                        <div class="left_players">
                            ${ player_input("left") }
                        </div>
                        <div class="middle">
                            <div class="time">
                                ${ time() }
                            </div>
                            <div class="versus">vs</div>
                        </div>
                        <div class="right_players">
                            ${ player_input("right") }
                        </div>
                    </div>
                </div>
                <div class="actions">
                    <input class="primary" name="submit" type="submit" />
                    <input class="primary" name="cancel" type="submit" />
                </div>
            </div>
        </div>
    </form>
</%def>
