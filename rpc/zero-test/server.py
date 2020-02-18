import zerorpc

class ResultRPC(object):
    def get_result(self, data):
        if not data:
            return dict(data='', code=400)
        u_id = data.get('u_id')
        return dict(data=u_id, code=200)

s = zerorpc.Server(ResultRPC())
s.bind("tcp://0.0.0.0:4242")
s.run()
