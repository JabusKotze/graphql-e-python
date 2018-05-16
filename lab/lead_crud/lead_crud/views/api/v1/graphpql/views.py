from pyramid.view import view_config
from webob_graphql import serve_graphql_request

from .query import schema


@view_config(route_name='graphql',)
def graphql_view(request):

    context = {'session': request.dbsession, 'request': request}

    return serve_graphql_request(request, schema, context_value=context)
