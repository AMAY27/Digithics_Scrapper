import scrapper_controller

def register_routes(app):
    app.register_blueprint(scrapper_controller.digithics_scrapper)
    return app