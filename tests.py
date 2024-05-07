import unittest
import utils

class TestHashCracker(unittest.TestCase):
    def test_reverse_hash(self):
        self.assertEqual(utils.reverse_hash("73298166fc49a851a91510af1bb7311d0aaa481ba5e01bc85233b06c79e379d791e40880c34184db11fb1561e3c7ec3b82e2bf7570d3bd5a73918a306a02bdb1"), "random")

if __name__ == "__main__":
    unittest.main()