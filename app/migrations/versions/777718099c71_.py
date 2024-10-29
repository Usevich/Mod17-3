"""empty message

Revision ID: 777718099c71
Revises: 55d14325f8ec
Create Date: 2024-08-30 15:48:27.930855

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '777718099c71'
down_revision: Union[str, None] = '55d14325f8ec'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
