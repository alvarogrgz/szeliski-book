import math
from statistics import variance
from turtle import back
from typing import Tuple
import numpy as np
import cv2
from PIL import Image
import scipy.stats as st

def get_statistics(video_name: str) -> Tuple[np.array, np.array]:
    # calculate mean
    cap = cv2.VideoCapture(video_name)
    if not cap.isOpened():
        print("Cannot open video")
        exit()

    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    mean = np.copy(frame)
    mean = mean.astype(np.int64)
    count = 1

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        mean += frame
        count+=1

    mean = mean/count

    # calculate variance
    cap = cv2.VideoCapture(video_name)
    	
    if not cap.isOpened():
        print("Cannot open video")
        exit()

    variance = np.zeros(mean.shape)

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        variance += np.power(frame-mean, 2) 

    variance = variance / count
    std_deviation = np.sqrt(variance)
    sem = std_deviation/math.sqrt(count)
    return mean, variance

def get_foreground(video_name, background, mean, variance):
    cap = cv2.VideoCapture(video_name)
    if not cap.isOpened():
        print("Cannot open video")
        exit()

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame_grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        foreground = np.bitwise_or(frame_grey > mean + variance, frame_grey < mean - variance)
        alpha = np.where(foreground, 1.0, 0.0).astype(np.float32)
        alpha = cv2.cvtColor(alpha, cv2.COLOR_GRAY2BGR).astype(np.uint8)
        
        composited = cv2.add(cv2.multiply(frame, alpha), cv2.multiply(background, 1 - alpha))
        cv2.imshow('Composited image', composited)
        cv2.waitKey(1)

def main():
    mean, variance = get_statistics('../images/exercise-3.5/background.mp4')

    background = cv2.imread('../images/exercise-3.5/beach.jpg')
    background = cv2.resize(background, (mean.shape[1], mean.shape[0]))
    get_foreground('../images/exercise-3.5/foreground.mp4', background, mean, variance)

if __name__ == "__main__":
	main()