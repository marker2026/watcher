import keyboard, cv2, discord, pyautogui
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio


Bot = commands.Bot(command_prefix= "")
client = discord.Client()



chat_id = 000000000000000000 # id пользователя discord.
m_position = (0, 0) # позиция мышки которая будет проверятся.
pyautogui.FAILSAFE = False #Не рекомендую это использовать, но может не работать без этого.
photo_count = 5 # Сколько фотографий Вам будет отправенно
start_keys = 'ctrl+alt' # Клавиши которые отвечают за снятия приложения с паузы.
pause_keys = 'alt+a' # Клавиши которые отвечают за паузу. 
TOKEN = "" # Токен от дискорд бота.

@Bot.event
async def on_ready():
    pyautogui.moveTo(m_position) # переводит курсор по заданным координатам из 13 строки
    print("bot online")

async def on_script(): # функция запуска скрипта
    pyautogui.moveTo(500, 500) # переводит курсор, что-бы было понятно, когда скрипт находится в режиме ожидания
    while 1:
        await asyncio.sleep(0.5)
        if keyboard.is_pressed(start_keys): # комбинация для запуска
            await main()

async def main():
    while 1:
        await Bot.wait_until_ready()
        await asyncio.sleep(0.5)
        if keyboard.is_pressed(pause_keys): # вкл. ожидания 
            await on_script()
        if pyautogui.position() != m_position:
            await run_script()

async def run_script():
    try:
        cam = cv2.VideoCapture(0) # вкл. камеры
    except:
        cam = cv2.VideoCapture(1) 
    for i in range(photo_count):
        ret, frame = cam.read() # делаем снимок
        cv2.imwrite('cam.png', frame) # сохраняем
        photo = open('cam.png', 'rb') # откр. для чтения в двоичном режиме
        user = Bot.get_user(chat_id)
        await user.send(file=discord.File(photo))# отправка в discord
        await asyncio.sleep(1) # задержка 1 сек.
    cam.release() # откл. камеру
    await asyncio.sleep(5)
    pyautogui.moveTo(m_position)

client.loop.create_task(main())
Bot.run(TOKEN)