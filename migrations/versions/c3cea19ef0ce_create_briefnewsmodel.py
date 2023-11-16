"""create BriefNewsModel

Revision ID: c3cea19ef0ce
Revises: 
Create Date: 2023-10-17 14:45:15.177114

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c3cea19ef0ce'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('brief_news',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cover_img', sa.String(length=256), nullable=True),
    sa.Column('cover_height', sa.Integer(), nullable=True),
    sa.Column('cover_weight', sa.Integer(), nullable=True),
    sa.Column('brief', sa.String(length=256), nullable=True),
    sa.Column('author_name', sa.String(length=256), nullable=True),
    sa.Column('author_cover', sa.String(length=256), nullable=True),
    sa.Column('authorHomePage', sa.String(length=256), nullable=True),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('excerpt', sa.Text(), nullable=True),
    sa.Column('url', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('brief_news')
    # ### end Alembic commands ###