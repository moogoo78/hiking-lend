"""lonlatx

Revision ID: da77bf6a63df
Revises: 12415ddbc8cd
Create Date: 2023-03-01 22:20:36.263153

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'da77bf6a63df'
down_revision = '12415ddbc8cd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('store', sa.Column('latitude_decimal', sa.Numeric(precision=9, scale=6), nullable=True))
    op.add_column('store', sa.Column('longitude_decimal', sa.Numeric(precision=9, scale=6), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('store', 'longitude_decimal')
    op.drop_column('store', 'latitude_decimal')
    # ### end Alembic commands ###
