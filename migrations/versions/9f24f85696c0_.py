"""empty message

Revision ID: 9f24f85696c0
Revises: 103e2ebc3b0e
Create Date: 2021-02-12 09:17:26.146389

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '9f24f85696c0'
down_revision = '103e2ebc3b0e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('label', sa.String(length=250), nullable=False))
    op.drop_column('tasks', 'text_task')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('text_task', mysql.VARCHAR(length=250), nullable=False))
    op.drop_column('tasks', 'label')
    # ### end Alembic commands ###
