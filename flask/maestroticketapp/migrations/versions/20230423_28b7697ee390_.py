"""empty message

Revision ID: 28b7697ee390
Revises: 566a11cdc2f0
Create Date: 2023-04-23 12:37:30.497636

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28b7697ee390'
down_revision = '566a11cdc2f0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('concerts_venues',
    sa.Column('concert_id', sa.Integer(), nullable=False),
    sa.Column('venue_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['concert_id'], ['concerts.id'], ),
    sa.ForeignKeyConstraint(['venue_id'], ['venues.id'], ),
    sa.PrimaryKeyConstraint('concert_id', 'venue_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('concerts_venues')
    # ### end Alembic commands ###