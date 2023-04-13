# Forest-Fire-Detecting-Drone

It is AI-aplied Drone program.<br>
First, I made Forest-Fire-Detector AI by Teachable Machine that is useful trasfer learning tool.<br>
This model classifies two classes(fire vs nonfire). I trained this model with about 14,000 photos. The photos consist of fire class(forest-fire, smoke),and nonfire class(dusty, foggy landscape, huge clouds over mountain, reddish sunset, nonfire photos). Database where I collected the images is Kaggle

<br>
<br>
Tello drone의 카메라를 통해 image를 받아와서 AI model에 입력하고 분류시킴. tello drone은 일정한 구역 반복적으로 움직이면서 이미지를 받아오는 매개체 역할임. 분류 시에 산불이 감지되면, drone을 실행시킨 컴퓨터에 경고음이 울림.  
<br>
<br>
<br>

converted_keras is trained model parameter file. main.py refers this keras parameter.
