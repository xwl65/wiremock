import json
from mitmproxy import http
def response(flow: http.HTTPFlow):
    if "quote.json" in flow.request.pretty_url :
        #data = json.loads(flow.response.content)
        #print(data)
        #data['data']['items'][1]['quote']['name'] = "mitm"
        #flow.response.text = json.dumps(data)

        with open(r"C:\tmp1.json", encoding='utf-8') as f:
            flow.response = http.HTTPResponse.make(
                200,  # (optional) status code
                f.read(),  # (optional) content
                {"Content-Type": "application/json"}  # (optional) headers
        )