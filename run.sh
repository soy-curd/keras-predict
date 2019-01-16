echo $1

docker run --name imager -it -e PORT=80 -e ENV=development -p 8002:80 -v `pwd`/webapp:/opt/webapp -d soycurd/keras-predict sh ./start.sh $1