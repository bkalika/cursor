"""empty message

Revision ID: dc1da4e9b479
Revises: eaf4a5071b6d
Create Date: 2020-01-03 20:42:07.593705

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dc1da4e9b479'
down_revision = 'eaf4a5071b6d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'shops', ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'shops', type_='unique')
    # ### end Alembic commands ###
