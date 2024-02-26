import subprocess

FOLDER_OUT = "/home/ubuntu/out"


def getout(cmd):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    return result.stdout.upper()


def test_step1():
    res1 = getout(f"crc32 {FOLDER_OUT}/arx2.7z")
    res2 = getout(f"7z h {FOLDER_OUT}/arx2.7z")
    assert res1 in res2, "test1 FAIL"
