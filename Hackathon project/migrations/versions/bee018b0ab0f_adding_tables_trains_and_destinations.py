"""Adding tables trains and destinations

Revision ID: bee018b0ab0f
Revises: 
Create Date: 2023-12-30 08:12:34.952791

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bee018b0ab0f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Trains',
    sa.Column('train_no', sa.Integer(), nullable=False),
    sa.Column('depart', sa.DateTime(), nullable=True),
    sa.Column('arrival', sa.DateTime(), nullable=True),
    sa.Column('fare', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('train_no')
    )
    op.create_table('Destination',
    sa.Column('destination_name', sa.String(length=120), nullable=False),
    sa.Column('dest_city', sa.String(length=120), nullable=False),
    sa.Column('train_no', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['train_no'], ['Trains.train_no'], ),
    sa.PrimaryKeyConstraint('destination_name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Destination')
    op.drop_table('Trains')
    # ### end Alembic commands ###
