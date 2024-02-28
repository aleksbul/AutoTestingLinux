import pytest
from checkers import checkout, getout
import random, string
import yaml
from datetime import datetime

with open('config.yaml') as f:
    data = yaml.safe_load(f)


@pytest.fixture()
def make_folders():
    return checkout(
        f"mkdir {data['FOLDER_IN']} {data['FOLDER_OUT']} {data['FOLDER_EXTRACT']} {data['FOLDER_EXTRACT2']}", "")


@pytest.fixture()
def clear_folders():
    return checkout(
        f"rm -rf {data['FOLDER_IN']}/* {data['FOLDER_OUT']}/* {data['FOLDER_EXTRACT']}/* {data['FOLDER_EXTRACT2']}/*",
        "")


@pytest.fixture()
def make_files():
    list_of_files = []
    for i in range(data['count']):
        filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        if checkout(f"cd {data['FOLDER_IN']}; dd if=/dev/urandom of={filename} bs={data['size']} count=1 iflag=fullblock", ""):
            list_of_files.append(filename)
    return list_of_files


@pytest.fixture()
def make_subfolder():
    testfilename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    subfoldername = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    if not checkout(f"cd {data['FOLDER_IN']}; mkdir {subfoldername}", ""):
        return None, None
    if not checkout(
            f"cd {data['FOLDER_IN']}/{subfoldername}; dd if=/dev/urandom of={testfilename} bs={data['size']} count=1 iflag=fullblock",
            ""):
        return subfoldername, None
    else:
        return subfoldername, testfilename


@pytest.fixture(autouse=True)
def print_time():
    print(f'Start: {datetime.now().strftime("%H:%M:%S.%f")}')
    yield
    print(f'Stop: {datetime.now().strftime("%H:%M:%S.%f")}')


@pytest.fixture()
def make_bad_file():
    if checkout(f"cd {data['FOLDER_IN']}; 7z a {data['FOLDER_OUT']}/arx2_bad", "") and \
            checkout(f"truncate -s 1 {data['FOLDER_OUT']}/arx2_bad.7z", ""):
        return 'arx2_bad'
    return None


@pytest.fixture(autouse=True)
def write_stat():
    yield
    with open('stat.txt', 'a', encoding='utf-8') as file:
        file.write(f"{datetime.now().strftime('%H:%M:%S.%f')},   total files: {data['count']},  size: {data['size']},   "
                   f"proc load: {getout('cat /proc/loadavg')}")
