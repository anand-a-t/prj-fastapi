"""create posts table

Revision ID: 25de25bb369e
Revises: 
Create Date: 2024-06-11 11:22:03.388266

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '25de25bb369e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                             sa.Column('title', sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_table('posts')
