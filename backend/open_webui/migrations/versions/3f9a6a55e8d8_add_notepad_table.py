"""add notepad table

Revision ID: 3f9a6a55e8d8
Revises: 3781e22d8b01
Create Date: 2024-03-11 11:30:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3f9a6a55e8d8'
down_revision = '3781e22d8b01'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'notepad',
        sa.Column('chat_id', sa.String(), nullable=False),
        sa.Column('content', sa.Text(), nullable=True),
        sa.Column('user_id', sa.String(), nullable=False),
        sa.Column('created_at', sa.BigInteger(), nullable=False),
        sa.Column('updated_at', sa.BigInteger(), nullable=False),
        sa.PrimaryKeyConstraint('chat_id')
    )

def downgrade() -> None:
    op.drop_table('notepad') 