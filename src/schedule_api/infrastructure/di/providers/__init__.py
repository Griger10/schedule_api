from dishka import Provider

from schedule_api.infrastructure.di.providers.config import ConfigProvider
from schedule_api.infrastructure.di.providers.db import DatabaseProvider


def get_providers() -> list[Provider]:
    return [
        ConfigProvider(),
        DatabaseProvider(),
    ]
