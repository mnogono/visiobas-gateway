import certifi
import unittest
from visiobas_client import VisiobasClient
from visiobas_gate_client import VisiobasGateClient
from visiobas_object_type import ObjectType
from visiobas_property import ObjectProperty
import visiobas_logging

if __name__ == 'main':
    print(certifi.where())
    exit(0)

LOCAL = {
    "host": "http://localhost",
    "port": 8080,
    "user": "s.gubarev",
    "pwd": "77777"
}
REMOTE = {
    "host": "https://visiodesk.net",
    "port": 8443,
    "user": "canio",
    "pwd": "canio"
}
SERVER = {
    "local": LOCAL,
    "remote": REMOTE
}

USING_SERVER = "remote"

HOST = SERVER[USING_SERVER]["host"]
PORT = SERVER[USING_SERVER]["port"]
USER = SERVER[USING_SERVER]["user"]
PWD = SERVER[USING_SERVER]["pwd"]


class TestVisiobasClient(unittest.TestCase):
    def setUp(self):
        visiobas_logging.initialize_logging()
        self.client = VisiobasClient(HOST, PORT, verify=False)
        self.client.rq_login(USER, PWD)

    def tearDown(self):
        self.client.rq_logout()

    def test_get_children(self):
        objects = self.client.rq_children()
        self.assertTrue(len(objects) > 0)

        reference = objects[0][ObjectProperty.OBJECT_PROPERTY_REFERENCE.id()]
        objects = self.client.rq_children(reference)
        self.assertTrue(len(objects) >= 0)

    # def test_rise_exception_on_logout(self):
    #     client = VisiobasClient(HOST, PORT, verify=False)
    #     handle_value_error = False
    #     try:
    #         client.rq_logout()
    #     except ValueError:
    #         handle_value_error = True
    #     self.assertEqual(handle_value_error, True, "Expected ValueError exception")
    #
    # def test_login_verify_logout(self):
    #     client = VisiobasClient(HOST, PORT, verify=False)
    #     client.rq_login(USER, PWD)
    #     # self.assertTrue(client.rq_check_auth_token(), "Authorization token check false")
    #     client.rq_logout()


class TestVisiobasGateClient(unittest.TestCase):
    def setUp(self):
        visiobas_logging.initialize_logging()
        self.client = VisiobasGateClient(HOST, PORT, verify=False)
        self.client.rq_login(USER, PWD)
        # if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
        #         getattr(ssl, '_create_unverified_context', None)):
        #     ssl._create_default_https_context = ssl._create_unverified_context

    def tearDown(self):
        self.client.rq_logout()

    def test_rq_device_list(self):
        devices = self.client.rq_devices()
        self.assertTrue(type(devices) is list)
        self.assertTrue(len(devices) > 0)

    def test_rq_device_objects(self):
        objects = self.client.rq_device_objects(200)
        self.assertTrue(objects is not None)

    def test_rq_binary_input(self):
        objects = self.client.rq_device_object(200, ObjectType.BINARY_INPUT)
        self.assertTrue(type(objects) is list)
