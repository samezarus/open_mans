include ./.env

update:
	git pull origin main

push:
	git add *
	git commit -m "add changes"
	git push origin 'main'

update_env:
	git pull origin main

push_env:
	git add *
	git commit -m "add changes"
	git push origin 'main'
	git push https://${GIT_USER}:${GIT_PASSWORD}@github.com/${GIT_USER}/${GIT_REPO}