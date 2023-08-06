# article i followed for creating a package
https://mathspp.com/blog/how-to-create-a-python-package-in-2022

# first, we need pipx in order to install poetry
python -m pip install --user pipx

# make sure the right python scripts folder is in the PATH env varaible on windows

pipx install poetry

#update the PATH env
pipx ensurepath

# reload the shell

# for a new project, run 'poetry new .' in the new empty directory
# for an existing project, type the below in the the directory and follow the prompts
poetry init

# now run install
poetry install

# do the git stuff if a new project that's not on git yet
git init
git add *
git commit -m "First commit"
git branch -M main
git remote add origin https://github.com/JamesRandell/ivypy.git
git push -u origin main

# more poetry stuff 
poetry add -D pre-commit

poetry config repositories.testpypi https://test.pypi.org/legacy/


#api token

# test account
poetry config http-basic.testpypi __token__ test-token-here

poetry build
poetry publish -r testpypi

# live account
poetry config pypi-token.pypi live-token-here


poetry publish --build
