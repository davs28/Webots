from controller import Robot, Keyboard, Camera
import modern_robotics as mr
import numpy as np

TIME_STEP = 64

robot = Robot()
keyboard = Keyboard()

keyboard.enable(TIME_STEP)

InitRotation = 0

motors = []
motorNames = ['motor1', 'motor2', 'motor3', 'motor4', 'motor5', 'motor6']
for i in range(6):
    motors.append(robot.getDevice(motorNames[i]))
    motors[i].setPosition(InitRotation)
    
gripper1 = robot.getDevice('gripper1')
gripper2 = robot.getDevice('gripper2')

ps = []
sensorNames = ['ps1', 'ps2', 'ps3', 'ps4', 'ps5', 'ps6', 'ps7', 'ps8']
for i in range(8):
    ps.append(robot.getDevice(sensorNames[i]))
    ps[i].enable(TIME_STEP)
    
camera = robot.getDevice('camera')
camera.enable(TIME_STEP)

camera_width = 360
camera_height = 360

motor1rotation = 0
motor2rotation = 0
motor3rotation = 0
motor4rotation = 0
motor5rotation = 0
motor6rotation = 0

minRotation = -0.78
maxRotation = 0.78

gripper1value = 0
gripper2value = 0

q = 81
w = 87
a = 65
s = 83
z = 90
x = 88
e = 69
r = 82
d = 68
f = 70
c = 67
v = 86
j = 74
k = 75
p = 80

# Testing Modern Robotics Functions

M = np.array([[ 0, -1,  0,     0],
              [ 1,  0,  0, 0.165],
              [ 0,  0,  1,   0.2],
              [ 0,  0,  0,    1]])
Blist = np.array([[0, 0,  1,    0,   0,   0],
                  [1, 0,  0,    0,   0,   0],
                  [1, 0,  0,    0, 0.2,   0],
                  [0, 1,  0, -0.2,   0,   0],
                  [1, 0,  0,    0,   1,   0],
                  [0, 1,  0,    0,   0, 0.1]]).T
thetalist = np.array([np.pi / 2.0, 3, np.pi])

forwardKinematics = mr.FKinBody(M, Blist, thetalist)
print("FK =",forwardKinematics)


while robot.step(TIME_STEP) != -1:
    currentKey = keyboard.getKey()
    print(currentKey)
    
    if currentKey == p:
        image = camera.getImage()
        for x in range(0, camera_width):
            for y in range(0, camera_width):
                r = camera.imageGetRed(image, camera_width, x, y)
                g = camera.imageGetGreen(image, camera_width, x, y)
                b = camera.imageGetBlue(image, camera_width, x, y)
                print("red:", r, "green:", g, "blue:", b)       
       
    # These lines of code control robot movement
    if currentKey == q:
        motor1rotation -= 0.03       
    elif currentKey == w :
        motor1rotation += 0.03      
    motors[0].setPosition(motor1rotation)
    
    if currentKey == a and motor2rotation > minRotation:
        motor2rotation -= 0.01
    if currentKey == s and motor2rotation < maxRotation:
        motor2rotation += 0.01
    motors[1].setPosition(motor2rotation)
        
    if currentKey == z and motor3rotation > minRotation:
        motor3rotation -= 0.01
        sensorValue3 = ps[2].getValue()
        print("Sensor 3 value: " , sensorValue3)       
    if currentKey == x and motor3rotation < maxRotation:
        sensorValue3 = ps[2].getValue()
        print("Sensor 3 value: " , sensorValue3)
        motor3rotation += 0.01
    motors[2].setPosition(motor3rotation)  
    
    if currentKey == e:
        motor4rotation -= 0.03       
    if currentKey == r:
        motor4rotation += 0.03       
    motors[3].setPosition(motor4rotation)  
    
    if currentKey == d and motor5rotation > minRotation:
        motor5rotation -= 0.01       
    if currentKey == f and motor5rotation < maxRotation:
        motor5rotation += 0.01 
    motors[4].setPosition(motor5rotation)
    
    if currentKey == c:
        motor6rotation -= 0.03       
    if currentKey == v:
        motor6rotation += 0.03
    motors[5].setPosition(motor6rotation)
    
    if currentKey == j:
        sensorValue7 = ps[6].getValue()
        sensorValue8 = ps[7].getValue()
        print("Sensor 7 value: " , sensorValue7)
        print("Sensor 8 value: " , sensorValue8)
        
        gripper1value += 0.001
        gripper2value += 0.001
        gripper1.setPosition(gripper1value)
        gripper2.setPosition(gripper2value)
        
    if currentKey == k:
        gripper1value -= 0.001 
        gripper2value -= 0.001
        gripper1.setPosition(gripper1value)
        gripper2.setPosition(gripper2value)
               