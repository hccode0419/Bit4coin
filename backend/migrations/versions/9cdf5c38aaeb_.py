"""empty message

Revision ID: 9cdf5c38aaeb
Revises: 
Create Date: 2024-08-01 16:15:57.685114

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9cdf5c38aaeb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('symbol', sa.String(), nullable=False),
    sa.Column('position_type', sa.String(), nullable=False),
    sa.Column('enter_time', sa.DateTime(), nullable=False),
    sa.Column('close_time', sa.DateTime(), nullable=False),
    sa.Column('entry_price', sa.Float(), nullable=False),
    sa.Column('purchase_price', sa.Float(), nullable=False),
    sa.Column('eval_price', sa.Float(), nullable=False),
    sa.Column('eval_PAL', sa.Float(), nullable=False),
    sa.Column('revenue_rate', sa.Float(), nullable=False),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.Column('profit_end', sa.Float(), nullable=False),
    sa.Column('loss_end', sa.Float(), nullable=False),
    sa.Column('owner_email', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_name', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.Text(), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=True),
    sa.Column('api_key', sa.Text(), nullable=False),
    sa.Column('api_key_secret', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_index(op.f('ix_users_user_name'), 'users', ['user_name'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_user_name'), table_name='users')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_table('item')
    # ### end Alembic commands ###
