"""New result columns added.

Revision ID: 07521127eb98
Revises: 21ca2a685bf1
Create Date: 2023-08-25 09:05:59.006448

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '07521127eb98'
down_revision = '21ca2a685bf1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('result', schema=None) as batch_op:
        batch_op.add_column(sa.Column('backset', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('height', sa.Float(), nullable=True))

    with op.batch_alter_table('test', schema=None) as batch_op:
        batch_op.drop_index('ix_test_label')
        batch_op.create_index(batch_op.f('ix_test_label'), ['label'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('test', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_test_label'))
        batch_op.create_index('ix_test_label', ['label'], unique=False)

    with op.batch_alter_table('result', schema=None) as batch_op:
        batch_op.drop_column('height')
        batch_op.drop_column('backset')

    # ### end Alembic commands ###
