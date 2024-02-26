# Доработать функцию из предыдущего задания таким образом, чтобы у неё появился дополнительный режим работы,
# в котором вывод разбивается на слова с удалением всех знаков пунктуации
# (их можно взять из списка string.punctuation модуля string). В этом режиме должно проверяться наличие слова в выводе.
import re
import string
import subprocess


def find_text(command, text):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if not result.returncode and text in split_text(result.stdout):
        return True
    else:
        return False


def split_text(text):
    for char in text:
        if char in string.punctuation:
            text = text.replace(char, ' ')
    list_text = re.split('[ \\n]', text)
    result = []
    for item in list_text:
        if item != '':
            result.append(item)
    print(result)
    return result
