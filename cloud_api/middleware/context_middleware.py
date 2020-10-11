import uuid


class ContextMiddleware:

    def process_request(self, req, resp):
        """Process the request before routing it.

        Note:
            Because Falcon routes each request based on req.path, a
            request can be effectively re-routed by setting that
            attribute to a new value from within process_request().

        Args:
            req: Request object that will eventually be
                routed to an on_* responder method.
            resp: Response object that will be routed to
                the on_* responder.
        """
        # Not using this as this will add additional computation even if the
        # request is not being routed.
        # It can be used for authorization purposes.
        pass

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
        # Adding a context ID to each request in the req.context class.
        req.context.id = uuid.uuid4()
        req.context.user = "TestUser"

    def process_response(self, req, resp, resource, params):
        if req.context.id:
            print("Context ID: " + str(req.context.id))
        if hasattr(req, "json"):
            print("JSON Serialized req body: " + str(req.json))
