import json

def generate_schema(fields, datatypes):
    schema = {
        "type": "object",
        "properties": {},
        "required": fields
    }
    for field, dtype in zip(fields, datatypes):
        schema["properties"][field] = {"type": dtype}
    return schema

def generate_openapi(fields, datatypes, path="/user", method="post"):
    schema = generate_schema(fields, datatypes)

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

    return openapi_spec


fields = ["name", "age", "email"]
datatypes = ["string", "integer", "string"]

spec = generate_openapi(fields, datatypes)

print(json.dumps(spec, indent=2))