from visiobas_client import VisiobasClient
from object_type import ObjectType


class VisiobasGateClient(VisiobasClient):
    def __init__(self, host, port):
        VisiobasClient.__init__(self, host, port)

    def rq_get_device_objects(self, device_id, object_id=None, object_type=None):
        """
        Request list of object under certain device
        :param device_id: device identifier
        :type device_id: int
        :param object_id: Optional object identifier
        :type object_id: int
        :param object_type: Optional object type
        :type object_type: object_type.ObjectType
        """
        if object_id is not None and object_type is not None:
            url = "{}/get/{}/{}/{}".format(self.get_addr(), device_id, object_id, object_type.name)
        else:
            url = "{}/get/{}".format(self.get_addr(), device_id)
        return self.get(url)

    def rq_devices(self) -> list:
        """
        Request of all available devices
        :return:
        """
        url = "{}/vbas/gate/getDevices".format(self.get_addr())
        return self.get(url)

    def rq_device_objects(self, device_id):
        url = "{}/vbas/gate/get/{}/empty".format(self.get_addr(), device_id)
        return self.get(url)

    def rq_device_object(self, device_id, object_id):
        """
        Request object
        :param device_id: device id
        :type device_id: int
        :param object_id: one of supported object type
        :type object_id: object_type.ObjectType
        :return:
        """
        url = "{}/vbas/gate/get/{}/{}".format(self.get_addr(), device_id, object_id.id())
        return self.get(url)
