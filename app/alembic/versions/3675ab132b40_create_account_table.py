"""create account table

Revision ID: 3675ab132b40
Revises: 
Create Date: 2022-05-28 01:17:52.773581

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3675ab132b40'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'account',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('description', sa.Unicode(200)),
    )

def downgrade():
    op.drop_table('account')