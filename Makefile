# Makefile

install: # выполнить установку
	poetry install


brain-games: # запуск игры
	poetry run brain-games


build: # собрать пакет
	poetry build


publish: # отладка публикации пакета
	poetry publish --dry-run


package-install: # установка пакета из ОС (запускать из корня проекта)
	python3 -m pip install --user dist/*.whl