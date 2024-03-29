"""ll2

Revision ID: f37c4b9f0037
Revises: 62befd7a052a
Create Date: 2023-03-01 22:53:05.662297

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f37c4b9f0037'
down_revision = '62befd7a052a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('store', 'latitude_decimal')
    op.drop_column('store', 'longitude_decimal')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('store', sa.Column('longitude_decimal', sa.NUMERIC(precision=10, scale=3), autoincrement=False, nullable=True))
    op.add_column('store', sa.Column('latitude_decimal', sa.NUMERIC(precision=8, scale=2), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
