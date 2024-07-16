"""empty message

Revision ID: 815c865ca7e0
Revises: 
Create Date: 2024-07-11 18:35:35.620054

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils

# revision identifiers, used by Alembic.
revision: str = '815c865ca7e0'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('search_film',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('name', sa.String(length=60), nullable=False),
                    sa.Column('janr', sa.String(length=60), nullable=True),
                    sa.Column('year', sa.Integer(), nullable=True),
                    sa.Column('country', sa.String(), nullable=True),
                    sa.Column('movie_length', sa.Integer(), nullable=True),
                    sa.Column('description', sa.Text(), nullable=True),
                    sa.Column('rating', sa.Float(), nullable=True),
                    sa.Column('age_rating', sa.Integer(), nullable=True),
                    sa.Column('picture', sqlalchemy_utils.types.url.URLType(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('search_serial',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('name', sa.String(length=60), nullable=False),
                    sa.Column('janr', sa.String(length=60), nullable=True),
                    sa.Column('rating', sa.Float(), nullable=True),
                    sa.Column('release_year', sa.String(length=60), nullable=True),
                    sa.Column('series_length', sa.String(length=10), nullable=True),
                    sa.Column('country', sa.String(), nullable=True),
                    sa.Column('age_rating', sa.Integer(), nullable=True),
                    sa.Column('description', sa.Text(), nullable=True),
                    sa.Column('picture', sqlalchemy_utils.types.url.URLType(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('users',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('name', sa.String(length=60), nullable=False),
                    sa.Column('email', sa.String(length=60), nullable=False),
                    sa.Column('phone_number', sa.String(length=15), nullable=False),
                    sa.Column('telegram_id', sa.BigInteger(), nullable=False),
                    sa.Column('created_at', sa.DateTime(), server_default=sa.text("TIMEZONE('utc', now())"),
                              nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'),
                    sa.UniqueConstraint('phone_number'),
                    sa.UniqueConstraint('telegram_id')
                    )
    op.create_table('history_search_film',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('user_id', sa.BigInteger(), nullable=False),
                    sa.Column('film_id', sa.BigInteger(), nullable=False),
                    sa.Column('created_at', sa.DateTime(), server_default=sa.text("TIMEZONE('utc', now())"),
                              nullable=False),
                    sa.ForeignKeyConstraint(['film_id'], ['search_film.id'], ),
                    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('history_search_serial',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('user_id', sa.BigInteger(), nullable=False),
                    sa.Column('serial_id', sa.BigInteger(), nullable=False),
                    sa.Column('created_at', sa.DateTime(), server_default=sa.text("TIMEZONE('utc', now())"),
                              nullable=False),
                    sa.ForeignKeyConstraint(['serial_id'], ['search_serial.id'], ),
                    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('history_search_serial')
    op.drop_table('history_search_film')
    op.drop_table('users')
    op.drop_table('search_serial')
    op.drop_table('search_film')
    # ### end Alembic commands ###