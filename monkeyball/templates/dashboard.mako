<%inherit file="layouts/base.mako" />

<%def name="body()">
    <div class="dashboard">
        <article class="left">
            <div class="profile">

            </div>
            <div class="leaderboard">
                % for i in range(20):
                    <div class="leader">
                        Leader
                    </div>
                % endfor
            </div>
        </article>
        <aside class="right">
            <div class="upcoming_games">
            % for i in range(10):
                <div class="upcoming_game">
                    Upcoming Game
                </div>
            % endfor
            </div>
            <div class="previous_games">
            % for i in range(10):
                <div class="previoues_game">
                    Previous Game
                </div>
            % endfor
            </div>
        </aside>
    </div>
</%def>
