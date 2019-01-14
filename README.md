# Miniconda on Heroku Example App

This repository contains two things:

- A `Dockerfile`, which installs [scikit-learn](http://scikit-learn.org/stable/) with [miniconda](http://conda.pydata.org/miniconda.html), and a few [pip](https://pip.pypa.io/en/stable/) dependencies.
- A [Flask](http://flask.pocoo.org) `webapp`, which utilizes basic functionality of `scikit-learn`.

All [Anaconda packages](https://docs.continuum.io/anaconda/pkg-docs) are supported—`scikit-learn` is just being used here as an example. 

## ☤ Advantages over [Conda Buildpack](https://github.com/kennethreitz/conda-buildpack):

- No slug size limit (Anaconda packages can be very large). 
- Exact Miniconda environment, from Continuum Analytics.

## ☤ Deploy this Application:

Deploy with the [Container Registry and Runtime](https://devcenter.heroku.com/articles/container-registry-and-runtime):

     $ heroku plugins:install heroku-container-registry
     $ heroku container:login
     
     $ git clone https://github.com/heroku-examples/python-miniconda
     $ cd python-miniconda
     
     $ heroku create
     $ heroku container:push web

✨🍰✨

## 起動

## download VGG16
```
from keras.applications.vgg16 import VGG16
model = VGG16(include_top=True, weights='imagenet', input_tensor=None, input_shape=None)
```

## 起動
```
docker run --name imager -it -e PORT=80 -e ENV=development -p 8002:80 -v `pwd`/webapp:/opt/webapp soycurd/keras-predict sh ./start.sh
```

```
sh ./start.sh # modelのロードに90sほどかかる
```

## TODO
+ [ ] テンプレート修正
+ [ ] デプロイ
+ [ ] 翻訳
+ [ ] モデル修正

## 参考
+ [VGG16 * keras]http://aidiary.hatenablog.com/entry/20170104/1483535144

+ [Imagener日本語ラベル](http://pynote.hatenablog.com/entry/keras-vgg16-mode)