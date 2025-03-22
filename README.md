# Работа с API

## Как сделать запрос

1. Создайте виртуальную среду

```
python -m venv .venv
```

2. Активируйте её

```
source .venv/bin/activate
```

3. Установите пакет

```bash
pip install requests
```

4. Создайте переменную, где будет храниться адрес API `https://jsonplaceholder.typicode.com/users/1`

_Маршрут был взят из документации сервиса [jsonplaceholder](https://jsonplaceholder.typicode.com/)_

5. Сделайте запрос

```python
response = requests.get(название_переменной)
```

6. Проверьте, что ответ удовлетворяет нас (HTTP код 200)

```python
if response.status_code == 200:
    print("Запрос выполнен успешно!")
else:
    print("Ошибка запроса:", response.status_code)
```

7. Преобразуйте ответ в JSON

```python
data = response.json()

print(data)
```

8. Выведите поле имя

```python
print(f"Имя: {data['name']}")
```

## Самостоятельная работа

Используя данный [список](https://github.com/public-apis/public-apis?tab=readme-ov-file#anime), сделайте 3 запроса к сервисам, которые покажутся вам интересными и не требуют регистрации (`Auth`: `No`)
