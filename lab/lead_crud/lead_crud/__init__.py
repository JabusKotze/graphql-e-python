from pyramid.config import Configurator


def main(global_config, **settings):

    config = Configurator(settings=settings)

    # Models
    config.include('.models')

    # Routes
    config.include('.views.api')

    config.scan()

    return config.make_wsgi_app()
