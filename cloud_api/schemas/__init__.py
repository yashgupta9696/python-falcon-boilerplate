import importlib
import jsonschema
import falcon


def load_schema(name, action):
    """
    Used for loading the schema from the schema file.
    :param name: name of schema file.
    :param action: action on the resource, eg. PUT, POST, etc.
    """
    schema = None
    base_schema_path = "cloud_api.schemas"

    path = base_schema_path + "." + name
    ss_schema_dict = importlib.import_module(path)

    if action != "GET":
        schema = getattr(ss_schema_dict, action + "_SCHEMA")

    return schema


def schema_hook(req, resp, resource, params, **kwargs):
    """
    Used as a hook function in falcon.before to do schema validation.
    """
    res_name = resource.schema_name
    action = kwargs.get("req_method") or req.method
    schema_dict = load_schema(res_name, action)
    if schema_dict:
        try:
            jsonschema.validate(instance=req.json, schema=schema_dict)
        except jsonschema.ValidationError as ex:
            raise falcon.HTTPBadRequest(
                title="Error while doing JSON schema validation",
                description=ex.message)
    else:
        pass
