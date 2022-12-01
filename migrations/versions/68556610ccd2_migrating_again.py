"""migrating again

Revision ID: 68556610ccd2
Revises: 563663343487
Create Date: 2022-12-01 16:28:06.662126

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '68556610ccd2'
down_revision = '563663343487'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('accounts', schema=None) as batch_op:
        batch_op.alter_column('account_name',
               existing_type=sa.VARCHAR(length=40),
               type_=sa.String(length=50),
               existing_nullable=False)

    with op.batch_alter_table('budgets', schema=None) as batch_op:
        batch_op.add_column(sa.Column('category_id', sa.Integer(), nullable=False))
        batch_op.drop_constraint('budgets_categoryId_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'categories', ['category_id'], ['id'])
        batch_op.drop_column('categoryId')

    with op.batch_alter_table('categories', schema=None) as batch_op:
        batch_op.alter_column('category_name',
               existing_type=sa.VARCHAR(length=40),
               type_=sa.String(length=50),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('categories', schema=None) as batch_op:
        batch_op.alter_column('category_name',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=40),
               existing_nullable=False)

    with op.batch_alter_table('budgets', schema=None) as batch_op:
        batch_op.add_column(sa.Column('categoryId', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('budgets_categoryId_fkey', 'categories', ['categoryId'], ['id'])
        batch_op.drop_column('category_id')

    with op.batch_alter_table('accounts', schema=None) as batch_op:
        batch_op.alter_column('account_name',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=40),
               existing_nullable=False)

    # ### end Alembic commands ###
