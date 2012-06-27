<%inherit file="layouts/base.mako" />

<%def name="player(id, name)">
    <div class="player">
        <img src="http://graph.facebook.com/${ id }/picture"/>
        <a href="/">${ name }</a>
    </div>
</%def>

<%def name="double(game)">
    <div class="game doubles">
        <div class="left_players">
            ${ player(game.lefts[0]['id'], game.lefts[0]['name'])}
            <div class="divider">-- and --</div>
            ${ player(game.lefts[1]['id'], game.lefts[1]['name'])}
        </div>
        <div class="middle">
            <div class="time">@3:00pm</div>
            <div class="versus">vs</div>
        </div>
        <div class="right_players">
            ${ player(game.rights[0]['id'], game.rights[0]['name'])}
            <div class="divider">-- and --</div>
            ${ player(game.rights[1]['id'], game.rights[1]['name'])}
        </div>
    </div>
</%def>

<%def name="single(game)">
    <div class="game singles">
        <div class="left_players">
            ${ player(game.lefts[0]['id'], game.lefts[0]['name'])}
        </div>
        <div class="middle">
            <div class="time">
                @${ game.hour }:${ "%02d" % game.time.minute }${ game.m }
            </div>
            <div class="versus">vs</div>
        </div>
        <div class="right_players">
            ${ player(game.rights[0]['id'], game.rights[0]['name'])}
        </div>
    </div>
</%def>

<%def name="body()">
    <div class="dashboard">
        <article class="left">
            <div class="profile">
                <h2><span class="wins">Wins:</span> <span class="num">${ wins }</span></h2>
                <h2><span class="losses">Losses:</span> <span class="num">${ losses }</span></h2>
                <h2><span class="ratio">Ratio:</span> <span class="num">${ ratio }</span></h2>
            </div>
            <div class="leaderboard">
                <h2>Leaders</h2>
                <table class="leaders">
                    <thead>
                        <th class="num">#</th>
                        <th>player</th>
                        <th>wins</th>
                        <th>losses</th>
                        <th>ratio</th>
                    </thead>
                    <tbody>
                    % for i in range(20):
                        <tr class="leader">
                            <td>${i+1}</td>
                            <td>jayd3e</td>
                            <td>5</td>
                            <td>8</td>
                            <td>1.5</td>
                        </tr>
                    % endfor
                    </tbody>
                </table>
            </div>
        </article>
        <aside class="right">
            <div class="upcoming_games">
                <h2>Upcoming Games</h2>
                % for upcoming_game in upcoming_games:
                    % if upcoming_game.game_type == 0:
                        ${ single(upcoming_game) }
                    % else:
                        ${ double(upcoming_game) }
                    % endif
                % endfor
            </div>
            <div class="previous_games">
                <h2>Previous Games</h2>
                % for previous_game in previous_games:
                    % if previous_game.game_type == 0:
                        ${ single(previous_game) }
                    % else:
                        ${ double(previous_game) }
                    % endif
                % endfor
            </div>
        </aside>
    </div>
</%def>
