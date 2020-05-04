
from pathlib import Path
from json_file import JSONFile


def test_json_file(tmp_path: Path):

    file_path = str(tmp_path.joinpath('test.txt'))
    JSONFile(file_path).write_dict({})
    assert JSONFile(file_path).read() == '{}'


def test_update_key_value(tmp_path: Path):

    file_path = str(tmp_path.joinpath('test.txt'))
    JSONFile(file_path).create()
    JSONFile(file_path).update_key_value(key="key", value="value")
    assert "key" in JSONFile(file_path).dict
    JSONFile(file_path).update_key_value_trim(key="detachKeys:", value="ctrl-e,e")
    assert "detachKeys" in JSONFile(file_path).dict

