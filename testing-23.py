from pyramid import response, config

def return_put_data(request):
    data = request.body.decode("ascii")
    resp_value = json.dumps(dict(data=data)).encode("ascii")
    return response.Response(resp_value, content_type="application/json")

def make_app():
    with config.Configurator() as cfg:
        cfg.add_route('put', '/put')
        cfg.add_view(return_put_data, route_name='put')
        app = cfg.make_wsgi_app()
    return app
