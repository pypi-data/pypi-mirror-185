import os

import httpx
import pytest

from authup import Authup
from authup.plugins.httpx import AuthupHttpx


@pytest.fixture(scope="session", autouse=True)
def authup_instance():
    authup = Authup(
        url=os.getenv("AUTHUP_URL"),
        username=os.getenv("AUTHUP_USERNAME"),
        password=os.getenv("AUTHUP_PASSWORD"),
    )
    return authup


@pytest.fixture(scope="session", autouse=True)
def robot_creds(authup_instance):
    secret = os.getenv("AUTHUP_ROBOT_SECRET")

    auth = AuthupHttpx(
        url=authup_instance.settings.url,
        username=authup_instance.settings.username,
        password=authup_instance.settings.password.get_secret_value(),
    )

    r = httpx.get(authup_instance.settings.url + "/robots", auth=auth)

    robot_id = r.json()["data"][0]["id"]

    print(r.json())

    return robot_id, secret
