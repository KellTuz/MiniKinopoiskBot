"""empty message

Revision ID: f4dcc5675d2b
Revises: 5e1a5a679f2a
Create Date: 2024-07-29 18:51:09.390732

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

import sqlalchemy_utils

# revision identifiers, used by Alembic.
revision: str = 'f4dcc5675d2b'
down_revision: Union[str, None] = '5e1a5a679f2a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('auth_group_name_a6ea08ec_like', table_name='auth_group')
    op.drop_table('auth_group')
    op.drop_index('users_user_user_permissions_permission_id_0b93982e', table_name='users_user_user_permissions')
    op.drop_index('users_user_user_permissions_user_id_20aca447', table_name='users_user_user_permissions')
    op.drop_table('users_user_user_permissions')
    op.drop_index('auth_group_permissions_group_id_b120cbf9', table_name='auth_group_permissions')
    op.drop_index('auth_group_permissions_permission_id_84c5c92e', table_name='auth_group_permissions')
    op.drop_table('auth_group_permissions')
    op.drop_index('django_session_expire_date_a5c62663', table_name='django_session')
    op.drop_index('django_session_session_key_c0390e0f_like', table_name='django_session')
    op.drop_table('django_session')
    op.drop_index('django_admin_log_content_type_id_c4bce8eb', table_name='django_admin_log')
    op.drop_index('django_admin_log_user_id_c564eba6', table_name='django_admin_log')
    op.drop_table('django_admin_log')
    op.drop_table('django_content_type')
    op.drop_table('django_migrations')
    op.drop_index('users_user_groups_group_id_9afc8d0e', table_name='users_user_groups')
    op.drop_index('users_user_groups_user_id_5f6f5a90', table_name='users_user_groups')
    op.drop_table('users_user_groups')
    op.drop_index('auth_permission_content_type_id_2f476e4b', table_name='auth_permission')
    op.drop_table('auth_permission')
    op.alter_column('films_serials_searchfilm', 'id',
               existing_type=sa.BIGINT(),
               server_default=None,
               type_=sa.Integer(),
               existing_nullable=False,
               autoincrement=True)
    op.alter_column('films_serials_searchfilm', 'name',
               existing_type=sa.VARCHAR(length=60),
               nullable=False)
    op.alter_column('films_serials_searchfilm', 'age_rating',
               existing_type=sa.BIGINT(),
               type_=sa.Integer(),
               existing_nullable=True)
    op.alter_column('films_serials_searchfilm', 'picture',
               existing_type=sa.VARCHAR(length=200),
               type_=sqlalchemy_utils.types.url.URLType(),
               existing_nullable=True)
    op.alter_column('films_serials_searchserial', 'id',
               existing_type=sa.BIGINT(),
               server_default=None,
               type_=sa.Integer(),
               existing_nullable=False,
               autoincrement=True)
    op.alter_column('films_serials_searchserial', 'name',
               existing_type=sa.VARCHAR(length=60),
               nullable=False)
    op.alter_column('films_serials_searchserial', 'age_rating',
               existing_type=sa.BIGINT(),
               type_=sa.Integer(),
               existing_nullable=True)
    op.alter_column('films_serials_searchserial', 'picture',
               existing_type=sa.VARCHAR(length=200),
               type_=sqlalchemy_utils.types.url.URLType(),
               existing_nullable=True)
    op.alter_column('history_historyfilm', 'id',
               existing_type=sa.BIGINT(),
               server_default=None,
               type_=sa.Integer(),
               existing_nullable=False,
               autoincrement=True)
    op.alter_column('history_historyfilm', 'created_at',
               existing_type=postgresql.TIMESTAMP(timezone=True),
               type_=sa.DateTime(),
               existing_nullable=False)
    op.drop_index('history_historyfilm_film_id_8684218c', table_name='history_historyfilm')
    op.drop_index('history_historyfilm_user_id_50fe0852', table_name='history_historyfilm')
    op.drop_constraint('history_historyfilm_user_id_50fe0852_fk_users_user_id', 'history_historyfilm', type_='foreignkey')
    op.drop_constraint('history_historyfilm_film_id_8684218c_fk_films_ser', 'history_historyfilm', type_='foreignkey')
    op.create_foreign_key(None, 'history_historyfilm', 'films_serials_searchfilm', ['film_id'], ['id'])
    op.create_foreign_key(None, 'history_historyfilm', 'users_user', ['user_id'], ['id'])
    op.alter_column('history_historyserial', 'id',
               existing_type=sa.BIGINT(),
               server_default=None,
               type_=sa.Integer(),
               existing_nullable=False,
               autoincrement=True)
    op.alter_column('history_historyserial', 'created_at',
               existing_type=postgresql.TIMESTAMP(timezone=True),
               type_=sa.DateTime(),
               existing_nullable=False)
    op.drop_index('history_historyserial_serial_id_f6f39cce', table_name='history_historyserial')
    op.drop_index('history_historyserial_user_id_2bf14ddb', table_name='history_historyserial')
    op.drop_constraint('history_historyserial_user_id_2bf14ddb_fk_users_user_id', 'history_historyserial', type_='foreignkey')
    op.drop_constraint('history_historyseria_serial_id_f6f39cce_fk_films_ser', 'history_historyserial', type_='foreignkey')
    op.create_foreign_key(None, 'history_historyserial', 'films_serials_searchserial', ['serial_id'], ['id'])
    op.create_foreign_key(None, 'history_historyserial', 'users_user', ['user_id'], ['id'])
    op.alter_column('users_user', 'id',
               existing_type=sa.BIGINT(),
               server_default=None,
               type_=sa.Integer(),
               existing_nullable=False,
               autoincrement=True)
    op.alter_column('users_user', 'last_login',
               existing_type=postgresql.TIMESTAMP(timezone=True),
               type_=sa.DateTime(),
               nullable=False)
    op.alter_column('users_user', 'username',
               existing_type=sa.VARCHAR(length=150),
               nullable=True)
    op.alter_column('users_user', 'first_name',
               existing_type=sa.VARCHAR(length=150),
               nullable=True)
    op.alter_column('users_user', 'last_name',
               existing_type=sa.VARCHAR(length=150),
               nullable=True)
    op.alter_column('users_user', 'email',
               existing_type=sa.VARCHAR(length=254),
               nullable=True)
    op.alter_column('users_user', 'date_joined',
               existing_type=postgresql.TIMESTAMP(timezone=True),
               type_=sa.DateTime(),
               existing_nullable=False)
    op.drop_index('users_user_phone_number_aff54ffd_like', table_name='users_user')
    op.drop_index('users_user_username_06e46fe6_like', table_name='users_user')
    op.drop_constraint('users_user_username_key', 'users_user', type_='unique')
    op.create_unique_constraint(None, 'users_user', ['email'])
    op.drop_column('users_user', 'image')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users_user', sa.Column('image', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'users_user', type_='unique')
    op.create_unique_constraint('users_user_username_key', 'users_user', ['username'])
    op.create_index('users_user_username_06e46fe6_like', 'users_user', ['username'], unique=False)
    op.create_index('users_user_phone_number_aff54ffd_like', 'users_user', ['phone_number'], unique=False)
    op.alter_column('users_user', 'date_joined',
               existing_type=sa.DateTime(),
               type_=postgresql.TIMESTAMP(timezone=True),
               existing_nullable=False)
    op.alter_column('users_user', 'email',
               existing_type=sa.VARCHAR(length=254),
               nullable=False)
    op.alter_column('users_user', 'last_name',
               existing_type=sa.VARCHAR(length=150),
               nullable=False)
    op.alter_column('users_user', 'first_name',
               existing_type=sa.VARCHAR(length=150),
               nullable=False)
    op.alter_column('users_user', 'username',
               existing_type=sa.VARCHAR(length=150),
               nullable=False)
    op.alter_column('users_user', 'last_login',
               existing_type=sa.DateTime(),
               type_=postgresql.TIMESTAMP(timezone=True),
               nullable=True)
    op.alter_column('users_user', 'id',
               existing_type=sa.Integer(),
               server_default=sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1),
               type_=sa.BIGINT(),
               existing_nullable=False,
               autoincrement=True)
    op.drop_constraint(None, 'history_historyserial', type_='foreignkey')
    op.drop_constraint(None, 'history_historyserial', type_='foreignkey')
    op.create_foreign_key('history_historyseria_serial_id_f6f39cce_fk_films_ser', 'history_historyserial', 'films_serials_searchserial', ['serial_id'], ['id'], initially='DEFERRED', deferrable=True)
    op.create_foreign_key('history_historyserial_user_id_2bf14ddb_fk_users_user_id', 'history_historyserial', 'users_user', ['user_id'], ['id'], initially='DEFERRED', deferrable=True)
    op.create_index('history_historyserial_user_id_2bf14ddb', 'history_historyserial', ['user_id'], unique=False)
    op.create_index('history_historyserial_serial_id_f6f39cce', 'history_historyserial', ['serial_id'], unique=False)
    op.alter_column('history_historyserial', 'created_at',
               existing_type=sa.DateTime(),
               type_=postgresql.TIMESTAMP(timezone=True),
               existing_nullable=False)
    op.alter_column('history_historyserial', 'id',
               existing_type=sa.Integer(),
               server_default=sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1),
               type_=sa.BIGINT(),
               existing_nullable=False,
               autoincrement=True)
    op.drop_constraint(None, 'history_historyfilm', type_='foreignkey')
    op.drop_constraint(None, 'history_historyfilm', type_='foreignkey')
    op.create_foreign_key('history_historyfilm_film_id_8684218c_fk_films_ser', 'history_historyfilm', 'films_serials_searchfilm', ['film_id'], ['id'], initially='DEFERRED', deferrable=True)
    op.create_foreign_key('history_historyfilm_user_id_50fe0852_fk_users_user_id', 'history_historyfilm', 'users_user', ['user_id'], ['id'], initially='DEFERRED', deferrable=True)
    op.create_index('history_historyfilm_user_id_50fe0852', 'history_historyfilm', ['user_id'], unique=False)
    op.create_index('history_historyfilm_film_id_8684218c', 'history_historyfilm', ['film_id'], unique=False)
    op.alter_column('history_historyfilm', 'created_at',
               existing_type=sa.DateTime(),
               type_=postgresql.TIMESTAMP(timezone=True),
               existing_nullable=False)
    op.alter_column('history_historyfilm', 'id',
               existing_type=sa.Integer(),
               server_default=sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1),
               type_=sa.BIGINT(),
               existing_nullable=False,
               autoincrement=True)
    op.alter_column('films_serials_searchserial', 'picture',
               existing_type=sqlalchemy_utils.types.url.URLType(),
               type_=sa.VARCHAR(length=200),
               existing_nullable=True)
    op.alter_column('films_serials_searchserial', 'age_rating',
               existing_type=sa.Integer(),
               type_=sa.BIGINT(),
               existing_nullable=True)
    op.alter_column('films_serials_searchserial', 'name',
               existing_type=sa.VARCHAR(length=60),
               nullable=True)
    op.alter_column('films_serials_searchserial', 'id',
               existing_type=sa.Integer(),
               server_default=sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1),
               type_=sa.BIGINT(),
               existing_nullable=False,
               autoincrement=True)
    op.alter_column('films_serials_searchfilm', 'picture',
               existing_type=sqlalchemy_utils.types.url.URLType(),
               type_=sa.VARCHAR(length=200),
               existing_nullable=True)
    op.alter_column('films_serials_searchfilm', 'age_rating',
               existing_type=sa.Integer(),
               type_=sa.BIGINT(),
               existing_nullable=True)
    op.alter_column('films_serials_searchfilm', 'name',
               existing_type=sa.VARCHAR(length=60),
               nullable=True)
    op.alter_column('films_serials_searchfilm', 'id',
               existing_type=sa.Integer(),
               server_default=sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1),
               type_=sa.BIGINT(),
               existing_nullable=False,
               autoincrement=True)
    op.create_table('auth_permission',
    sa.Column('id', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('content_type_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('codename', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['content_type_id'], ['django_content_type.id'], name='auth_permission_content_type_id_2f476e4b_fk_django_co', initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('id', name='auth_permission_pkey'),
    sa.UniqueConstraint('content_type_id', 'codename', name='auth_permission_content_type_id_codename_01ab375a_uniq'),
    postgresql_ignore_search_path=False
    )
    op.create_index('auth_permission_content_type_id_2f476e4b', 'auth_permission', ['content_type_id'], unique=False)
    op.create_table('users_user_groups',
    sa.Column('id', sa.BIGINT(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.BIGINT(), autoincrement=False, nullable=False),
    sa.Column('group_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['group_id'], ['auth_group.id'], name='users_user_groups_group_id_9afc8d0e_fk_auth_group_id', initially='DEFERRED', deferrable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users_user.id'], name='users_user_groups_user_id_5f6f5a90_fk_users_user_id', initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('id', name='users_user_groups_pkey'),
    sa.UniqueConstraint('user_id', 'group_id', name='users_user_groups_user_id_group_id_b88eab82_uniq')
    )
    op.create_index('users_user_groups_user_id_5f6f5a90', 'users_user_groups', ['user_id'], unique=False)
    op.create_index('users_user_groups_group_id_9afc8d0e', 'users_user_groups', ['group_id'], unique=False)
    op.create_table('django_migrations',
    sa.Column('id', sa.BIGINT(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('app', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('applied', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='django_migrations_pkey')
    )
    op.create_table('django_content_type',
    sa.Column('id', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('app_label', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('model', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='django_content_type_pkey'),
    sa.UniqueConstraint('app_label', 'model', name='django_content_type_app_label_model_76bd3d3b_uniq'),
    postgresql_ignore_search_path=False
    )
    op.create_table('django_admin_log',
    sa.Column('id', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('action_time', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.Column('object_id', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('object_repr', sa.VARCHAR(length=200), autoincrement=False, nullable=False),
    sa.Column('action_flag', sa.SMALLINT(), autoincrement=False, nullable=False),
    sa.Column('change_message', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('content_type_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.BIGINT(), autoincrement=False, nullable=False),
    sa.CheckConstraint('action_flag >= 0', name='django_admin_log_action_flag_check'),
    sa.ForeignKeyConstraint(['content_type_id'], ['django_content_type.id'], name='django_admin_log_content_type_id_c4bce8eb_fk_django_co', initially='DEFERRED', deferrable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users_user.id'], name='django_admin_log_user_id_c564eba6_fk_users_user_id', initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('id', name='django_admin_log_pkey')
    )
    op.create_index('django_admin_log_user_id_c564eba6', 'django_admin_log', ['user_id'], unique=False)
    op.create_index('django_admin_log_content_type_id_c4bce8eb', 'django_admin_log', ['content_type_id'], unique=False)
    op.create_table('django_session',
    sa.Column('session_key', sa.VARCHAR(length=40), autoincrement=False, nullable=False),
    sa.Column('session_data', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('expire_date', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('session_key', name='django_session_pkey')
    )
    op.create_index('django_session_session_key_c0390e0f_like', 'django_session', ['session_key'], unique=False)
    op.create_index('django_session_expire_date_a5c62663', 'django_session', ['expire_date'], unique=False)
    op.create_table('auth_group_permissions',
    sa.Column('id', sa.BIGINT(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('group_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('permission_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['group_id'], ['auth_group.id'], name='auth_group_permissions_group_id_b120cbf9_fk_auth_group_id', initially='DEFERRED', deferrable=True),
    sa.ForeignKeyConstraint(['permission_id'], ['auth_permission.id'], name='auth_group_permissio_permission_id_84c5c92e_fk_auth_perm', initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('id', name='auth_group_permissions_pkey'),
    sa.UniqueConstraint('group_id', 'permission_id', name='auth_group_permissions_group_id_permission_id_0cd325b0_uniq')
    )
    op.create_index('auth_group_permissions_permission_id_84c5c92e', 'auth_group_permissions', ['permission_id'], unique=False)
    op.create_index('auth_group_permissions_group_id_b120cbf9', 'auth_group_permissions', ['group_id'], unique=False)
    op.create_table('users_user_user_permissions',
    sa.Column('id', sa.BIGINT(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.BIGINT(), autoincrement=False, nullable=False),
    sa.Column('permission_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['permission_id'], ['auth_permission.id'], name='users_user_user_perm_permission_id_0b93982e_fk_auth_perm', initially='DEFERRED', deferrable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users_user.id'], name='users_user_user_permissions_user_id_20aca447_fk_users_user_id', initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('id', name='users_user_user_permissions_pkey'),
    sa.UniqueConstraint('user_id', 'permission_id', name='users_user_user_permissions_user_id_permission_id_43338c45_uniq')
    )
    op.create_index('users_user_user_permissions_user_id_20aca447', 'users_user_user_permissions', ['user_id'], unique=False)
    op.create_index('users_user_user_permissions_permission_id_0b93982e', 'users_user_user_permissions', ['permission_id'], unique=False)
    op.create_table('auth_group',
    sa.Column('id', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='auth_group_pkey'),
    sa.UniqueConstraint('name', name='auth_group_name_key')
    )
    op.create_index('auth_group_name_a6ea08ec_like', 'auth_group', ['name'], unique=False)
    # ### end Alembic commands ###
