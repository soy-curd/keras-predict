echo start!!!! $ENV $1

if [ "$1" = "noop" ]; then
  tail -f /dev/null
elif [ "$ENV" = "development" ]; then
  echo "develop mode"
  gunicorn --bind 0.0.0.0:$PORT -t 3000 --reload --reload-extra-file templates/* wsgi
else
  echo "prod mode"
  gunicorn --bind 0.0.0.0:$PORT -t 60 wsgi
fi  