"""empty message

Revision ID: f5377bbc353e
Revises: 40554a08ec26
Create Date: 2023-10-19 21:26:35.460869

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f5377bbc353e'
down_revision = '40554a08ec26'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('brief_news', schema=None) as batch_op:
        batch_op.drop_column('cover_height')
        batch_op.drop_column('cover_width')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('brief_news', schema=None) as batch_op:
        batch_op.add_column(sa.Column('cover_width', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('cover_height', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))

    # ### end Alembic commands ###
