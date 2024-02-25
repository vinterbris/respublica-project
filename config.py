import pydantic_settings

WEB_URL = "https://www.respublica.ru"


class Config(pydantic_settings.BaseSettings):
    base_url: str = WEB_URL
    window_width: int = 1920
    window_height: int = 1080
    timeout: float = 10.0
