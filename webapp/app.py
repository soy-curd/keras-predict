# coding: UTF-8
import os
import json

from flask import Flask, request, g, render_template
from flask import jsonify
from flask import send_file

# from PIL import Image, ExifTags
# from scipy.misc import imresize
import numpy as np
from keras.models import load_model
from keras.applications.vgg16 import preprocess_input, decode_predictions
from keras.preprocessing import image

app = Flask(__name__
  , instance_relative_config=True
  , static_url_path='/image-predict/static'
  )

app.config.from_object('config.ProductionConfig')


f = open("model/imagenet_class_index.json")
json_data = json.load(f)
imagenet_class = {}
for data in json_data:
    imagenet_class[data["en"]] = data

# Preload our model
print("Loading model")
# model = load_model('./model/model.h5', compile=False)
print("Loading is finihsed")


def vgg16_predict(x):
    preds = model.predict(preprocess_input(x))
    results = decode_predictions(preds, top=5)[0]
    for result in results:
        print(result)
    result = results[0]
    return {"class": result[1],
      "value": float(result[2]),
      "name": translate2jp(result[1])}

def translate2jp(en):
  return imagenet_class[en]["ja"]

@app.route('/image-predict/predict', methods=['POST'])
def predict():
    print("predict")
    img = image.load_img(request.files['file'], target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    # result = vgg16_predict(x)
    result = {"class": "hgoe", "name": "fuga"}
    return jsonify(ResultSet=result)

@app.route('/image-predict/')
def homepage():
  
    print("hoge")
    return render_template('index.html')

@app.route('/<path:path>')
def catch_all(path):
    print(path)
    return 'You want path: %s' % path

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=os.environ["PORT"])
