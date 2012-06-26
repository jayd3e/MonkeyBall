<%inherit file="layouts/base.mako" />

<%def name="body()">
    <div class="dashboard">
        <article class="left">
            <div class="profile">

            </div>
            <div class="leaderboard">
                <h2>Leaders</h2>
                <table class="leaders">
                    <thead>
                        <th class="num">
                           #
                        </th>
                        <th>
                            player
                        </th>
                        <th>
                            wins
                        </th>
                        <th>
                            losses
                        </th>
                        <th>
                            ratio
                        </th>
                    </thead>
                    <tbody>
                    % for i in range(20):
                        <tr class="leader">
                            <td>
                                ${i+1}
                            </td>
                            <td>
                                jayd3e
                            </td>
                            <td>
                                5
                            </td>
                            <td>
                                8
                            </td>
                            <td>
                                1.5
                            </td>
                        </tr>
                    % endfor
                    </tbody>
                </table>
            </div>
        </article>
        <aside class="right">
            <div class="upcoming_games">
            <h2>Upcoming Games</h2>
            % for i in range(2):
                <div class="game doubles">
                    <div class="left_players">
                        <div class="player">
                            <img src="/static/img/avatar.png"/>
                            <a href="/">jayd3e</a>
                        </div>
                        <div class="divider">-- and --</div>
                        <div class="player">
                            <img src="/static/img/avatar.png"/>
                            <a href="/">jayd3e</a>
                        </div>
                    </div>
                    <div class="middle">
                        <div class="time">@3:00pm</div>
                        <div class="versus">vs</div>
                    </div>
                    <div class="right_players">
                        <div class="player">
                            <img src="/static/img/avatar.png"/>
                            <a href="/">jayd3e</a>
                        </div>
                        <div class="divider">-- and --</div>
                        <div class="player">
                            <img src="/static/img/avatar.png"/>
                            <a href="/">jayd3e</a>
                        </div>
                    </div>
                </div>
            % endfor
            % for i in range(1):
                <div class="game singles">
                    <div class="left_players">
                        <div class="player">
                            <img src="/static/img/avatar.png"/>
                            <a href="/">jayd3e</a>
                        </div>
                    </div>
                    <div class="middle">
                        <div class="time">@3:00pm</div>
                        <div class="versus">vs</div>
                    </div>
                    <div class="right_players">
                        <div class="player">
                            <img src="/static/img/avatar.png"/>
                            <a href="/">jayd3e</a>
                        </div>
                    </div>
                </div>
            % endfor
            </div>
            <div class="previous_games">
            <h2>Previous Games</h2>
            % for i in range(2):
                <div class="game doubles">
                    <div class="left_players">
                        <div class="player">
                            <img src="/static/img/avatar.png"/>
                            <a href="/">jayd3e</a>
                        </div>
                        <div class="divider">-- and --</div>
                        <div class="player">
                            <img src="/static/img/avatar.png"/>
                            <a href="/">jayd3e</a>
                        </div>
                    </div>
                    <div class="middle">
                        <div class="time">@3:00pm</div>
                        <div class="versus">vs</div>
                    </div>
                    <div class="right_players">
                        <div class="player">
                            <img src="/static/img/avatar.png"/>
                            <a href="/">jayd3e</a>
                        </div>
                        <div class="divider">-- and --</div>
                        <div class="player">
                            <img src="/static/img/avatar.png"/>
                            <a href="/">jayd3e</a>
                        </div>
                    </div>
                </div>
            % endfor
            % for i in range(1):
                <div class="game singles">
                    <div class="left_players">
                        <div class="player">
                            <img src="/static/img/avatar.png"/>
                            <a href="/">jayd3e</a>
                        </div>
                    </div>
                    <div class="middle">
                        <div class="time">@3:00pm</div>
                        <div class="versus">vs</div>
                    </div>
                    <div class="right_players">
                        <div class="player">
                            <img src="/static/img/avatar.png"/>
                            <a href="/">jayd3e</a>
                        </div>
                    </div>
                </div>
            % endfor
            </div>
        </aside>
    </div>
</%def>
