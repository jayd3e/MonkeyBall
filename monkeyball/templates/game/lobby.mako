<%inherit file="../layouts/base.mako" />

<%def name="player_large(id, name)">
    <div class="player_large">
        <img src="http://graph.facebook.com/${ id }/picture"/>
        ${ name }
    </div>
</%def>

<%def name="body()">
    <form action="/game/${ game.id }" method="POST">
        <div class="game game_lobby">
            <div class="lobby${ game_type }">
                % if game.completed != True:
                    <div class="left_score">
                        <input maxlength="2" min="1" max="10" type="text" name="left_score" value="0" />
                    </div>
                % else:
                    <div class="left_score_display">
                        ${ game.left_score }
                    </div>
                % endif
                <div class="left_players">
                    ${ player_large(lefts[0]['id'], lefts[0]['name']) }
                    % if game.game_type == 1:
                        <div class="divider">-- and --</div>
                        ${ player_large(lefts[1]['id'], lefts[1]['name']) }
                    % endif
                </div>
                <div class="middle">
                    <div class="time">
                        @${ hour }:${ game.time.minute }${ m }
                    </div>
                    <div class="versus">vs</div>
                </div>
                <div class="right_players">
                    ${ player_large(rights[0]['id'], rights[0]['name']) }
                    % if game.game_type == 1:
                        <div class="divider">-- and --</div>
                        ${ player_large(rights[1]['id'], rights[1]['name']) }
                    % endif
                </div>
                % if game.completed != True:
                    <div class="right_score">
                        <input maxlength="2" min="1" max="10" type="text" name="right_score" value="0" />
                    </div>
                % else:
                    <div class="right_score_display">
                        ${ game.right_score }
                    </div>
                % endif
            </div>
            % if game.completed != True:
                <div class="finalize">
                    <input class="primary big" name="finalize" value="Finalize" type="submit" />
                </div>
            % endif
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
    </form>
</%def>
