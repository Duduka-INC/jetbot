from jetbot import Robot
import time

class jetbot_movement:
    def __init__(self):
        self.robot = Robot()
        
    def stop(self, change):
        robot.stop()

    def step_forward(self, change):
        robot.forward(0.4)
        time.sleep(0.5)
        robot.stop()

    def step_backward(self):
        robot.backward(0.4)
        time.sleep(0.5)
        robot.stop()

    def step_left(self):
        robot.left(0.3)
        time.sleep(0.5)
        robot.stop()

    def step_right(self):
        robot.right(0.3)
        time.sleep(0.5)
        robot.stop()
        
    def make_move(self, left_motor_torque, right_motor_torque):
        self.robot.set_motors(left_motor_torque, right_motor_torque)
        time.sleep(0.5)