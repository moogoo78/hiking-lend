"""store-status

Revision ID: 93cae113281b
Revises: 3c480eb39ffa
Create Date: 2024-01-29 19:50:22.272046

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '93cae113281b'
down_revision = '3c480eb39ffa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('store', sa.Column('status', sa.String(length=2), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('store', 'status')
    # ### end Alembic commands ###
