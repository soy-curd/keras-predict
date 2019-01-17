# kerasで画像認識

## download VGG16
```
from keras.applications.vgg16 import VGG16
model = VGG16(include_top=True, weights='imagenet', input_tensor=None, input_shape=None)
model.save()
```

## 起動
```
docker run --name imager -it -e PORT=80 -e ENV=development -p 8002:80 -v `pwd`/webapp:/opt/webapp soycurd/keras-predict sh ./start.sh
```

```
sh ./start.sh # modelのロードに90sほどかかる
```

## TODO
+ [x] デプロイ
+ [ ] テンプレート修正
+ [ ] モデル修正

## 参考
+ [Deploying your Keras model](https://medium.com/@burgalon/deploying-your-keras-model-35648f9dc5fb)

+ [VGG16 * keras](http://aidiary.hatenablog.com/entry/20170104/1483535144)

+ [Imagener日本語ラベル](http://pynote.hatenablog.com/entry/keras-vgg16-mode)


Kerasを使って画像分類するwebアプリを動かしてみた

Kerasを使って画像分類するwebアプリを動かしてみた。

http://soy-curd.com/image-predict/


哺乳類は結構判定できているかんじがする。

実装はほとんどこの記事(https://medium.com/@burgalon/deploying-your-keras-model-35648f9dc5fb)をそのまま参考にした。モデルはVGG16をそのまま使ったので、ImageNetにない画像は分類できない。
