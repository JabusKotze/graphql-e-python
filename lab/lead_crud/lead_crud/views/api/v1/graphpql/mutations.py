from typing import Dict

import graphene
import transaction
from graphene import relay
from pyramid.request import Request

from lead_crud.models import lead as lead_models
from .schemas import Lead


def create_lead(request: Request, **lead_data: Dict[str, str]) -> Lead:

    lead = lead_models.Lead(**lead_data)

    with transaction.manager:
        lead = lead_models.Lead(**lead_data)
        request.dbsession.add(lead)

    return Lead(**lead_data)


def update_lead(request: Request, **lead_data: Dict[str, str]) -> Lead:
    # TODO: criteria to update...
    return Lead(**lead_data)


def delete_lead(request: Request, **lead_data: Dict[str, str]) -> Lead:
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

        lead = create_lead(info.context['request'], **kwargs)

        return NewLead(lead=lead)


class UpdatedLead(relay.ClientIDMutation):

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
    def mutate_and_get_payload(cls, root, info, **kwargs) -> 'UpdatedLead':

        lead = update_lead(info.context['request'], **kwargs)

        return UpdatedLead(lead=lead)


class DeletedLead(relay.ClientIDMutation):

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
    def mutate_and_get_payload(cls, root, info, **kwargs) -> 'DeletedLead':

        lead = delete_lead(info.context['request'], **kwargs)

        return DeletedLead(lead=lead)


class Mutation(graphene.ObjectType):

    new_lead = NewLead.Field()
    update_lead = UpdatedLead.Field()
    delete_lead = DeletedLead.Field()
