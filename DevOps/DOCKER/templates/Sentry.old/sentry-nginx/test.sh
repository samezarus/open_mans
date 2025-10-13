#!/bin/bash

# chmod +x test.sh


clear


SENTRY_HOST=<урл сентри сервера с портом>
SENTRY_KEY=<ключ проекта>
PROJECT_ID=<id проекта>


curl \
--data '{"test": "test done"}' \
-H 'Content-Type: application/json' \
-H "X-Sentry-Auth: Sentry sentry_version=7, sentry_key=$SENTRY_KEY, sentry_client=raven-bash/0.1" \
https://$SENTRY_HOST/api/$PROJECT_ID/store/
