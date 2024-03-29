"""email

Revision ID: 3c480eb39ffa
Revises: 72ece169657b
Create Date: 2024-01-29 19:32:05.335696

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3c480eb39ffa'
down_revision = '72ece169657b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('store', sa.Column('next_process', sa.String(length=500), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('store', 'next_process')
    # ### end Alembic commands ###
