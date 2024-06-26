"""initial migration

Revision ID: 1b2329cd0eec
Revises: 
Create Date: 2024-04-13 21:54:20.748608

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1b2329cd0eec'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('event',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.Column('start_date', sa.DateTime(), nullable=False),
    sa.Column('end_date', sa.DateTime(), nullable=False),
    sa.Column('venue', sa.String(length=100), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('polls',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question', sa.String(length=100), nullable=False),
    sa.Column('option1', sa.String(length=100), nullable=False),
    sa.Column('option2', sa.String(length=100), nullable=False),
    sa.Column('option3', sa.String(length=100), nullable=True),
    sa.Column('option4', sa.String(length=100), nullable=True),
    sa.Column('count_option1', sa.Integer(), nullable=False),
    sa.Column('count_option2', sa.Integer(), nullable=False),
    sa.Column('count_option3', sa.Integer(), nullable=True),
    sa.Column('count_option4', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('semester',
    sa.Column('semester_name', sa.String(length=100), nullable=False),
    sa.Column('recruitment_started', sa.DateTime(), nullable=True),
    sa.Column('recruitment_end', sa.DateTime(), nullable=True),
    sa.Column('recruitment_status', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('semester_name')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('phone', sa.String(length=14), nullable=False),
    sa.Column('semester', sa.String(length=4), nullable=False),
    sa.Column('dob', sa.Date(), nullable=False),
    sa.Column('blood_group', sa.String(length=3), nullable=False),
    sa.Column('department', sa.String(length=35), nullable=False),
    sa.Column('password', sa.String(length=100), nullable=False),
    sa.Column('approved', sa.Boolean(), nullable=True),
    sa.Column('designation', sa.String(length=20), nullable=True),
    sa.Column('joined_semester', sa.String(length=10), nullable=False),
    sa.Column('reset_token', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone'),
    sa.UniqueConstraint('reset_token'),
    sa.UniqueConstraint('student_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('semester')
    op.drop_table('polls')
    op.drop_table('event')
    # ### end Alembic commands ###
