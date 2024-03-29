"""lending-entity

Revision ID: 1b5c68cb8bd2
Revises: 96d0aacb0d69
Create Date: 2023-03-08 03:03:42.289789

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1b5c68cb8bd2'
down_revision = '96d0aacb0d69'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('lending_entity_id_fkey', 'lending', type_='foreignkey')
    op.create_foreign_key(None, 'lending', 'entity', ['entity_id'], ['id'], ondelete='SET NULL')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'lending', type_='foreignkey')
    op.create_foreign_key('lending_entity_id_fkey', 'lending', 'store', ['entity_id'], ['id'], ondelete='SET NULL')
    # ### end Alembic commands ###
