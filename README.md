# 1_caching_decorator

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)


Кэширующий декоратор в Python

## Task
Название проекта: **1_caching_decorator**

1. реализовать декоратор, который позволит кэшировать результаты выполнения произвольной функции
2. обращаю внимание, что сразу несколько функций в программе может быть одновременно задекорировано и при этом декоратор должен работать корректно
3. параметры - стратегия запоминания (как вариант минимум - глубина кэша)

## Installation

Создать виртуальное окружение

```bash
virtualenv venv
```

И активировать его
```powershell
# Для Windows
venv\Scripts\activate
```

```bash
# Для Linux
source venv/bin/activate
```

В корневой директории проекта выполнить

```bash
pip install .
```

## Usage

Пример использования

```python
from caching_decorator import cache

@cache(depth=5)
def compute(x, y, factor=1):
    return x * y * factor
```

```python
from caching_decorator import cache

@cache(depth=5, policy = "MRU")
def compute(x, y, factor=1):
    return x * y * factor
```

Ограничения:


Декоратор поддерживает только хэшируемые типы дынных.  
Глубина может быть бесконечной, если задать значение переменной depth = None:
```python
from caching_decorator import cache

@cache(depth=None, policy = "MRU")
def compute(x, y, factor=1):
    return x * y * factor
```


## Contributing

Предварительно нужно создать и активировать виртуальное окружение, а также установить в него зависимости проекта

```bash
pip install -r requirements.txt
```

В проекте используется автоматический форматировщик кода - [`Black`](https://github.com/psf/black), с настройками по умолчанию. В дополнение к нему используется [`isort`](https://github.com/PyCQA/isort) для сортировки импортов. Оба инструмента включёны в `requirements.txt`. 

Для того, чтобы отформатировать все файлы, достаточно в корне проекта выполнить:
```sh
black .
isort --profile black .
```

Однако **крайне желательно** перед работой над проектом настроить автоматическое форматирование с использованием Black и isort при сохранении файла в вашей IDE. Эти настройки можно включить только для этого проекта, чтобы случайно не повлиять на другие проекты. Для VS Code эти настройки уже активированы (см. `.vscode/settings.json`).

**Неотформатированный код ревью не пройдёт**.

Алгоритм внесения изменений выглядит следующим образом:

1. Создаём новую ветку от ветки `main`. Название состоит из английских букв в нижнем регистре, цифр и тире. Название должно отражать суть происходящего в ветке.
```bash
git checkout main
git pull
git checkout -b <branch-name>
```
2. Делаем коммиты с осмысленными названиями и делаем их часто. В рамках каждого коммита должны быть изменения только с одинаковой смысловой нагрузкой. Коммиты лучше называть на русском, если не уверены в своём английском, главное, чтобы другие участники процесса могли быстро разобраться в том, что вы делали.
3. Мерджим `main` в нашу ветку, чтобы захватить изменения, сделанные другими разработчиками, и разрешаем возможные конфликты.
```bash
# Эта команда спулит main и вмерджит в вашу ветку
git pull origin main
```
4. Тестируем работоспособность кода. Желательно, конечно, сразу покрывать новый код тестами.
```bash
pytest tests
```
5. Пушим изменения в своей ветке и создаём Pull Request. Задаём ему осмысленное название и описание, если это необходимо. Указываем как минимум одного разработчика в списке Reviewers.
```bash
# При первом пуше
git push -u origin <branch_name>
# При последующих
git push
```