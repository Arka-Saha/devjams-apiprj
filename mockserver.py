from fastapi import FastAPI
from faker import Faker
import uvicorn
import json

fake = Faker()
app = FastAPI()

# Load OpenAPI-like schema (can be from file or dynamically generated)
with open("openapi.json") as f:
    spec = json.load(f)

# Utility: generate fake value for a given datatype
def fake_value(dtype):
    if dtype == "string":
        return fake.word()
    elif dtype == "integer":
        return fake.random_int(1, 100)
    elif dtype == "boolean":
        return fake.boolean()
    elif dtype == "email":
        return fake.email()
    else:
        return "mock_" + dtype

# Register endpoints dynamically
for path, methods in spec["paths"].items():
    for method, details in methods.items():
        responses = details.get("responses", {})
        schema = (
            responses.get("200", {})
            .get("content", {})
            .get("application/json", {})
            .get("schema", {})
        )

        properties = schema.get("properties", {})

        async def endpoint(properties=properties):
            return {field: fake_value(prop["type"]) for field, prop in properties.items()}

        app.add_api_route(path, endpoint, methods=[method.upper()])

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
