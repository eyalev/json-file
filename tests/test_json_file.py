
from pathlib import Path
from json_file import JSONFile


def test_json_file(tmp_path: Path):

    file_path = str(tmp_path.joinpath('test.txt'))
    JSONFile(file_path).write_dict({})
    assert JSONFile(file_path).read() == '{}'


def test_update_key_value(tmp_path: Path):

    file_path = str(tmp_path.joinpath('test.txt'))
    json_file = JSONFile(file_path)
    json_file.create()
    json_file.update_key_value(key="key", value="value")
    assert "key" in json_file.dict
    json_file.update_key_value_trim(key="detachKeys:", value="ctrl-e,e")
    assert "detachKeys" in json_file.dict


def test_keep_formatting(tmp_path: Path):

    json_string_4_spaces = """\
{
    "key1": "value1",
    "key2": "value2"
}\
"""

    file_path = str(tmp_path.joinpath('test.txt'))
    json_file = JSONFile(file_path, keep_formatting=True)
    json_file.create_from_string(json_string_4_spaces)
    json_file.update_key_value(key="key", value="value")
    assert json_file.is_formatted
    assert json_file.indentation == 4

    json_string_2_spaces_and_newline = """\
{
  "key1": "value1",
  "key2": "value2"
}
"""

    file_path = str(tmp_path.joinpath('test2.txt'))
    json_file = JSONFile(file_path, keep_formatting=True)
    json_file.create_from_string(json_string_2_spaces_and_newline)
    json_file.update_key_value(key="key", value="value")
    assert json_file.is_formatted
    assert json_file.indentation == 2

    json_string = """{"key1": "value1"}"""
    json_file.override_from_string(json_string)
    json_file.update_key_value(key="key", value="value")
    assert json_file.is_not_formatted


def test_json_string_formatting():

    json_string_4_spaces = """\
{
    "key1": "value1",
    "key2": "value2"
}\
"""

    result = JSONFile.is_json_string_formatted(json_string_4_spaces)
    assert result is True
    
    json_string_2_spaces = """\
{
  "key1": "value1",
  "key2": "value2"
}\
"""

    result = JSONFile.is_json_string_formatted(json_string_2_spaces)
    assert result is True

    json_string_2_spaces_with_new_line = """
{
  "key1": "value1",
  "key2": "value2"
}
"""

    result = JSONFile.is_json_string_formatted(json_string_2_spaces_with_new_line)
    assert result is True

    json_string_no_formatting = """{"key1": "value1"}"""
    result = JSONFile.is_json_string_formatted(json_string_no_formatting)
    assert result is False
