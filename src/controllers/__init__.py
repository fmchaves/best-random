from ..server.instance import server
from .uniform_random_integer import end_point as ep1
from .uniform_random_custom import end_point as ep2

server.app.register_blueprint(ep1)
server.app.register_blueprint(ep2)

__all__ = ['ep1', 'ep2']
