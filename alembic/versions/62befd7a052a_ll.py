"""ll

Revision ID: 62befd7a052a
Revises: 614b1428c27b
Create Date: 2023-03-01 22:50:22.115375

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '62befd7a052a'
down_revision = '614b1428c27b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('store', sa.Column('latitude_decimal', sa.Numeric(precision=8, scale=2), nullable=True))
    op.add_column('store', sa.Column('longitude_decimal', sa.Numeric(precision=10, scale=3), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('store', 'longitude_decimal')
    op.drop_column('store', 'latitude_decimal')
    # ### end Alembic commands ###