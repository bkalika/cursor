"""empty message

Revision ID: 77cbb2887920
Revises: 99bd4380a86f
Create Date: 2020-01-09 00:18:38.987684

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '77cbb2887920'
down_revision = '99bd4380a86f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'shops_products', ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'shops_products', type_='unique')
    # ### end Alembic commands ###
