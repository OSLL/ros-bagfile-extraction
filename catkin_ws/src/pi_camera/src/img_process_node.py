#!/usr/bin/env python3
import rospy
import cv2
import numpy as np
from sensor_msgs.msg import CompressedImage

class Storage:
    publisher = None

def cbCImg(msg):
    # cv_image = bridge.imgmsg_to_cv2(msg, desired_encoding="passthrough")
    # image = cv2.imdecode(data, 1)
    
    # Uncompress CompressedImage to cv image

    np_arr = np.fromstring(msg.data, np.uint8)
    _image_np = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    # Process image_np

    # Publish empty msg for easy hz testing
    Storage.publisher.publish(CompressedImage())

if __name__ == '__main__': 
    rospy.init_node('cv_test', anonymous=False)
    Storage.publisher = rospy.Publisher("~test", CompressedImage, queue_size=1)
    sub_img = rospy.Subscriber("camera/image/compressed", CompressedImage, cbCImg)
    rospy.spin()

