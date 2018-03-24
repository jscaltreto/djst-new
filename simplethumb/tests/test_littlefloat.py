from unittest import TestCase

from simplethumb.spec import LittleFloat


class TestLittleFloat(TestCase):
    test_data = [
        (2.1, 2150),
        (100, 13440),
        (1020.12, 20464)
    ]
    def test_pack(self):
        for unpacked, packed in self.test_data:
            check_packed = LittleFloat.pack(unpacked)
            self.assertEqual(check_packed, packed)

    def test_unpack(self):
        for unpacked, packed in self.test_data:
            check_unpacked = LittleFloat.unpack(packed)
            self.assertAlmostEqual(check_unpacked, unpacked, delta=1)
