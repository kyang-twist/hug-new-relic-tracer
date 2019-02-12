import newrelic.agent as newrelic_agent

class TracerMiddleware:
  
  def get_transaction_name(self, req) -> str:
    return f'{req.method} {req.uri_template}'

  def process_response(self, req, resp, resource, req_succeeded):
    newrelic_agent.set_transaction_name(self.get_transaction_name(req), priority=100)
