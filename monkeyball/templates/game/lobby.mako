<%inherit file="../layouts/base.mako" />

<%def name="body()">
    <div class="game game_lobby">
        <div class="lobby">
            <div class="left_score">
                <input maxlength="2" min="1" max="10" type="text" name="score" />
            </div>
            <div class="left_players">
                <div class="player_large">
                    <img src="/static/img/thumbnail_normal.jpeg"/>
                    jayd3e
                </div>
                <div class="divider">-- and --</div>
                <div class="player_large">
                    <img src="/static/img/thumbnail_normal.jpeg"/>
                    jayd3e
                </div>
            </div>
            <div class="middle">
                <div class="time">
                    @3:00pm
                </div>
                <div class="versus">vs</div>
            </div>
            <div class="right_players">
                <div class="player_large">
                    <img src="/static/img/thumbnail_normal.jpeg"/>
                    jayd3e
                </div>
                <div class="divider">-- and --</div>
                <div class="player_large">
                    <img src="/static/img/thumbnail_normal.jpeg"/>
                    jayd3e
                </div>
            </div>
            <div class="right_score">
                <input maxlength="2" min="1" max="10" type="text" name="score" />
            </div>
        </div>
        <div class="finalize">
            <a class="primary big" href="#">Finalize</a>
        </div>
        <div class="chat">
            <div class="messages">
                % for i in range(100):
                <div class="message">
                    <span class="username">jayd3e</span>Some text here!!
                </div>
                % endfor
            </div>
            <div class="message_input">
                <input type="text" name="body" />
            </div>
        </div>
    </div>
</%def>
