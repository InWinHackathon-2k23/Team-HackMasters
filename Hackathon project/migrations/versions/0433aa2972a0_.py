"""empty message

Revision ID: 0433aa2972a0
Revises: 33482b456bc8
Create Date: 2023-12-30 10:40:12.265080

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0433aa2972a0'
down_revision = '33482b456bc8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Destination', schema=None) as batch_op:
        batch_op.add_column(sa.Column('train_no_to', sa.String(length=20), nullable=True))
        batch_op.add_column(sa.Column('train_no_from', sa.String(length=20, collation=ForeignKey('Trains.train_no')), nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key(None, 'Trains', ['train_no_to'], ['train_no'])
        batch_op.drop_column('train_no')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Destination', schema=None) as batch_op:
        batch_op.add_column(sa.Column('train_no', sa.VARCHAR(length=20), nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key(None, 'Trains', ['train_no'], ['train_no'])
        batch_op.drop_column('train_no_from')
        batch_op.drop_column('train_no_to')

    # ### end Alembic commands ###
