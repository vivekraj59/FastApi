"""empty message

Revision ID: 33c9e790cd70
Revises: 888ca6edcdb3
Create Date: 2023-09-11 07:51:00.040228

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '33c9e790cd70'
down_revision: Union[str, None] = '888ca6edcdb3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
