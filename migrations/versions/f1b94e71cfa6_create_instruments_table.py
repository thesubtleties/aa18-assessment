"""Create instruments table

Revision ID: f1b94e71cfa6
Revises: 
Create Date: 2024-12-15 21:24:38.618954

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f1b94e71cfa6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('instruments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_bought', sa.Date(), nullable=False),
    sa.Column('nickname', sa.String(length=50), nullable=False),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('maker', sa.String(length=50), nullable=True),
    sa.Column('type', sa.String(length=50), nullable=False),
    sa.Column('used', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('instruments')
    # ### end Alembic commands ###
