Инструкции по запуску
===================

Необходимые компоненты
-------------
[Задание](https://park.mail.ru/blog/topic/view/10294/) </br>
[Чек-лист](https://docs.google.com/spreadsheets/d/1E2wA4Ew0h8apS7aZ_IDom6-4onpZ2EQ-c95Syl3ULh0/edit#gid=638182835)
```sh
pip install -U selenium

```

Чтобы запустить один браузер (чисто для проверки)
-------------
Выполняем команды
```sh
make set-os-<имя операционой системы (linux | macos | win)>
make set-env
python test_area.py

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