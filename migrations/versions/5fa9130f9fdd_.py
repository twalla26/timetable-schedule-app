"""empty message

Revision ID: 5fa9130f9fdd
Revises: ad5f0ee8c4b8
Create Date: 2022-12-11 13:59:44.798379

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5fa9130f9fdd'
down_revision = 'ad5f0ee8c4b8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('plan', schema=None) as batch_op:
        batch_op.add_column(sa.Column('needed_time', sa.String(length=150), nullable=False))
        batch_op.add_column(sa.Column('overlapped_schedule', sa.PickleType(), nullable=True))
        batch_op.add_column(sa.Column('best_time', sa.Text(), nullable=True))
        batch_op.drop_column('input_way')

    with op.batch_alter_table('schedule', schema=None) as batch_op:
        batch_op.alter_column('timetable_array',
               existing_type=sa.TEXT(),
               type_=sa.PickleType(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('schedule', schema=None) as batch_op:
        batch_op.alter_column('timetable_array',
               existing_type=sa.PickleType(),
               type_=sa.TEXT(),
               existing_nullable=True)

    with op.batch_alter_table('plan', schema=None) as batch_op:
        batch_op.add_column(sa.Column('input_way', sa.VARCHAR(length=150), nullable=False))
        batch_op.drop_column('best_time')
        batch_op.drop_column('overlapped_schedule')
        batch_op.drop_column('needed_time')

    # ### end Alembic commands ###
