import graphene
from graphene import relay
from sqlalchemy.orm.exc import NoResultFound

from lead_crud.models import lead as lead_models
from . import mutations
from . import schemas


class Query(graphene.ObjectType):

    node = relay.Node.Field()
    leads = graphene.List(schemas.Lead, uuid=graphene.UUID())
    lead = graphene.Field(schemas.Lead, uuid=graphene.UUID())

    def resolve_leads(self, info, **kwargs):
        return info.context['request'].dbsession.query(lead_models.Lead).all()

    def resolve_lead(self, info, **kwargs):

        try:
            return info.context['request'].dbsession.query(lead_models.Lead).filter(
                lead_models.Lead.uuid == kwargs.get('uuid').hex
            ).one()
        except NoResultFound:
            return


schema = graphene.Schema(query=Query, mutation=mutations.Mutation, types=[schemas.Lead])
