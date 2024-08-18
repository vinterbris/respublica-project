import pydantic_settings

from respublica_ui_tests.utils import path


class Config(pydantic_settings.BaseSettings):
    login: str = None
    password: str = None
    base_url: str = "https://www.respublica.ru"
    window_width: int = 1920
    window_height: int = 1080
    timeout: float = 10.0

    selenoid: bool = False
    browser_version: str = '127.0'
    selenoid_url: str = 'http://localhost:4444'
    selenoid_ui_url: str = 'http://localhost:8080'


config = Config(_env_file=path.relative_from_root('.env'))
