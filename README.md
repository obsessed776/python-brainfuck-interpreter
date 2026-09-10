# Python Brainfuck Interpreter

Простий інтерпретатор мови програмування Brainfuck на Python.

# Можливості

- Підтримка основних команд Brainfuck.
- Робота з введенням та виведенням.
- Підтримка циклів.
- Підтримка виведення кириличних символів завдяки роботі з Unicode у Python.

# Запуск

Клонуйте репозиторій:
```shell
git clone https://github.com/obsessed776/python-brainfuck-interpreter.git
cd python-brainfuck-interpreter
```

Запустіть інтерпретатор:

Перед запуском укажіть .bf файл, який потрібно виконати, у функції read_file():

```python
raw_code = read_file("helloworld.bf")
```

Замініть helloworld.bf на назву потрібного Brainfuck-файлу:

```python
raw_code = read_file("my_program.bf")
```

Після цього запустіть інтерпретатор:

```shell
python interpreter.py
```

