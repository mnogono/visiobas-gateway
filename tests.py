import unittest
from visiobas_client import VisiobasClient
from visiobas_gate_client import VisiobasGateClient
from visiobas_gate_client import ObjectType
import visiobas_logging


class TestVisiobasClient(unittest.TestCase):
    def setUp(self):
        visiobas_logging.initialize_logging()

    def test_rise_exception_on_logout(self):
        client = VisiobasClient("localhost", 8080)
        handle_value_error = False
        try:
            client.rq_logout()
        except ValueError:
            handle_value_error = True
        self.assertEqual(handle_value_error, True, "Expected ValueError exception")

    def test_login_verify_logout(self):
        client = VisiobasClient("localhost", 8080)
        client.rq_login("s.gubarev", "77777")
        # self.assertTrue(client.rq_check_auth_token(), "Authorization token check false")
        client.rq_logout()


class TestVisiobasGateClient(unittest.TestCase):
    def setUp(self):
        visiobas_logging.initialize_logging()
        self.client = VisiobasGateClient("127.0.0.1", 8080)
        self.client.rq_login("s.gubarev", "77777")

    def tearDown(self):
        self.client.rq_logout()

    def test_rq_device_list(self):
        devices = self.client.rq_devices()
        self.assertTrue(type(devices) is list)

    def test_rq_device_objects(self):
        objects = self.client.rq_device_objects(200)
        self.assertTrue(objects is not None)

    def test_rq_binary_input(self):
        objects = self.client.rq_device_object(200, ObjectType.BINARY_INPUT)
        self.assertTrue(type(objects) is list)
