#!/usr/bin/python3

import logging
import subprocess
from aiogram import F
import os
from aiogram import Bot, Dispatcher
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command, CommandObject

TOKEN = "token" # token here

admins = {1234567890,1234567891} # admins id

timeout = 45 # timeout seconds, to apply terminal(cmd).

dp = Dispatcher()

logger = logging.getLogger(__name__)


@dp.message(Command(commands=["start"])) 
async def command_start_handler(message: Message, bot: Bot) -> None:
    if message.from_user.id in admins:
        await message.answer("hello")
    else:
        for admin in admins:
            await bot.send_message(admin,f"{message.from_user.id} - unauthorized access to command")

@dp.message(Command(commands=["send"]))
async def send_file(message: Message, command: CommandObject, bot: Bot) -> None:
    if message.from_user.id in admins:
        try:
            await bot.send_document(message.chat.id, FSInputFile(command.args))
        except Exception as error: 
            await message.answer(str(error))
    else:
        for admin in admins:
            await bot.send_message(admin,f"{message.from_user.id} - unauthorized access to command")

@dp.message(Command(commands=["screenshot"]))
async def screenshot(message: Message, command: CommandObject, bot: Bot) -> None:
    if message.from_user.id in admins:
        try:
            os.system('import -window root root.png')
            if command.args == "-no":
                await bot.send_document(message.chat.id, FSInputFile('root.png'))
            else:
                await bot.send_photo(message.chat.id, FSInputFile("root.png"))
            os.system('rm -rf root.png')
        except Exception as error: 
            await message.answer(str(error))
    else:
        for admin in admins:
            await bot.send_message(admin,f"{message.from_user.id} - unauthorized access to command")

@dp.message(F.document)
async def download(message: Message, bot: Bot):
    if message.from_user.id in admins:
        try:
            msg = await bot.send_message(message.from_user.id, "⌛")
            file = await bot.get_file(message.document.file_id)
            await bot.download_file(file.file_path, message.document.file_name)
            await bot.edit_message_text('Successfully loaded ✅',message.chat.id, msg.message_id)
        except Exception as error:
            await bot.edit_message_text(str(error), message.chat.id, msg.message_id)
    else:
        for admin in admins:
            await bot.send_message(admin,f"{message.from_user.id} - unauthorized access to command")

@dp.message(Command(commands=["cmd","c"]))
async def system(message: Message, command: CommandObject, bot : Bot) -> None:
    if message.from_user.id in admins:
        try:
            bbb = subprocess.check_output(command.args, shell=True,stderr=subprocess.STDOUT,timeout=timeout).decode('utf-8') 
            await message.answer(f'<code>{bbb}</code>') 

        except Exception as error:
            await message.answer(str(error))
    else:

       for admin in admins:
            await bot.send_message(admin,f"{message.from_user.id} - unauthorized access to command")

def main() -> None:
    bot = Bot(TOKEN, parse_mode="HTML")
    dp.run_polling(bot)

if __name__ == "__main__":
    main()
