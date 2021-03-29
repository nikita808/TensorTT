import os
import json

path = os.getcwd().split("\\")
dirname = path[len(path) - 1]

with open('settings.json', 'r+') as f:
    settings = json.load(f)


def set_file_name(url: str):
    if 'https://' in url:
        url = url.replace('https://', f'[{dirname}]/')
    else:
        url = url.replace('http://', f'[{dirname}]/')

    split_url = url.split('/')
    split_url = split_url[:-1]
    name = ' '.join([str(item) for item in split_url])
    name += '.txt'
    return name


def print_settings(to_change: bool):
    if not to_change:
        print('Настройки: \n'
              f'Максимальное количество символов в строке: {settings["max_symbols_in_line"]}\n'
              f'Разделить текст по абзацам: {settings["separate_text_by_paragraphs"]}\n'
              f'\nХотите изменить настройки? Y/N?')
    else:
        print('Настройки: \n'
              f'1: Максимальное количество символов в строке: {settings["max_symbols_in_line"]}\n'
              f'2: Разделить текст по абзацам: {settings["separate_text_by_paragraphs"]}\n')


def change_settings():
    print_settings(False)
    user_input = input()
    if user_input.lower() == 'y':
        print('Выберите настройку, которую хотите изменить: \n')
        print_settings(True)
        i = int(input())
        if i == 1:
            print("Введите максимальное количество символов в строке: \n")
            settings["max_symbols_in_line"] = int(input())
            with open('settings.json', 'w', encoding='utf-8') as f:
                json.dump(settings, f)
            print(f"Теперь максимальное количество символов в строке = {settings['max_symbols_in_line']}\n")
        elif i == 2:
            if settings['separate_text_by_paragraphs']:
                settings["max_symbols_in_line"] = False
                with open('settings.json', 'w', encoding='utf-8') as f:
                    json.dump(settings, f)
                print("Теперь текст не разделяется по абзацам")
            else:
                settings['max_symbols_in_line'] = True
                with open('settings.json', 'w', encoding='utf-8') as f:
                    json.dump(settings, f)
                print("Теперь текст разделяется по абзацам")
    elif user_input.lower() == 'n':
        pass
    else:
        print('Введите ответ в формате "Y/N"')
