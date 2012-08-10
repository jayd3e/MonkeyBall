"""Also changed the notifications model to match the new joins model.

Revision ID: 179a7a60ed90
Revises: 27c0ca36e0de
Create Date: 2012-08-10 10:56:45.983262

"""

# revision identifiers, used by Alembic.
revision = '179a7a60ed90'
down_revision = '27c0ca36e0de'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('notifications', sa.Column('spot', sa.Integer(), nullable=True))
    op.drop_column('notifications', u'side')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('notifications', sa.Column(u'side', sa.INTEGER(), nullable=True))
    op.drop_column('notifications', 'spot')
    ### end Alembic commands ###
