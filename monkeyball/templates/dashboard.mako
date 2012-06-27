<%inherit file="layouts/base.mako" />

<%def name="player(id, name)">
    <div class="player">
        % if name == "monkey":
            <img src="/static/img/thumbnail_normal.jpeg"/>
        % else:
            <img src="http://graph.facebook.com/${ id }/picture"/>
        % endif
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
            <div class="time">
                <a href="/game/${ game.id }">@${ game.hour }:${ "%02d" % game.time.minute }${ game.m }</a>
            </div>
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
                <a href="/game/${ game.id }">@${ game.hour }:${ "%02d" % game.time.minute }${ game.m }</a>
            </div>
            <div class="versus">vs</div>
        </div>
        <div class="right_players">
            ${ player(game.rights[0]['id'], game.rights[0]['name'])}
        </div>
    </div>
</%def>

<%def name="body()">
    <script id="monkeyball_queueme_template" type="handlebars-template">
        <div class="container">
            <div class="queueme">
                Queueing...
            </div>
        </div>
    </script>

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
                    <% i = 0 %>
                    % for leader in leaders:
                        <tr class="leader">
                            <td>${i+1}</td>
                            <td>${ leader.name }</td>
                            <td>${ leader.wins }</td>
                            <td>${ leader.losses }</td>
                            <td>${ leader.ratio }</td>
                        </tr>
                        <% i += 1 %>
                    % endfor
                    </tbody>
                </table>
            </div>
        </article>
        <aside class="right">
            <div class="upcoming_games">
                <h2>Upcoming Games</h2>
                % if len(upcoming_games) is not 0:
                    % for upcoming_game in upcoming_games:
                        % if upcoming_game.game_type == 0:
                            ${ single(upcoming_game) }
                        % else:
                            ${ double(upcoming_game) }
                        % endif
                    % endfor
                % else:
                    <div class="game">
                        <span class="notify">No Upcoming Games</span>
                    </div>
                % endif
            </div>
            <div class="previous_games">
                <h2>Previous Games</h2>
                % if len(previous_games) is not 0:
                    % for previous_game in previous_games:
                        % if previous_game.game_type == 0:
                            ${ single(previous_game) }
                        % else:
                            ${ double(previous_game) }
                        % endif
                    % endfor
                % else:
                    <div class="game">
                        <span class="notify">No Previous Games</span>
                    </div>
                % endif
            </div>
        </aside>
    </div>
</%def>
