# 판다 실시간 객체 인식
<div>
<img src="https://user-images.githubusercontent.com/55565351/75853843-3b085900-5e32-11ea-95e4-accbb07d2f9a.jpg" width="300"/>
<img src="https://user-images.githubusercontent.com/55565351/75853974-760a8c80-5e32-11ea-851b-f66996bf8569.jpg" width="300"/>
</div>

## 프로젝트 내용식
* 왼쪽, 오른쪽의 초음파 센서로부터 거리를 측정한다. 왼쪽의 거리가 10cm 이하가 되면 로봇이 멈추고 버저가 울리면서 오른쪽으로 회전하여 회피한다. 
* 버튼 센서 2개를 사용하여 각각 전원, 속도 조절용으로 사용한다. 전원 버튼은 한 번 누르면 로봇이 움직이고 한 번 더 누르면 멈춘다. 속도 조절 버튼은 누를 때마다 속도가 올라간다. 
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
