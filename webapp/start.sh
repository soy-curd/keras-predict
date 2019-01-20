echo start!!!! $ENV $1

if [ "$1" = "noop" ]; then
  tail -f /dev/null
elif [ "$ENV" = "development" ]; then
  echo "develop mode"
  python app.py
else
  echo "prod mode"
  gunicorn --bind 0.0.0.0:$PORT -t 600 wsgi
fi  