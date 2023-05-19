import rospy
from naoqi_bridge_msgs.msg import JointAnglesWithSpeed
import math

# Define the joint names for the left and right arms
left_arm_joint_names = ['LShoulderPitch', 'LShoulderRoll', 'LElbowYaw', 'LElbowRoll', 'LWristYaw']
right_arm_joint_names = ['RShoulderPitch', 'RShoulderRoll', 'RElbowYaw', 'RElbowRoll', 'RWristYaw']

def handshake():
    # Initialize ROS node
    rospy.init_node('nao_handshake')

    # Set the joint angles for the left arm to simulate the hand shake motion
    left_arm_joint_angles = [math.radians(-20), math.radians(20), math.radians(-60), math.radians(-20), math.radians(-80)]
    
    # Set the joint angles for the right arm to simulate the hand shake motion
    right_arm_joint_angles = [math.radians(-20), math.radians(-20), math.radians(60), math.radians(20), math.radians(80)]
    
    # Set the speed for the joint angles
    speed = 0.5
    
    # Create a JointAnglesWithSpeed message for the left arm
    left_arm_msg = JointAnglesWithSpeed()
    left_arm_msg.joint_names = left_arm_joint_names
    left_arm_msg.joint_angles = left_arm_joint_angles
    left_arm_msg.speed = speed
    
    # Create a JointAnglesWithSpeed message for the right arm
    right_arm_msg = JointAnglesWithSpeed()
    right_arm_msg.joint_names = right_arm_joint_names
    right_arm_msg.joint_angles = right_arm_joint_angles
    right_arm_msg.speed = speed
    
    # Publish the JointAnglesWithSpeed messages
    left_arm_pub = rospy.Publisher('/joint_angles', JointAnglesWithSpeed, queue_size=1)
    right_arm_pub = rospy.Publisher('/joint_angles', JointAnglesWithSpeed, queue_size=1)
    
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        left_arm_pub.publish(left_arm_msg)
        right_arm_pub.publish(right_arm_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        handshake()
    except rospy.ROSInterruptException:
        pass





  # def control_Body_init(self):
    #     command = "rostopic pub /body_pose/goal naoqi_bridge_msgs/BodyPoseActionGoal \"{header: {stamp: now, frame_id: 'map'}, goal_id: {id: '1', stamp: now}, goal: {pose_name: 'Stand'}}\""
    #     os.system(command)
    # def control_LShoulder_Pitch(self, radian, speed=0.2):
    #     data = JointAnglesWithSpeed()
    #     # data.header = {'seq': 0,
    #     #                'stamp': {'secs': 0, 'nsecs': 0},
    #     #                'frame_id': ''}
    #     data.joint_names.append('LShoulderPitch')
    #     data.joint_angles.append(radian)
    #     data.speed = 0.2
    #     data.relative = 0
    #     rospy.loginfo('111')
    #     rate = rospy.Rate(0.7) # 10hz
    #     # while not rospy.is_shutdown():
    #     rate.sleep()
    #     self.pub.publish(data)
    #     rate.sleep()

    # def control_joints(self,joint_list, radian, speed=0.2):
    #     joint_names = joint_list
    #     joint_angles = radian # Move the head to the right and down

    #     # Construct the rostopic pub command
    #     cmd = "rostopic pub -1 /joint_angles naoqi_bridge_msgs/JointAnglesWithSpeed '{joint_names: [" + " ,".join(["'{}'".format(joint) for joint in joint_names]) + "], joint_angles: [" + " ,".join([str(angle) for angle in joint_angles]) + "], speed: " + str(speed) + "}'"
    #     # Use os.system to run the rostopic pub command
    #     os.system(cmd)

    # def control_LShoulder_Roll(self, radian, speed=0.2):
    #     joint_names = ["LShoulderRoll"]
    #     joint_angles = [radian] # Move the head to the right and down

    #     # Construct the rostopic pub command
    #     cmd = "rostopic pub -1 /joint_angles naoqi_bridge_msgs/JointAnglesWithSpeed '{joint_names: [" + " ,".join(["'{}'".format(joint) for joint in joint_names]) + "], joint_angles: [" + " ,".join([str(angle) for angle in joint_angles]) + "], speed: " + str(speed) + "}'"
    #     # Use os.system to run the rostopic pub command
    #     os.system(cmd)

    # def control_LElbow_Yaw(self, radian, speed=0.2):
    #     joint_names = ["LElbowYaw"]
    #     joint_angles = [radian] # Move the head to the right and down

    #     # Construct the rostopic pub command
    #     cmd = "rostopic pub -1 /joint_angles naoqi_bridge_msgs/JointAnglesWithSpeed '{joint_names: [" + " ,".join(["'{}'".format(joint) for joint in joint_names]) + "], joint_angles: [" + " ,".join([str(angle) for angle in joint_angles]) + "], speed: " + str(speed) + "}'"
    #     # Use os.system to run the rostopic pub command
    #     os.system(cmd)

    # def control_LElbow_Roll(self, radian, speed=0.2):
    #     joint_names = ["LElbowRoll"]
    #     joint_angles = [radian] # Move the head to the right and down

    #     # Construct the rostopic pub command
    #     cmd = "rostopic pub -1 /joint_angles naoqi_bridge_msgs/JointAnglesWithSpeed '{joint_names: [" + " ,".join(["'{}'".format(joint) for joint in joint_names]) + "], joint_angles: [" + " ,".join([str(angle) for angle in joint_angles]) + "], speed: " + str(speed) + "}'"
    #     # Use os.system to run the rostopic pub command
    #     os.system(cmd)

    # def control_LWrist_Yaw(self, radian, speed=0.2):

    #     joint_names = ["LWristYaw"]
    #     joint_angles = [radian] # Move the head to the right and down

    #     # Construct the rostopic pub command
    #     cmd = "rostopic pub -1 /joint_angles naoqi_bridge_msgs/JointAnglesWithSpeed '{joint_names: [" + " ,".join(["'{}'".format(joint) for joint in joint_names]) + "], joint_angles: [" + " ,".join([str(angle) for angle in joint_angles]) + "], speed: " + str(speed) + "}'"
    #     # Use os.system to run the rostopic pub command
    #     os.system(cmd)
