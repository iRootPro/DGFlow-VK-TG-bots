import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from dotenv import load_dotenv
import os
import random


from dgflow import get_answer
from file import get_project_id


def send_answer(event, vk_api, text, lang):
    session_id = random.randint(1, 1000)
    answer = get_answer(get_project_id(), session_id, event.text, lang)
    if answer:
        vk_api.messages.send(
            user_id=event.user_id,
            message=answer,
            random_id=random.randint(1, 1000)
        )


def launch_vk_bot(token):
    vk_session = vk_api.VkApi(token=token)
    vkontakte_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            send_answer(event, vkontakte_api, event.text, 'ru')


load_dotenv()
launch_vk_bot(os.getenv('VK_TOKEN'))
