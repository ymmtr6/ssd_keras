[![license](https://img.shields.io/github/license/mashape/apistatus.svg)](LICENSE)
# A port of [SSD: Single Shot MultiBox Detector](https://github.com/weiliu89/caffe/tree/ssd) to [Keras](https://keras.io) framework.
For more details, please refer to [arXiv paper](http://arxiv.org/abs/1512.02325).
For forward pass for 300x300 model, please, follow `SSD.ipynb` for examples. For training procedure for 300x300 model, please, follow `SSD_training.ipynb` for examples. Moreover, in `testing_utils` folder there is a useful script to test `SSD` on video or on camera input.

Weights are ported from the original models and are available [here](https://mega.nz/#F!7RowVLCL!q3cEVRK9jyOSB9el3SssIA). You need `weights_SSD300.hdf5`, `weights_300x300_old.hdf5` is for the old version of architecture with 3x3 convolution for `pool6`.

This code was tested with `Keras` v1.2.2, `Tensorflow` v1.0.0, `OpenCV` v3.1.0-dev

# ssd_keras

keras2で動作する様にカスタマイズしたSingleShotMultiboxDetector。
[rykkov8/ssd_keras](https://github.com/rykov8/ssd_keras)のコードを流用している。
わからないことが合ったら、本家GithubのIssueを見れば大体書いてる。


## Environment

動作確認ライブラリは[requirements.txt](requirements.txt)を参照。
* Tensorflow 1.13
* Keras 2.2.4
* opencv-python 4.1.0
* scikit
* imageio
* Python3.7.4

動作環境はDockerイメージを用意。
```
$ docker pull ymmtr6/ssd_keras
```


GPU版はこちら
```
$ docker pull ymmtr6/ssd_keras:gpu
```

学習済モデル[pre-trained model](https://github.com/ymmtr6/ssd_keras/releases/download/1.0/weights_SSD300.hdf5)

論文ではVGG16のpretrainを行っているため、モデルの流用を行う場合は精度が出ない可能性がある。**VGG16のpretrainはそのうち実装予定**。

## RUN

デフォルトでは、picsディレクトリの中から1枚指定してdetectionを行う。
```
$ cd ssd_keras
$ docker run -it --rm -v `pwd`:/workspace --name ssd_keras ymmtr6/ssd_keras bash
$ python3 run.py
```

GPU版はこちら
```
$ cd ssd_keras
$ docker run -it --rm --runtime nvidia -v `pwd`:/workspace --name ssd_keras ymmtr6/ssd_keras:gpu bash
$ python3 run.py
```

## Train

未検証。多分これでうごくと思います（適当）

1. データセットをディレクトリ配下に生やす
1. PASCAL_VOC/get_data_from_XML.pyでpklファイルを作成
1. config.pyのDATA_PKLのパスを変更
1. train.py

### (参考)PASCALVOCの学習を行う場合

1. VOC2007データセットのダウンロード
```
$ wget http://host.robots.ox.ac.uk/pascal/VOC/voc2007/VOCtrainval_06-Nov-2007.tar
$ wget http://host.robots.ox.ac.uk/pascal/VOC/voc2007/VOCtest_06-Nov-2007.tar

$ tar -xvf VOCtarinval_06-Nov-2007.tar
$ tar -xvf VOCtest_06-Nov-2007.tar
```
すると、以下の様に展開される
```
├── VOCdevkit
│   └── VOC2007
│       ├── Annotations
│       ├── ImageSets
│       │   ├── Layout
│       │   ├── Main
│       │   └── Segmentation
│       ├── JPEGImages
│       ├── SegmentationClass
│       └── SegmentationObject
```

1. 教師データをpklにまとめる。

ROOTからAnnotationsまでのパスをPASCAL_VOC/get_data_from_XML.pyの下部に記載する。また、吐き出すファイル名を指定する。
```
# example on how to use it
data = XML_preprocessor('VOCdevkit/VOC2007/Annotations/').data
pickle.dump(data, open('VOC2007.pkl', 'wb'))
```

そのあと実行。

```
$ cd ssd_keras
$ python3 PASCAL_VOC/get_data_from_XML.py
```

1. 学習を行う。

config.pyを環境に合わせたあと、
```
$ python3 train.py
```
を実行するれば稼働する。実行途中の重みはcheckpoints/に保存されていく。

## 参考資料

* https://arkouji.cocolog-nifty.com/blog/2018/01/tensorflowkeras.html
* https://qiita.com/ttskng/items/4f67f4bbda2568229956
* https://qiita.com/slowsingle/items/64cc927bb29a49a7af14


## 変更履歴

* Dockerfileの配置に伴い、requirements.txtを移動。gpu対応。
* scipy 1.3.0　では、scipy.misc.imreadがdeprecatedなので、同じ処理を行うimageioに変更
* Keras2.0に伴い、merge関数がdeprecated, Concatレイヤーに変更
* Keras2.0に伴い、カスタムレイヤーの実装する関数compute_output_shapeを変更
