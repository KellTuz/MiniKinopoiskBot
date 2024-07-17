# MiniKinopoisk

## Описание

Телеграмм бот для поиска фильмов, мини аналог сайта Кинопоиск.\
Стек: aiogram, SQLAlchemy

## Установка

Следуйте инструкциям ниже для установки и запуска бота в телеграм.

### Шаги установки

1. Клонируйте репозиторий

    ```bash
    git clone https://github.com/KellTuz/MiniKinopoiskBot.git
    cd MiniKinopoiskBot
    ```

2. Создайте и активируйте виртуальное окружение

   - Windows
        ```bash
        python -m venv venv
        venv\Scripts\activate
        ```

   - Linux and MacOS
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3. Установите зависимости

    ```bash
    pip install -r requirements.txt
    ```
   
4. Получите персональный токен в телеграм у BotFather и поместите его\
в файл .env (смотрите пример в .env.template)

5. Скопируйте и выполните код из файла "mini_kinopoisk.sql" в своей субд
   (рекомендуется использовать PostqreSQL)

6. Запустите бота командой

    - Windows
         ```python
         cd MiniKinopoiskBot
         python main.py
         ```
   
    - Linux and MacOS
        ```python
        cd MiniKinopoiskBot
        python3 main.py
        ```
      
## Возможности бота
1. В боте присутствует регистрация (необходимо ввести: имя, почту и номер телефона). 
Она делается единожды и в дальнейшем больше не потребуется.
2. Основной функционал находиться в кнопке "Фильмы / Сериалы":
* Найти фильм / сериал - находит фильм или сериал по названию.
* Рандомный фильм / сериал - выдаёт рандомный фильм или сериал. Так же можно ввести некоторые критерии.
* Малобюджетный фильм / сериал - выдаёт фильм или сериал с маленьким бюджетом. Так же можно ввести некоторые критерии.
* Высоко бюджетный фильм / сериал - выдаёт фильм или сериал с высоким бюджетом. Так же можно ввести некоторые критерии.
* Кастомный поиск - выдает фильм или сериал по большим настройкам поиска.
3. В боте присутствует история поиска фильмов или сериалов.

### Развитие бота (будущее)
1. Удаление фильма или сериала из истории поиска
2. Галочка в истории фильма или сериала о просмотре
3. Добавление более подробного описания характеристик фильма или сериала
4. Автоматическое удаление непонятных фильмов (к сожалению такие есть, может найтись фильм без названия, хотя все остальное у него присутствует)
5. Красивый вывод текста (возможно добавление цвета)
6. Мини викторина по знанию фильмов по постеру или описанию
7. Переделать все виды машин состояний и по возможности все reply клавиатуры на inline
8. Подключить web версию (для этого выучить надо frontend)
9. Создать приложение (в мечтах)
10. Продать проект
11. Добавить вкладку с будущими фильмами
12. Сделать рассылки с вышедшими фильмами