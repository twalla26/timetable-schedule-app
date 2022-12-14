"""empty message

Revision ID: 4584f1ee3cf3
Revises: 61bada784bdd
Create Date: 2022-12-11 00:01:37.448882

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4584f1ee3cf3'
down_revision = '61bada784bdd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('plan', schema=None) as batch_op:
        batch_op.add_column(sa.Column('duration', sa.String(length=150), nullable=False))

    with op.batch_alter_table('schedule', schema=None) as batch_op:
        batch_op.add_column(sa.Column('timetable_array', sa.Text(), nullable=True))
        batch_op.drop_column('possible_time')
        batch_op.drop_column('impossible_time')
        batch_op.drop_column('ambiguous_time')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('schedule', schema=None) as batch_op:
        batch_op.add_column(sa.Column('ambiguous_time', sa.VARCHAR(), nullable=True))
        batch_op.add_column(sa.Column('impossible_time', sa.VARCHAR(), nullable=True))
        batch_op.add_column(sa.Column('possible_time', sa.VARCHAR(), nullable=False))
        batch_op.drop_column('timetable_array')

    with op.batch_alter_table('plan', schema=None) as batch_op:
        batch_op.drop_column('duration')

    # ### end Alembic commands ###
