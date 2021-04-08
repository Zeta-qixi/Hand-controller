import cv2
import mediapipe as mp
import os
import time
import random
from PIL import Image
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
'''
results: json格式的21个节点
'''

cfile = '/Users/mac/vscode/python/ML/data/pic'
# For static images:
hands = mp_hands.Hands(
    static_image_mode=True,
    max_num_hands=2,
    min_detection_confidence=0.7)
file_list = random.sample(os.listdir(cfile),1)
sum = 0
t = []
for idx, file in enumerate(file_list):
  time1 = time.time()
  # Read an image, flip it around y-axis for correct handedness output (see
  # above).
  file = cfile + '/'+ file
  image = cv2.flip(cv2.imread(file), 1)
  # Convert the BGR image to RGB before processing.
  results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

  #---- Print handedness and draw hand landmarks on the image. ---#
  #print('handedness:', results.multi_handedness)
  if not results.multi_hand_landmarks:
    continue
  annotated_image = image.copy()
  for hand_landmarks in results.multi_hand_landmarks:
    #print('hand_landmarks:', hand_landmarks)
    mp_drawing.draw_landmarks(
        annotated_image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
  t.append(time.time()-time1)
  im = Image.fromarray(cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB))
  im.show()
  cv2.imwrite('/Users/mac/vscode/python/ML/data/annotated_image/_' + str(idx) + '.png', cv2.flip(annotated_image, 1))
hands.close()

