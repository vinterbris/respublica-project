<h1 align="center">Проект UI автотестов книжного магазина
<p align="center">
<a href="respublica.ru"> <img src="readme_resources/respublica_logo.svg" width="" height="110"> </a> </h1>


<h3 align="center">Python | Pytest | Selene | Jenkins | Allure | Selenoid | Telegram</h3>
<h3 align="center">
<img height="50" src="readme_resources/icons/Python.png"/>      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<img height="50" src="readme_resources/icons/Pytest.svg"/>      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<img height="50" src="readme_resources/icons/Selene.png"/>      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<img height="50" src="readme_resources/icons/jenkins.png"/>     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<img height="50" src="readme_resources/icons/allure.png"/>      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<img height="50" src="readme_resources/icons/Selenoid.svg"/>    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<img height="50" src="readme_resources/icons/telegram.png"/>
</h3>



---

### Реализованы тесты:
- [x] Логин
- [x] Добавление одного товара в корзину
- [x] Добавление нескольких товаров одного типа в корзину
- [x] Добавление нескольких разных товаров в корзину
- [x] Удаление одного товара из корзины
- [x] Очистка корзины


## Запуск тестов

### Локально

1. Клонируем репозиторий

```bash
git clone https://github.com/vinterbris/qa_guru_python_9_15.git
```

2. Выполняем в консоли pycharm (linux\mac):

```bash
python -m venv .venv
pip install -r requirements.txt
source .venv/bin/activate
pytest .
```

Для Windows:
```bash
python -m venv .venv
pip install -r requirements.txt
.venv/Scripts/activate
pytest .
```

<details>
  <summary><b>Устанавливаем Allure</b></summary>

Linux\Mac через Homebrew
```bash
brew install allure
```

Windows через scoop
```bash
scoop install allure
```

3. После запуска тестов получить отчёт allure командой (если добавлен в PATH): 

Linux\Mac

```bash
allure serve
```
Windows
```bash
allure.bat serve
```

[Установить из напрямую из релизов с github](https://github.com/allure-framework/allure2/releases)

<details>
    <summary>Инструкция при установке из архива</summary>

1. Скачать последнюю версию под свою систему 
2. Разархивировать в корень проекта
3. Папку (например `allure-2.27.0`) переименовываем в `allure`
4. Аллюр из архива готов, теперь запускать отчет можно из корня проекта командой:

Linux\Mac: 
```bash
allure/bin/allure serve
```

Win: 
```bash
allure/bin/allure.bat serve
```

</details>

[Другие варианты](https://allurereport.org/docs/gettingstarted-installation/)



</details>






## Запуск через jenkins+selenoid

## Пример запуска тестов
https://github.com/vinterbris/qa_guru_python_9_15/assets/21102027/61ba7f0b-e5d1-486c-bdce-e55f67388d89

## Оповещения в мессенджер
Настроена отправка оповещений в телеграм канал. Возможна настройка для email, slack, discord, skype, mattermost

<img src="readme_resources/telegram.png" height="350"/>




