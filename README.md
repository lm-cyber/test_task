# Тестовое задание Python разработчика
Выполнил все кроме docker <br/>


запуск

```bash
sudo docker run --name test_for_dev -p 5432:5432 -e POSTGRES_USER=yt -e POSTGRES_PASSWORD=yt -e POSTGRES_DB=test -d postgres%
python migration.py
python main.py
```
миграции
```bash
python migration.py
```
тесты
```bash
pytest tests.py
```
