"""Changed a field on the Player model

Revision ID: 43ca03a53294
Revises: 51063ed8b872
Create Date: 2012-06-26 19:45:46.683655

"""

# revision identifiers, used by Alembic.
revision = '43ca03a53294'
down_revision = '51063ed8b872'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('players', sa.Column('name', sa.String(), nullable=True))
    op.drop_column('players', u'username')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('players', sa.Column(u'username', sa.VARCHAR(), nullable=True))
    op.drop_column('players', 'name')
    ### end Alembic commands ###
