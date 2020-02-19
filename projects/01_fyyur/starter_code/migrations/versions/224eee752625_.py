"""Set up show table and model relationships

Revision ID: 224eee752625
Revises: 8c6ddf1da233
Create Date: 2020-02-11 18:25:58.919833

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '224eee752625'
down_revision = '8c6ddf1da233'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('show',
                    sa.Column('venue_id', sa.Integer(), nullable=False),
                    sa.Column('artist_id', sa.Integer(), nullable=False),
                    sa.Column('start_time', sa.DateTime(), nullable=False,
                              server_default=sa.func.current_timestamp()),
                    sa.ForeignKeyConstraint(['artist_id'], ['artist.id'], ),
                    sa.ForeignKeyConstraint(['venue_id'], ['venue.id'], ),
                    sa.PrimaryKeyConstraint('venue_id', 'artist_id', 'start_time')
                    )
    op.add_column('artist', sa.Column(
        'seeking_description', sa.String(), nullable=True))
    op.add_column('artist', sa.Column(
        'seeking_venue', sa.Boolean(), nullable=True))
    op.add_column('artist', sa.Column(
        'website', sa.String(length=500), nullable=True))
    op.add_column('venue', sa.Column(
        'genres', sa.ARRAY(sa.String()), nullable=True))
    op.add_column('venue', sa.Column(
        'seeking_description', sa.String(), nullable=True))
    op.add_column('venue', sa.Column(
        'seeking_talent', sa.Boolean(), nullable=True))
    op.add_column('venue', sa.Column(
        'website', sa.String(length=500), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('venue', 'website')
    op.drop_column('venue', 'seeking_talent')
    op.drop_column('venue', 'seeking_description')
    op.drop_column('venue', 'genres')
    op.drop_column('artist', 'website')
    op.drop_column('artist', 'seeking_venue')
    op.drop_column('artist', 'seeking_description')
    op.drop_table('show')
    # ### end Alembic commands ###
