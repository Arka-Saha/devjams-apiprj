import json, requests
import jsonschema, time
import statistics
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

def generate_openapi(fields, datatypes, path="/user", method="post"):
    schema = gen_scheme(fields, datatypes)

    openapi_spec = {
        "openapi": "3.0.0",
        "info": {
            "title": "Dynamic API",
            "version": "1.0.0"
        },
        "paths": {
            path: {
                method: {
                    "summary": "Auto-generated endpoint",
                    "requestBody": {
                        "required": True,
                        "content": {
                            "application/json": {
                                "schema": schema
                            }
                        }
                    },
                    "responses": {
                        "200": {
                            "description": "Success",
                            "content": {
                                "application/json": {
                                    "schema": schema
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    with open("openai.json", "a+") as f:
        json.dump(openapi_spec, f)
    return openapi_spec

schema = gen_scheme(fields, types)
spec = generate_openapi(fields, types)

latencies = []
status_codes = []
errors = 0

for _ in range(10):
    start = time.time()
    try:
        resp = requests.get(URL, timeout=3)
        latency = (time.time() - start) * 1000 #in ms
        status = resp.status_code
        latencies.append(latency)
        status_codes.append(status)
    except:
        errors+=1
latency_avg = sum(latencies) / len(latencies)
print(resp.json())
jsonschema.validate(instance=resp, schema=schema)
print(latency_avg)
