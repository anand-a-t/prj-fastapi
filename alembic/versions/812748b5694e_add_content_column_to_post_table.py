"""add content column to post table

Revision ID: 812748b5694e
Revises: 25de25bb369e
Create Date: 2024-06-11 11:32:43.719633

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '812748b5694e'
down_revision: Union[str, None] = '25de25bb369e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_column('posts', 'content')
