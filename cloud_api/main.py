import configparser
import os
import ast
import importlib
from cloud_api.app import APIService


def main():
    conf = read_conf()

    # Making the string of middlewares into a list of names
    middlewares = ast.literal_eval(conf["middleware"])
    middleware_classes = []
    for middleware in middlewares:
        package_path, class_name = middleware.rsplit('.', 1)
        package = importlib.import_module(package_path)
        middleware_classes.append(getattr(package, class_name)())

    # DB objects if there can also be initialized here and can be passed
    app = APIService(middleware=middleware_classes)

    return app


def read_conf(path=None, section=configparser.DEFAULTSECT):
    return_dict = {}
    parser = configparser.ConfigParser()

    if path is None:
        config_file_dir = os.path.abspath(os.path.dirname(
            os.path.dirname(__file__)))
        path = os.path.join(
            config_file_dir, "etc", "cloud_api", "cloud_api.conf")

    parser.read(path)

    # Reading the items in the default section
    for item in parser.items(section):
        return_dict[item[0]] = item[1]

    return return_dict


app = main()
