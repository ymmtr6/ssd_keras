[![license](https://img.shields.io/github/license/mashape/apistatus.svg)](LICENSE)
# A port of [SSD: Single Shot MultiBox Detector](https://github.com/weiliu89/caffe/tree/ssd) to [Keras](https://keras.io) framework.
For more details, please refer to [arXiv paper](http://arxiv.org/abs/1512.02325).
For forward pass for 300x300 model, please, follow `SSD.ipynb` for examples. For training procedure for 300x300 model, please, follow `SSD_training.ipynb` for examples. Moreover, in `testing_utils` folder there is a useful script to test `SSD` on video or on camera input.

Weights are ported from the original models and are available [here](https://mega.nz/#F!7RowVLCL!q3cEVRK9jyOSB9el3SssIA). You need `weights_SSD300.hdf5`, `weights_300x300_old.hdf5` is for the old version of architecture with 3x3 convolution for `pool6`.

This code was tested with `Keras` v1.2.2, `Tensorflow` v1.0.0, `OpenCV` v3.1.0-dev

# ssd_keras

keras2で動作する様にカスタマイズしたSingleShotMultiboxDetector。
[rykkov8/ssd_keras](https://github.com/rykov8/ssd_keras)のコードを流用している。


## environment

動作確認ライブラリは[requirements.txt](requirements.txt)を参照。
* Tensorflow 1.13
* Keras 2.2.4
* opencv-python 4.1.0
* scikit
* imageio
* Python3.7.4

動作環境はDockerイメージを用意。

## 学習について

* https://arkouji.cocolog-nifty.com/blog/2018/01/tensorflowkeras.html
* https://qiita.com/ttskng/items/4f67f4bbda2568229956
* 

##　変更履歴

* scipy 1.3.0　では、scipy.misc.imreadがdeprecatedなので、同じ処理を行うimageioに変更
* Keras2.0に伴い、merge関数がdeprecated, Concatレイヤーに変更
* Keras2.0に伴い、カスタムレイヤーの実装する関数compute_output_shapeを変更
