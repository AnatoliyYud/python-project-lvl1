install: # install the poetry
	poetry install

brain-games: # start brain-games script
	poetry run brain-games

brain-even: # start brain-even script
	poetry run brain-even

build: # building
	poetry build

publish: #publish
	poetry publish --dry-run

package-install: # install package
	python3 -m pip install --user dist/*.whl

package-uninstall: # uninstall package for next installation of updated package
	python3 -m pip uninstall dist/*.whl

lint: # flake8 linter checking
	poetry run flake8 brain_games
