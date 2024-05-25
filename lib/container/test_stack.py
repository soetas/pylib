import unittest
from ddt import data, ddt, unpack, file_data

@ddt
class TestStack(unittest.TestCase):
  @data([], [], [])
  @unpack
  def test_push(self):
    pass
