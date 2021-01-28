# watcher
Этот скрипт является переработкой [этого скрипта](https://github.com/pro100git/watcher).

Он следит за мышкой, и делает снимки с камеры после того как заметит движения.

PS На самом деле я бы мог использовать телеграмм а не дискорд, но у телеграмма не удобный API для устновки, и в принципе телеграмм местами даже менее анонимен чем дискорд. Так что я решил использовать то что мне ближе.

# Установка
* [python 3.6+](https://www.python.org/)
* git clone https://github.com/14bc034d/watcher.git
* cd watcher
* sudo python3 -m pip install -r requirements.txt

# Использование
Скрипт отсылает фотографии пользователю в дискорд, по ID (12 строка), он проверятет находится ли мышь в позиции указанной позиции, по умолчанию (0, 0).

Его можно поставить на паузу при помощи комбинаций **alt+a**, и запустить обратно комбинацией **ctrl+alt**, но это можно изменить в 16 и 17 строке.

Так же ему нужен токен от бота, его надо указать в 18 строке.

# Запуск
* sudo python3 main.py
