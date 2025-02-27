"""empty message

Revision ID: 3a4399d96712
Revises: 
Create Date: 2024-11-04 23:29:28.154439

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3a4399d96712'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.add_column(sa.Column('priority', sa.String(length=20), nullable=True))
        batch_op.add_column(sa.Column('completed', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.drop_column('completed')
        batch_op.drop_column('priority')

    # ### end Alembic commands ###
