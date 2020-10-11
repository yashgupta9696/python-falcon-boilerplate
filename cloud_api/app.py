import falcon
from cloud_api.resources import storage_system


class APIService(falcon.API):
    def __init__(self, cfg=None, *args, **kwargs):
        super().__init__(middleware=kwargs["middleware"])
        self.cfg = cfg

        storage_system_res = storage_system.StorageSystemResource()

        self.add_route('/storage-system', storage_system_res)


if __name__ == "__main__":
    app = APIService()
