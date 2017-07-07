# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_record(app):
    app.session.login(Group(username="roman2", password="222"))


def test_record2(app):
    app.session.login(Group(username="roman", password="123"))