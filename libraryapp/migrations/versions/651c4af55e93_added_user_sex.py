"""added User.sex

Revision ID: 651c4af55e93
Revises: ba4afc0925b2
Create Date: 2024-03-07 23:06:44.657672

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '651c4af55e93'
down_revision = 'ba4afc0925b2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('sex', sa.Enum('male', 'female', 'other', name='sexenum'), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('sex')

    # ### end Alembic commands ###
