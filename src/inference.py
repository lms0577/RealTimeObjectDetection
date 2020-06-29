#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tflite_runtime.interpreter as tflite
import numpy as np
import re
import cv2
import time

class TFLite:

    def __init__(self):

        # Load label map
        self.labelmap_dir = '/home/michael/TransferLearning/ssd_mobilnet_v2_quant_panda/model/tflite/labelmap.txt'
        self.labels = self.load_labels(self.labelmap_dir)

        # Load TFLite model and allocate tensors.
        self.ssd_v2_edgetpu_detect_tflite_dir = '/home/michael/TransferLearning/ssd_mobilnet_v2_quant_panda/model/tflite/detect_edgetpu.tflite'
        self.interpreter = tflite.Interpreter(model_path=self.ssd_v2_edgetpu_detect_tflite_dir, experimental_delegates=[tflite.load_delegate('libedgetpu.so.1')])
        self.interpreter.allocate_tensors()

    def load_labels(self, path):
        """Loads the labels file. Supports files with or without index numbers."""
        with open(path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            labels = {}
            for row_number, content in enumerate(lines):
                pair = re.split(r'[:\s]+', content.strip(), maxsplit=1)
                if len(pair) == 2 and pair[0].strip().isdigit():
                    labels[int(pair[0])] = pair[1].strip()
                else:
                    labels[row_number] = pair[0].strip()
        return labels

    def get_output_tensor(self, interpreter, index):
        """Returns the output tensor at the given index."""
        output_details = interpreter.get_output_details()[index]
        tensor = np.squeeze(interpreter.get_tensor(output_details['index']))
        return tensor

    def detect_objects(self, interpreter, image, threshold):
        """Returns a list of detection results, each a dictionary of object info."""
        input_details = interpreter.get_input_details()
        interpreter.set_tensor(input_details[0]['index'], image)
        interpreter.invoke()

        # Get all output details
        boxes = self.get_output_tensor(interpreter, 0)
        classes = self.get_output_tensor(interpreter, 1)
        scores = self.get_output_tensor(interpreter, 2)
        count = int(self.get_output_tensor(interpreter, 3))

        results = []
        for i in range(count):
            if scores[i] >= threshold:
                result = {
                    'bounding_box': boxes[i],
                    'class_id': classes[i],
                    'score': scores[i]
                }
                results.append(result)
        return results

    def show_inference_image(self, image, results, labels):
        result_size = len(results)
        for idx, obj in enumerate(results):
            # print(obj)
            # Prepare image width, height
            im_height, im_width, _ = image.shape

            # Prepare score, name
            score = obj['score']
            name = labels[obj['class_id']]
            # print('idx: {}, name: {}'.format(idx, name))
        
            # Prepare boundary box
            ymin, xmin, ymax, xmax = obj['bounding_box']
            xmin = int(xmin * im_width)
            xmax = int(xmax * im_width)
            ymin = int(ymin * im_height)
            ymax = int(ymax * im_height)

            # Draw rectangle to desired thickness
            cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)
        
            # Annotate image with label and confidence score
            cv2.putText(image, '{}: {:.2f}'.format(name, score), (xmin, ymin + 12), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)
    
        return image

    def inference(self, color_image):
        
        # Expand Dimensions for Inference and resize 300*300
        tflite_image = cv2.resize(color_image, dsize=(300, 300), interpolation=cv2.INTER_AREA)
        tflite_image = np.expand_dims(tflite_image, 0)

        # Detection
        threshold = 0.5
        results = self.detect_objects(self.interpreter, tflite_image, threshold)

        # Return result Color image
        result_color_image = self.show_inference_image(color_image, results, self.labels)

        return result_color_image

def main():

    try:
        tf = TFLite()

        cap = cv2.VideoCapture('/home/michael/Downloads/test_panda_video.mp4')

        frame_size = (640, 480)
        fourcc = cv2.VideoWriter_fourcc(*'MJPG')
        fps = 20
        color_filename = '/home/michael/Bit_Project/Video/color_video.avi'
        out_color = cv2.VideoWriter(color_filename, fourcc, fps, frame_size)

        while True:

            start_time = time.time()

            # Get Video Frames
            retval, frame = cap.read()
            if not retval:
                break

            # Inference Image 
            inference_color_image = tf.inference(color_image)

            # Show Inference Image
            cv2.imshow('Inference Color Image', inference_color_image)

            # Video Write
            out_color.write(inference_color_image)

            end_time = time.time()
            print('Total_FPS = {0:03d}'.format(int(1/(end_time - start_time))), end='\r')

            cv2.waitKey(1)

    finally:

        out_color.release()
        cap.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
        
