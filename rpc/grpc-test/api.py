import time
import gevent


def get_result(u_id):
    time.sleep(1)
    if not u_id:
        return dict(data='', code=400)
    return dict(data=u_id, code=200)