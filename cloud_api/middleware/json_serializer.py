import json
import falcon


class JSONSerializer:
    def process_resource(self, req, resp, resource, params):
        """Process the request after routing.

        Note:
            This method is only called when the request matches
            a route to a resource.

        Args:
            req: Request object that will be passed to the
                routed responder.
            resp: Response object that will be passed to the
                responder.
            resource: Resource object to which the request was
                routed.
            params: A dict-like object representing any additional
                params derived from the route's URI template fields,
                that will be passed to the resource's responder
                method as keyword arguments.
        """
        content_type = req.content_type

        if content_type:
            if "application/json" in content_type and req.content_length:
                # Here we will just check if the request body is in proper json
                # We can use this after storing it in req.json and continue
                # using that in other places as well.
                try:
                    req.json = json.loads(req.stream.read(req.content_length))
                except Exception as ex:
                    # print(ex)
                    raise falcon.HTTPBadRequest(
                        title="Error while serializing request body.",
                        description=ex.msg)
