from pprint import pprint
import io

def custom_write(file_name, strings):
    f = open(file_name, 'w', encoding = 'utf-8')
    for s in strings:
        f.write(f"{s}\n")
    f.close()
    f = open(file_name, 'r', encoding = 'utf-8')
    end_off_file = False
    string_positions = {}
    line_number = 1
    bytes_from_begin_file = 0
    while end_off_file == False:
        current_line = f.readline()
        if not current_line == '':
            string_positions[(line_number, bytes_from_begin_file)] = current_line.rstrip()
            line_number = line_number + 1
            bytes_from_begin_file = f.tell()
        else:
            end_off_file = True
    f.close()
    return string_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)

