"""This package contains the whole boilerplateapp with all of its models, views and other modules.

This particular file additionally contains the applications factory.
"""
from fastapi import FastAPI
from starlette.config import Config
import os



def create_app(env):
    """
    FastAPI web app factory method
    """
    app = FastAPI()
    config = Config(f'.env.{env}')


    # Initialize extensions
    # Prometheus metrics
    from starlette_exporter import PrometheusMiddleware, handle_metrics
    app.add_middleware(PrometheusMiddleware)
    app.add_route("/metrics", handle_metrics)

    # from boilerplateapp.extensions import db, passlib
    # db.init_app(app)
    # passlib.init_app(app)
    #
    # # Initialize handlers
    # from boilerplateapp.handlers import register_handlers
    # register_handlers(app)
    #
    # Initialize blueprints
    from boilerplateapp.api import health
    app.include_router(
        health.router,
        prefix="",
        tags=[],
        dependencies=[],
        responses={},
    )

    #
    # # Initialize custom commands
    # from boilerplateapp.cli import register_cli
    # register_cli(app)
    #
    return app
