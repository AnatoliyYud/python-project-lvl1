install: #установить poetry
	poetry install

brain-games: # запускаем brain-games
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl


