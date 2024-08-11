import pytest


def test_imports():
    from ef_chat_bot.lib import MyApp, MyHandler

    assert MyApp
    assert MyHandler
