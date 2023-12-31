"""Initial Migration

Revision ID: 7e60b546476d
Revises: 
Create Date: 2023-08-03 12:29:33.643747

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7e60b546476d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('test', schema=None) as batch_op:
        batch_op.drop_index('ix_test_label')
        batch_op.create_index(batch_op.f('ix_test_label'), ['label'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('test', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_test_label'))
        batch_op.create_index('ix_test_label', ['label'], unique=False)

    # ### end Alembic commands ###
