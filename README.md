# python-falcon-boilerplaye
This is the boilerplate code for Falcon 2.0.0 Python web application Framework.

## Configuration files
 -> cloud_api.conf: For now this config only supports middleware implementation, however later on this can be used just like settings.py in Django Framework and that work has to be done inside the main.py file
 For now you can provide the middleware classes as list items inside the key middleware.

 -> gunicorn.conf: This configuration file is being used by gunicorn to spawn off the falcon wsgi workers.

## Middlewares
 -> Context Middleware: This middleware puts the context ID and the User name in the request context class which can be accessed later in the other layers.

 -> JSON Serializer: This middleware verifies the JSON body of the request, in case JSON is not proper HTTPBadRequest exception is being raised. If it is proper the JSON body is saved inside "<request_object>.json" field.

### For more information of the implementations please feel free to raise an issue. Will update more.
