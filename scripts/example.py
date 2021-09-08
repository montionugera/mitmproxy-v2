import json

from mitmproxy import ctx



class CryptoGenAddressFailPlugin:
    def __init__(self):
        self.num = 0

    def response(self, flow):
        request_url = flow.request.pretty_url
        if request_url.endswith("api/cryptrofunds/withdraw/address"):
            ctx.log.info("This is some informative text.")
            self._modify_something(flow.response)

    def _modify_something(self, response):
        # json_data = json.loads(response.text)
        # json_data['data']['is_internal']
        response.text = '{"error":1093}'
        response.status_code = 400


addons = [
    CryptoGenAddressFailPlugin()
]
