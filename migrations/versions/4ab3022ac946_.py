"""empty message

Revision ID: 4ab3022ac946
Revises: 1e1efc183f90
Create Date: 2017-03-18 17:38:13.740197

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4ab3022ac946'
down_revision = '1e1efc183f90'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('ranking_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'comments', 'rankings', ['ranking_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_column('comments', 'ranking_id')
    # ### end Alembic commands ###
