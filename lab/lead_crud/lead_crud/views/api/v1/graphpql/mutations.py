from typing import Dict

import graphene
import transaction
from graphql import GraphQLError
from graphene import relay
from pyramid.request import Request
from sqlalchemy.orm.exc import NoResultFound

from lead_crud.models import lead as lead_models
from .schemas import Lead


def create_lead(request: Request, **lead_data: Dict[str, str]) -> Lead:

    with transaction.manager:
        lead = lead_models.Lead(**lead_data)
        request.dbsession.add(lead)

        request.dbsession.flush()  # Flushing to update the attribute uuid with the default value
        lead_data['uuid'] = lead.uuid

    return Lead(**lead_data)


def update_lead(request: Request, **lead_data: Dict[str, str]) -> Lead:

    try:
        lead = request.dbsession.query(lead_models.Lead).filter_by(uuid=lead_data['uuid']).one()
    except NoResultFound:
        raise GraphQLError('Invalid lead uuid')
    else:

        for attribute, value in lead_data.items():
            setattr(lead, attribute, value)

        request.dbsession.add(lead)
        return Lead(**lead_data)


def delete_lead(request: Request, **lead_data: Dict[str, str]) -> Lead:
    try:
        lead = request.dbsession.query(lead_models.Lead).filter_by(uuid=lead_data['uuid']).one()
    except NoResultFound:
        raise GraphQLError('Invalid lead uuid')
    else:
        request.dbsession.delete(lead)

    return Lead(**lead_data)


class NewLead(relay.ClientIDMutation):

    class Input:
        product = graphene.String(required=True)
        email = graphene.String(required=True)
        name = graphene.String(required=True)
        cpf = graphene.String(required=True)
        employment_salary = graphene.String(required=True)
        loan_reason = graphene.String(required=True)
        loan_principal = graphene.String(required=True)
        loan_instalment_number = graphene.String(required=True)

    lead = graphene.Field(Lead)
    @classmethod
    def mutate_and_get_payload(cls, root, info, **kwargs) -> 'NewLead':

        client_mutation_id = kwargs['client_mutation_id']
        del(kwargs['client_mutation_id'])

        lead = create_lead(info.context['request'], **kwargs)

        return NewLead(lead=lead)


class UpdatedLead(relay.ClientIDMutation):

    class Input:
        uuid = graphene.String(required=True)
        product = graphene.String()
        email = graphene.String()
        name = graphene.String()
        cpf = graphene.String()
        employment_salary = graphene.String()
        loan_reason = graphene.String()
        loan_principal = graphene.String()
        loan_instalment_number = graphene.String()

    lead = graphene.Field(Lead)
    @classmethod
    def mutate_and_get_payload(cls, root, info, **kwargs) -> 'UpdatedLead':

        client_mutation_id = kwargs.get('client_mutation_id')
        if client_mutation_id:
            del(kwargs['client_mutation_id'])

        lead = update_lead(info.context['request'], **kwargs)

        return UpdatedLead(lead=lead)


class DeletedLead(relay.ClientIDMutation):

    class Input:
        uuid = graphene.String(required=True)

    lead = graphene.Field(Lead)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **kwargs) -> 'DeletedLead':

        client_mutation_id = kwargs.get('client_mutation_id')
        if client_mutation_id:
            del(kwargs['client_mutation_id'])

        lead = delete_lead(info.context['request'], **kwargs)

        return DeletedLead(lead=lead)


class Mutation(graphene.ObjectType):

    new_lead = NewLead.Field()
    update_lead = UpdatedLead.Field()
    delete_lead = DeletedLead.Field()
