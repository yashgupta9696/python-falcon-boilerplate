POST_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "required": ["storageSystem"],
    "additionalProperties": False,
    "properties": {
        "storageSystem": {
            "type": "object",
            "additionalProperties": False,
            "required": ["networkAddress", "type"],
            "properties": {
                "networkAddress": {
                    "type": "string",
                    "minLength": 1,
                    "maxLength": 255
                },
                "description": {
                    "type": "string",
                    "minLength": 1,
                    "maxLength": 255
                },
                "name": {
                    "type": "string",
                    "minLength": 1,
                    "maxLength": 255
                },
                "type": {
                    "type": "string",
                    "enum": [
                        "test_SS"
                    ]
                },
                "tags": {
                    "type": "array",
                    "uniqueItems": True,
                    "minItems": 1,
                    "items": {
                        "type": "string",
                        "minLength": 36,
                        "maxLength": 36
                    }
                }
            }
        }
    }
}

PATCH_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "required": ["storageSystem"],
    "additionalProperties": False,
    "properties": {
        "storageSystem": {
            "type": "object",
            "additionalProperties": False,
            "minProperties": 1,
            "properties": {
                "networkAddress": {
                    "type": "string",
                    "minLength": 1,
                    "maxLength": 255
                },
                "description": {
                    "type": "string",
                    "maxLength": 255
                },
                "name": {
                    "type": "string",
                    "maxLength": 255
                },
                "tags": {
                    "type": "array",
                    "uniqueItems": True,
                    "items": {
                        "type": "string",
                        "minLength": 36,
                        "maxLength": 36
                    }
                },
                "ports": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "additionalProperties": False,
                        "required": ["networkAddress", "managed"],
                        "properties": {
                            "networkAddress": {
                                "type": "string"
                            },
                            "managed": {
                                "type": "boolean"
                            }
                        }
                    }
                }
            }
        }
    }
}
