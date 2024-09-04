#!/usr/bin/python3
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class Converter:
    def __init__(self):
        rospy.init_node('msg_to_mp4', anonymous=True)
        rospy.Subscriber("/zedm/zed_node/rgb/image_rect_color", Image, self.callback)

        self.out = cv2.VideoWriter("output2.mp4", cv2.VideoWriter_fourcc(*'mp4v'), 15, (1104, 621))
        # self.out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'), 1.0, (640, 360))
        
    def callback(self, data: Image):
        bridge = CvBridge()
        cv_image = bridge.imgmsg_to_cv2(data, desired_encoding='bgr8')
        print(cv_image.shape)
        self.out.write(cv_image)
    
    def save(self):
        self.out.release()  
         
def main():
    converter = Converter()
    try: 
        rospy.spin() 
    except rospy.ROSInterruptException:
        converter.save()

if __name__ == '__main__':
    main()