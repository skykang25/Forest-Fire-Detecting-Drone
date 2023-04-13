import keras
import numpy as np
from djitellopy import tello
import cv2
import keyboard
import threading

#드론 실행 drone operate
drone = tello.Tello()
drone.connect()
print(drone.get_battery())

drone.streamon()

# 모델 위치
TrainedParameter = 'C:\\Users\\user\\Desktop\\converted_keras\\keras_model.h5'

# 케라스 모델 가져오기
model = keras.models.load_model(TrainedParameter)

# 이미지 처리하기
def preprocessing(frame):
    #frame_fliped = cv2.flip(frame, 1)
    # 사이즈 조정 티쳐블 머신에서 사용한 이미지 사이즈로 변경해준다.
    size = (224, 224)
    frame_resized = cv2.resize(frame, size, interpolation=cv2.INTER_AREA)
    
    # 이미지 정규화
    # astype : 속성
    frame_normalized = (frame_resized.astype(np.float32) / 127.0) - 1

    # 이미지 차원 재조정 - 예측을 위해 reshape 해줍니다.
    # keras 모델에 공급할 올바른 모양의 배열 생성
    frame_reshaped = frame_normalized.reshape((1, 224, 224, 3))
    #print(frame_reshaped)
    return frame_reshaped

# 예측용 함수
def predict(frame):
    prediction = model.predict(frame)
    return prediction

'''
#순찰 함수
def patrol():
    drone.move_forward(10)
    drone.get_yaw(-90)
    drone.move_forward(10)
    drone.get_yaw(-90)
    drone.move_forward(10)
    drone.get_yaw(-90)
    drone.move_forward(10)
    drone.get_yaw(-90)

def patrol_thread():
    thread = threading.Thread(target=patrol)
    thread.daemon = True
    thread.start()

# 실행
drone.takeoff()
sleep(1)
patrol_thread()
'''

while True:
    frame = drone.get_frame_read().frame

    if cv2.waitKey(100) > 0: 
        break

    preprocessed = preprocessing(frame)
    prediction = predict(preprocessed)

    if (prediction[0,0] < prediction[0,1]):
        print('산불 아님')
        cv2.putText(frame, 'no fire', (0, 25), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0))

    else:
        cv2.putText(frame, 'fire', (0, 25), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0))
        print('산불')

    cv2.imshow("VideoFrame", frame)
    cv2.waitKey(10)
    
    if keyboard.is_pressed("1"):
        break
