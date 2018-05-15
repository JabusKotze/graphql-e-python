import uuid

import sqlalchemy as sa
import sqlalchemy_utils as sa_utils

from .meta import Base


class Lead(Base):

    __tablename__ = 'leads'

    id = sa.Column(sa.Integer, primary_key=True)

    uuid = sa.Column(sa.String(32), default=lambda: uuid.uuid4().hex)

    product = sa.Column(sa.String(100), nullable=False)
    email = sa.Column(sa.String(255), nullable=False)
    name = sa.Column(sa.String(100), nullable=False)
    cpf = sa.Column(sa.String(20), nullable=False)
    employment_salary = sa.Column(sa.String(10), nullable=False)
    loan_reason = sa.Column(sa.String(100), nullable=False)
    loan_principal = sa.Column(sa.String(10), nullable=False)
    loan_instalment_number = sa.Column(sa.String(3), nullable=False)


sa.Index('lead_name_index', Lead.name, unique=True)
sa.Index('lead_cpf_index', Lead.cpf, unique=True)
sa.Index('lead_email_index', Lead.email, unique=True)
sa.Index('lead_loan_reason_index', Lead.loan_reason, unique=True)
