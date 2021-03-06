"""Fixed some more BigInteger problems.

Revision ID: 1fcf103516a8
Revises: 66c383cb0ab
Create Date: 2012-06-27 12:02:19.283787

"""

# revision identifiers, used by Alembic.
revision = '1fcf103516a8'
down_revision = '66c383cb0ab'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('notifications', 'player_id', type_=sa.BigInteger)
    op.alter_column('game_invite_notifications', 'player_id', type_=sa.BigInteger)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('notifications', 'player_id', type_=sa.Integer)
    op.alter_column('game_invite_notifications', 'player_id', type_=sa.Integer)
    ### end Alembic commands ###
