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

## RUN

デフォルトでは、picsディレクトリの中から1枚指定してdetectionを行う。
```
$ python3 run.py
```

## Train

未検証。多分これでうごくと思います（適当）

1. データセットをディレクトリ配下に生やす
1. PASCAL_VOC/get_data_from_XML.pyでpklファイルを作成
1. config.pyのDATA_PKLのパスを変更
1. train.py

## 参考資料

* https://arkouji.cocolog-nifty.com/blog/2018/01/tensorflowkeras.html
* https://qiita.com/ttskng/items/4f67f4bbda2568229956
* https://qiita.com/slowsingle/items/64cc927bb29a49a7af14


##　変更履歴

* Dockerfileの配置に伴い、requirements.txtを移動。gpu対応。
* scipy 1.3.0　では、scipy.misc.imreadがdeprecatedなので、同じ処理を行うimageioに変更
* Keras2.0に伴い、merge関数がdeprecated, Concatレイヤーに変更
* Keras2.0に伴い、カスタムレイヤーの実装する関数compute_output_shapeを変更
