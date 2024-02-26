import subprocess

FOLDER_IN = "/home/ubuntu/tst"
FOLDER_OUT = "/home/ubuntu/out"
FOLDER_EXTRACT = "/home/ubuntu/folder_test"


def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if not result.returncode and text in result.stdout:
        return True
    else:
        return False


def test_step1():
    res1 = checkout(f"cd {FOLDER_IN}; 7z a {FOLDER_OUT}/arx2", "Everything is Ok")
    res2 = checkout(f"cd {FOLDER_OUT}; 7z l arx2.7z", "test.txt")
    assert res1 and res2, "test1 FAIL"


def test_step2():
    res1 = checkout(f"cd {FOLDER_OUT}; 7z x arx2.7z -o{FOLDER_EXTRACT} -y", "Everything is Ok")
    res2 = checkout(f"ls {FOLDER_EXTRACT}", "tst_2")
    res3 = checkout(f"ls {FOLDER_EXTRACT}/tst_2", "test.txt")
    assert res1 and res2 and res3, "test2 FAIL"

