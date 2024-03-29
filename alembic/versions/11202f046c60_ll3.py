"""ll3

Revision ID: 11202f046c60
Revises: f37c4b9f0037
Create Date: 2023-03-01 22:53:15.416817

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '11202f046c60'
down_revision = 'f37c4b9f0037'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('store', sa.Column('latitude_decimal', sa.Numeric(precision=9, scale=6), nullable=True))
    op.add_column('store', sa.Column('longitude_decimal', sa.Numeric(precision=10, scale=7), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('store', 'longitude_decimal')
    op.drop_column('store', 'latitude_decimal')
    # ### end Alembic commands ###
