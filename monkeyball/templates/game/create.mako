<%inherit file="../layouts/base.mako" />

<%def name="body()">
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
            <div class="creator">
                <div class="doubles">
                    <div class="left_players">
                        <div class="player_input">
                            <img src="/static/img/thumbnail_normal.jpeg"/>
                            <input name="user" type="text" value="player"/>
                        </div>
                        <div class="divider">-- and --</div>
                        <div class="player_input">
                            <img src="/static/img/thumbnail_normal.jpeg"/>
                            <input name="user" type="text" value="player"/>
                        </div>
                    </div>
                    <div class="middle">
                        <div class="time">
                            <input type="text" name="time" value="time"/>
                        </div>
                        <div class="versus">vs</div>
                    </div>
                    <div class="right_players">
                        <div class="player_input">
                            <img src="/static/img/thumbnail_normal.jpeg"/>
                            <input name="user" type="text" value="player"/>
                        </div>
                        <div class="divider">-- and --</div>
                        <div class="player_input">
                            <img src="/static/img/thumbnail_normal.jpeg"/>
                            <input name="user" type="text" value="player"/>
                        </div>
                    </div>
                </div>
                <div class="singles">
                    <div class="left_players">
                        <div class="player_input">
                            <img src="/static/img/thumbnail_normal.jpeg"/>
                            <input name="user" type="text" value="player"/>
                        </div>
                    </div>
                    <div class="middle">
                        <div class="time">
                            <input type="text" name="time" value="time"/>
                        </div>
                        <div class="versus">vs</div>
                    </div>
                    <div class="right_players">
                        <div class="player_input">
                            <img src="/static/img/thumbnail_normal.jpeg"/>
                            <input name="user" type="text" value="player"/>
                        </div>
                    </div>
                </div>
            </div>
            <div class="actions">
                <a class="primary" href="/">Send Invites</a>
                <a class="primary" href="/">Cancel</a>
            </div>
        </div>
    </div>
</%def>
