"""empty message

Revision ID: 88b72134e16e
Revises: 3bbfa2eb9cbc
Create Date: 2023-04-23 12:33:24.745784

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '88b72134e16e'
down_revision = '3bbfa2eb9cbc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bands_concerts',
    sa.Column('band_id', sa.Integer(), nullable=False),
    sa.Column('concert_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['band_id'], ['bands.id'], ),
    sa.ForeignKeyConstraint(['concert_id'], ['concerts.id'], ),
    sa.PrimaryKeyConstraint('band_id', 'concert_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('bands_concerts')
    # ### end Alembic commands ###
