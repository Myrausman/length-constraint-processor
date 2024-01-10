import pytest


def test_process_list():
  assert process_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 5, 7]
  print(True)
  with pytest.raises(ValueError):
    process_list([1, 2, 3, 4, 5, 6, 7, 8, 9])
  print(True)
test_process_list()
