"""empty message

Revision ID: 2da675b9512f
Revises: 77cbb2887920
Create Date: 2020-01-09 22:58:31.425382

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2da675b9512f'
down_revision = '77cbb2887920'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('products', 'shop')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('shop', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
