# 판다 실시간 객체 인식
<div>
<img src="https://user-images.githubusercontent.com/55565351/75853843-3b085900-5e32-11ea-95e4-accbb07d2f9a.jpg" width="300"/>
<img src="https://user-images.githubusercontent.com/55565351/83985445-4361ba00-a974-11ea-8c3b-3a6e2f565d9d.jpg" width="300"/>
</div>

## 프로젝트 내용식
* COCO dataset으로 사전 훈련된 SSD MobileNet v2 Quantized 모델을 Transfer Learning하여 ‘Panda’를 객체 인식한다. ‘Panda’ 이미지를 수집하고 ‘LabelImg’ 툴을 사용하여 Panda dataset을 준비한다. 
* TensorFlow Object Detection API로 준비한 Panda dataset을 Transfer Learning한다. 50000번 학습한 결과를 TensorFlow Lite로 변환한다. 그리고 Google Coral로 추론을 가속하기 위해 TensorFlow Lite 모델을 Edge TPU로 컴파일한다. 완성된 모델을 Jetson Nano에 올려 실시간으로 ‘Panda’를 객체 인식한다. 
## 개발 환경
제목 | 내용
--------- | --------
OS | Ubuntu 18.04
언어 | Python
하드웨어 | Jetson Nano, Google Coral USB Accerelator
라이브러리 | OpenCV
프레임워크 | TensorFlow, TensorFlow Lite
 
 ## 프로젝트 결과
 [![img](http://img.youtube.com/vi/wmvQsCfuFDU/0.jpg)](http://www.youtube.com/watch?v=wmvQsCfuFDU "img")
