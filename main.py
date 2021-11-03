from pypresence import Presence
import webbrowser
import string
import os
import time
import linecache

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

print('У вас имеется client_id вашего приложения? (на Discord Developers)?')
print('Напишите Да или Нет')
hasci = input()
hascitolower = hasci.lower()
if hascitolower == 'да':
    print('Напишите его')
    clientid = input()
    RPC = Presence(clientid)
    RPC.connect()
    RPC.update()
    print('Готово! Теперь вы играете в это!')
    while True:  # The presence will stay on as long as the program is running
        time.sleep(15) # Can only update rich presence every 15 seconds
elif hascitolower == 'нет':
    clearConsole()
    print('Сейчас вам будет предложено нажать любую кнопку для перехода на сайт. Там делаете следующее:')
    print('Жмем "New Application". В "Name" пишем то, во что вы будете "Играть"')
    print('Потом, если вы хотите добавить изображение, то добавляем его как иконку для проекта.')
    print('Слева выбираем раздел OAuth2, копируем Client Id и возвращаемся сюда')
    print()
    input('Нажмите любую кнопку, чтобы перейти на сайт')
    webbrowser.open('https://discord.com/developers')
    print('Как сделаете - перезапустите файл.')
    time.sleep(9999)
else:
    print('Некорректный ответ.')
    print('Давай по новой')
    exit()