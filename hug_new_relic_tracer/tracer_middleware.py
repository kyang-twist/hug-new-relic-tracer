import newrelic

class TracerMiddleware:
  
  def get_transaction_name(self, req) -> str:
    return f'{req.method} {req.relative_uri}'

  def process_request(self, req, resp):
    newrelic.agent.set_transaction_name(self.get_transaction_name(req))
