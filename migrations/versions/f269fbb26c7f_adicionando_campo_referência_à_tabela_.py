"""Adicionando campo referência à tabela Endereco

Revision ID: f269fbb26c7f
Revises: f37a2be08737
Create Date: 2020-06-06 13:12:16.553441

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f269fbb26c7f'
down_revision = 'f37a2be08737'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('endereco', sa.Column('referencia', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('endereco', 'referencia')
    # ### end Alembic commands ###
