
import os
from channels.routing import ProtocolTypeRouter, URLRouter

from django.core.asgi import get_asgi_application

from django.urls import path
from asycs.custom_func.consumers import PerformActionAsync

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'job_test.settings')

django_app = get_asgi_application()


application = ProtocolTypeRouter({
    "http": django_app,
    "websocket": URLRouter([
        path("ws/add/", PerformActionAsync.as_asgi()),
    ])
})