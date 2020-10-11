import falcon

from falcon.media.validators.jsonschema import validate

from cloud_api.schemas import schema_hook


@falcon.before(schema_hook)
class StorageSystemResource:
    def __init__(self):
        self.schema_name = "storage_system"

    def on_get(self, req, resp):
        # Not doing json schema validation for GET request
        ss_system_name = {"name": "old_3PAR"}
        resp.status = falcon.HTTP_200
        resp.media = {
            "ss_system": ss_system_name
        }

    def on_post(self, req, resp):
        resp.status = falcon.HTTP_201
        resp.media = "Validated the post request json using class hook from falcon"

    def on_patch(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.media = "Validated the patch request json using the class hook from falcon"
