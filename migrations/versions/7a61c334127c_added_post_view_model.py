"""added post view model

Revision ID: 7a61c334127c
Revises: 3135b3eb2a71
Create Date: 2019-09-01 13:05:01.221852

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7a61c334127c'
down_revision = '3135b3eb2a71'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post_category',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('status', sa.String(length=25), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('post',
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('updated', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('view_count', sa.Integer(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('creator_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['post_category.id'], ),
    sa.ForeignKeyConstraint(['creator_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comment',
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('updated', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('status', sa.String(length=25), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('posted_by_id', sa.Integer(), nullable=False),
    sa.Column('replied_comment_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ),
    sa.ForeignKeyConstraint(['posted_by_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['replied_comment_id'], ['comment.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('post_like',
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('updated', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('status', sa.String(length=25), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('like_by_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['like_by_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('topic_view',
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('updated', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('status', sa.String(length=25), nullable=False),
    sa.Column('viewer_ip_address', sa.String(length=30), nullable=False),
    sa.Column('topic_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['topic_id'], ['post.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('topic_category')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('topic_category',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.Column('description', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('status', sa.VARCHAR(length=25), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='topic_category_pkey'),
    sa.UniqueConstraint('name', name='topic_category_name_key')
    )
    op.drop_table('topic_view')
    op.drop_table('post_like')
    op.drop_table('comment')
    op.drop_table('post')
    op.drop_table('post_category')
    # ### end Alembic commands ###
