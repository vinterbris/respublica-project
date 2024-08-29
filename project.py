import dotenv
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


config = Config(_env_file=dotenv.find_dotenv())

if __name__ == '__main__':
    """
    Run config.py to check config values on start. Used for debugging
    """
    print(config.__repr__())