import graphene
from graphene import relay


class Lead(graphene.ObjectType):

    class Meta:
        interfaces = (relay.Node, )

    uuid = graphene.String(description='The lead uuid. Useful to query a specific lead')
    product = graphene.String(description='The product slug')
    email = graphene.String(description='The user email')
    name = graphene.String(description='The user name')
    cpf = graphene.String(description='The user CPF document number')
    employment_salary = graphene.String(description='The user employment salary')
    loan_reason = graphene.String(description='The reason to the loan request')
    loan_principal = graphene.String(description='The loan request value')
    loan_instalment_number = graphene.String(description='The number of instalments')
    whoami = graphene.String(description='Identify this user.')

    def resolve_whoami(self, info):
        raise ValueError('who wants to know???')


class LeadConnection(relay.Connection):

    class Meta:
        node = Lead
