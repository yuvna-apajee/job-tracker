"""Add status column to JobApplication model

Revision ID: ec6c0963b306
Revises: 
Create Date: 2024-09-06 14:00:00

"""
from alembic import op
import sqlalchemy as sa


# Revision identifiers, used by Alembic.
revision = 'ec6c0963b306'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # Step 1: Add the 'status' column without NOT NULL constraint
    with op.batch_alter_table('job_application', schema=None) as batch_op:
        batch_op.add_column(sa.Column('status', sa.String(length=20), nullable=True))  # Allow NULL initially

    # Step 2: Update existing rows with a default value
    op.execute("UPDATE job_application SET status = 'Applied' WHERE status IS NULL")

    # Step 3: Alter the column to NOT NULL after setting the default
    with op.batch_alter_table('job_application', schema=None) as batch_op:
        batch_op.alter_column('status', existing_type=sa.String(length=20), nullable=False)


def downgrade():
    # Remove the 'status' column if rolling back
    with op.batch_alter_table('job_application', schema=None) as batch_op:
        batch_op.drop_column('status')
