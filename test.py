import dialogue
import unittest

from handlers.client import command_start, command_help, team, test_image_handler, none_reply

from aiogram_unittest import Requester
from aiogram_unittest.handler import MessageHandler
from aiogram_unittest.types.dataset import MESSAGE


class TestBot(unittest.IsolatedAsyncioTestCase):

    async def test_message_help_handler(self):
        requester = Requester(request_handler=MessageHandler(command_help))

        message = MESSAGE.as_object(text='Довідка 🌚')
        calls = await requester.query(message)

        answer_message = calls.send_message.fetchone().text
        self.assertEqual(answer_message, dialogue.help_message)

    async def test_message_team_handler(self):
        requester = Requester(request_handler=MessageHandler(team))

        message = MESSAGE.as_object(text='Команда 💪')
        calls = await requester.query(message)

        answer_message = calls.send_message.fetchone().text
        self.assertEqual(answer_message, dialogue.team_message)

    async def test_command_start_handler(self):
        requester = Requester(request_handler=MessageHandler(command_start, commands=["start"]))

        message = MESSAGE.as_object(text="/start")
        calls = await requester.query(message)

        answer_message = calls.send_message.fetchone().text
        self.assertEqual(answer_message, dialogue.hello_message.format(name=message.from_user.first_name))

    async def test_command_help_handler(self):
        requester = Requester(request_handler=MessageHandler(command_help, commands=["help"]))

        message = MESSAGE.as_object(text="/help")
        calls = await requester.query(message)

        answer_message = calls.send_message.fetchone().text
        self.assertEqual(answer_message, dialogue.help_message)

    async def test_command_team_handler(self):
        requester = Requester(request_handler=MessageHandler(team, commands=["team"]))

        message = MESSAGE.as_object(text="/team")
        calls = await requester.query(message)

        answer_message = calls.send_message.fetchone().text
        self.assertEqual(answer_message, dialogue.team_message)

    async def test_picture_to_text_handler(self):
        requester = Requester(request_handler=MessageHandler(test_image_handler))

        message = MESSAGE.as_object(text='Test picture')
        calls = await requester.query(message)

        answer_message = calls.send_message.fetchone().text
        self.assertEqual(answer_message, "You do not find the happy life. You make it")

    async def test_process_messages_handler(self):
        requester = Requester(request_handler=MessageHandler(none_reply))

        message = MESSAGE.as_object(text='Some text')
        calls = await requester.query(message)

        answer_message = calls.send_message.fetchone().text
        self.assertEqual(answer_message, dialogue.error)


if __name__ == '__main__':
    unittest.main()
