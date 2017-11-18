Инструкции по запуску
===================

Необходимые компоненты
-------------
![Задание](https://park.mail.ru/blog/view/4/)
```sh
pip install -U selenium

```

Чтобы запустить один браузер (чисто для проверки)
-------------
Выполняем команды
```sh
make set-env
python test-area.py

```

Чтобы запустить grid
-------------
Выбрать браузер:
CHROME:
```sh
make set-chrome

```
или FIREFOX:
```sh
make set-firefox

```
Запустить грид:
```sh
make grid

```
Запустить браузеры:
```sh
make node

```
Запустить тесты:
```sh
make run-tests

```