<%inherit file="layouts/base.mako" />

<%def name="body()">
    <div class="dashboard">
        <article class="left">
            <div class="profile">

            </div>
            <div class="leaderboard">
                <h2>Leaders</h2>
                % for i in range(20):
                    <div class="leader">
                        Leader
                    </div>
                % endfor
            </div>
        </article>
        <aside class="right">
            <div class="upcoming_games">
            <h2>Upcoming Games</h2>
            % for i in range(10):
                <div class="upcoming_game">
                    Upcoming Game
                </div>
            % endfor
            </div>
            <div class="previous_games">
            <h2>Previous Games</h2>
            % for i in range(10):
                <div class="previoues_game">
                    Previous Game
                </div>
            % endfor
            </div>
        </aside>
    </div>
</%def>
