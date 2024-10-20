"""Database creation

Revision ID: b60852cdf7f2
Revises: 
Create Date: 2024-10-20 17:25:13.845204

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b60852cdf7f2'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('fk_day_event_id', table_name='day')
    op.drop_index('fk_day_room_id', table_name='day')
    op.drop_index('fk_event_person_id', table_name='event')
    op.drop_index('fk_event_room_id', table_name='event')
    op.add_column('person', sa.Column('registered_at', sa.TIMESTAMP(), nullable=True))
    op.drop_index('fk_person_day_day_id', table_name='person_day')
    op.drop_index('fk_person_day_person_id', table_name='person_day')
    op.drop_index('fk_person_room_person_id', table_name='person_room')
    op.drop_index('fk_person_room_room_id', table_name='person_room')
    op.drop_index('fk_room_person_id', table_name='room')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('fk_room_person_id', 'room', ['person_id'], unique=False)
    op.create_index('fk_person_room_room_id', 'person_room', ['room_id'], unique=False)
    op.create_index('fk_person_room_person_id', 'person_room', ['person_id'], unique=False)
    op.create_index('fk_person_day_person_id', 'person_day', ['person_id'], unique=False)
    op.create_index('fk_person_day_day_id', 'person_day', ['day_id'], unique=False)
    op.drop_column('person', 'registered_at')
    op.create_index('fk_event_room_id', 'event', ['room_id'], unique=False)
    op.create_index('fk_event_person_id', 'event', ['person_id'], unique=False)
    op.create_index('fk_day_room_id', 'day', ['room_id'], unique=False)
    op.create_index('fk_day_event_id', 'day', ['event_id'], unique=False)
    # ### end Alembic commands ###
