import unittest
from datetime import datetime
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# Models
from monkeyball.models.base import Base
from monkeyball.models.game import Game
from monkeyball.models.join import Join
from monkeyball.models.message import Message
from monkeyball.models.player import Player


class TestModels(unittest.TestCase):
    def setUp(self):
        engine = create_engine('sqlite://')
        Base.metadata.bind = engine
        Base.metadata.create_all(engine)
        self.Session = sessionmaker(bind=engine)

    def testGames(self):
        session = self.Session()

        game = Game(id=1,
                    completed=False,
                    left_score=0,
                    right_score=0,
                    game_type=0,
                    time=datetime.now(),
                    created=datetime.now())
        player = Player(id=1,
                        name="jayd3e")
        join = Join(game_id=1,
                    player_id=1)

        session.add(game)
        session.add(player)
        session.add(join)
        session.flush()

        self.assertTrue(str(game).startswith('<Game'),
                        msg="str(Game) must start with '<Game'")
        self.assertTrue(str(join).startswith('<Join'),
                        msg="str(Join) must start with '<Join'")
        self.assertIn(player, game.players)
        self.assertIn(game, player.games)

    def testMessages(self):
        session = self.Session()

        game = Game(id=1,
                    completed=False,
                    left_score=0,
                    right_score=0,
                    game_type=0,
                    time=datetime.now(),
                    created=datetime.now())
        player = Player(id=1,
                        name="jayd3e")
        message = Message(game_id=1,
                          player_id=1,
                          body="U Suk!")

        session.add(game)
        session.add(player)
        session.add(message)
        session.flush()

        self.assertTrue(str(message).startswith('<Message'),
                        msg="str(Message) must start with '<Message'")
        self.assertIn(message, game.messages)
        self.assertIn(message, player.messages)

    def testPlayers(self):
        session = self.Session()

        player = Player(id=1,
                        name="jayd3e")
        game = Game(id=1,
                    completed=False,
                    left_score=0,
                    right_score=0,
                    game_type=0,
                    time=datetime.now(),
                    created=datetime.now())
        join = Join(game_id=1,
                    player_id=1)

        session.add(game)
        session.add(player)
        session.add(join)
        session.flush()

        self.assertTrue(str(player).startswith('<Player'),
                        msg="str(Player) must start with '<Player'")
        self.assertIn(player, game.players)
        self.assertIn(game, player.games)
