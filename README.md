# Markdown to HTML Converter

Цей застосунок конвертує файли з розміткою Markdown у HTML.

## Інструкція, як зібрати та запустити проект

### Вимоги
- Python 3.6 або вище

### Кроки

1. Клонувати репозиторій або скопіювати вихідні файли проекту у ваш локальний каталог.
2. Перейти до каталогу проекту у вашому терміналі.
3. Створити віртуальне середовище:
    ```sh
    python -m venv .venv
    ```
4. Активувати віртуальне середовище:
    - Windows:
      ```sh
      .venv\Scripts\activate
      ```
    - macOS/Linux:
      ```sh
      source .venv/bin/activate
      ```
      
## Інструкція до використання проекту

1. Переконайтесь, що ваше віртуальне середовище активоване (див. крок 4 у секції "Кроки").
2. Запустіть скрипт для конвертації Markdown у HTML:
    ```sh
    python main.py example.md --out output.html
    ```
   Це команда конвертує файл `example.md` у HTML і зберігає результат у `output.html`.

3. Якщо ви хочете побачити HTML в стандартному виводі (stdout), запустіть скрипт без параметра `--out`:
    ```sh
    python main.py example.md
    ```
4. Переконайтесь, що у вас є файл `example.md`, який ви хочете конвертувати. Ви можете використовувати будь-який інший файл з розширенням `.md`, який ви бажаєте конвертувати.

## Приклад використання

### Markdown файл (example.md)

```
**bold text**
_italic fragment_
`monospaced`

Paragraph1. Lorem Ipsum Dolor Sit Amet.
This is still paragraph 1.

And after a blank line this is paragraph 2.
```
### Команда для запуску

   ```sh
   python main.py example.md --out output.html
   ```
### Результат (output.html)

**bold text**
_italic fragment_
`monospaced`

Paragraph1. Lorem Ipsum Dolor Sit Amet.
This is still paragraph 1.

And after a blank line this is paragraph 2.

## Revert commit

[Посилання на Revert commit](https://github.com/chErnykovaDD/lab1_sdmt/commit/2051241a480d1b8a9a3d3d37add0a51e56141ea2)