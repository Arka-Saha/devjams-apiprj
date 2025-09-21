import json, requests
import jsonschema, time

# fields = list(map(str, input("Fields> ").split(", ")))
# types = list(map(str, input("Data types> ").split(", ")))
fields = ["id", "name", "role"]
types = ["integer", "string", "string"]
URL = r"http://127.0.0.1:5000/api/data"

def gen_scheme(fields, types):
    schema = {
    # "type": "object",
    "properties": {},
    "required": fields
    }

    for f, t in zip(fields, types):
        schema["properties"][f] = {"type": t}
    return schema
schema = gen_scheme(fields, types)

start = time.time()
resp = requests.get(URL)
latency = (time.time() - start) * 1000 #in ms

print(resp.json())
jsonschema.validate(instance=resp, schema=schema)
status = resp.status_code
print(latency)
