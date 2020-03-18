# coding: utf-8
from pprint import pprint
import csv
import re


with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
pprint(contacts_list)

new_phonebook = list()
new_phonebook.append(contacts_list[0])
contacts_list.pop(0)
for contact in contacts_list:
    pattern_fio = re.compile("(\w*)\s*(\w*)\s*(\w*)")
    fio_list = [contact[0], contact[1], contact[2]]
    fio = ' '.join(fio_list)
    sub_pattern_lname = r"\1"
    sub_pattern_fname = r"\2"
    sub_pattern_sname = r"\3"
    contact[0] = pattern_fio.sub(sub_pattern_lname, fio)
    contact[1] = pattern_fio.sub(sub_pattern_fname, fio)
    contact[2] = pattern_fio.sub(sub_pattern_sname, fio)

    pattern_phone = re.compile("(\+7|8)\s*\(?(\d{3})[\)\-]?\s*(\d{3})\-?(\d{2})\-?(\d{2})(\s*\(?(доб\.\s*\d{4})\)?)?")
    sub_pattern_phone = r"+7(\2)\3-\4-\5 \7"
    contact[5] = pattern_phone.sub(sub_pattern_phone, contact[5]).rstrip()

    double = False
    for new_contact in new_phonebook:
        if new_contact[0] == contact[0] and new_contact[1] == contact[1] and (new_contact[2] == contact[2] or new_contact[2] == '' or contact[2] == ''):
            new_contact[0] = max(new_contact[0],contact[0])
            new_contact[1] = max(new_contact[1], contact[1])
            new_contact[2] = max(new_contact[2], contact[2])
            new_contact[3] = max(new_contact[3], contact[3])
            new_contact[4] = max(new_contact[4], contact[4])
            new_contact[5] = max(new_contact[5], contact[5])
            new_contact[6] = max(new_contact[6], contact[6])
            double = True
            break

    if not double:
        new_phonebook.append(contact)


# код для записи файла в формате CSV
with open("phonebook.csv", "w",  newline='', encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(new_phonebook)
