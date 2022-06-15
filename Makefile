install: #установить poetry
	poetry install

brain-games: # запускаем brain-games
	poetry run brain-games

build: # building
	poetry build

publish: #publish
	poetry publish --dry-run

package-install: # install package
	python3 -m pip install --user dist/*.whl

lint: # flake8 linter checking
	poetry run flake8 brain_games
