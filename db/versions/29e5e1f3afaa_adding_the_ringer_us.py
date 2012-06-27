"""Adding the ringer user.

Revision ID: 29e5e1f3afaa
Revises: 2757518b534a
Create Date: 2012-06-27 07:48:52.095259

"""

# revision identifiers, used by Alembic.
revision = '29e5e1f3afaa'
down_revision = '2757518b534a'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.execute("INSERT INTO players(id, name) VALUES(0, 'monkey')")


def downgrade():
    op.execute("DELETE FROM players WHERE id=0;")
