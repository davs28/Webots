from controller import Robot, Keyboard

TIME_STEP = 64

robot = Robot()
keyboard = Keyboard()

keyboard.enable(TIME_STEP)

ds = []
dsNames = ['ds_right', 'ds_left']
for i in range(2):
    ds.append(robot.getDevice(dsNames[i]))
    ds[i].enable(TIME_STEP)
    
wheels = []
wheelsNames = ['wheel1', 'wheel2', 'wheel3', 'wheel4']
for i in range(4):
    wheels.append(robot.getDevice(wheelsNames[i]))
    wheels[i].setPosition(float('inf'))
    wheels[i].setVelocity(0.0)
    
linearMotor = robot.getDevice("LinearMotor")
linearPos = 0
linearMotor.setPosition(linearPos) 

rotationalMotor = robot.getDevice("RotationalMotor")
rotatePos = 0
rotationalMotor.setPosition(rotatePos)

avoidObstacleCounter = 0
while robot.step(TIME_STEP) != -1:
    leftSpeed = 1.0
    rightSpeed = 1.0
    if avoidObstacleCounter > 0:
        avoidObstacleCounter -= 1
        leftSpeed = 1.0
        rightSpeed = -1.0
    else:     
        for i in range(2):
            if ds[i].getValue() < 950.0:
                avoidObstacleCounter = 100
               
    wheels[0].setVelocity(leftSpeed)
    wheels[1].setVelocity(rightSpeed)
    wheels[2].setVelocity(leftSpeed)
    wheels[3].setVelocity(rightSpeed)
    
    currentKey = keyboard.getKey()
    print(currentKey)
    if currentKey == 87 and linearPos < 0.14:
        linearPos += 0.005

    if currentKey == 83 and linearPos > 0:
        linearPos -= 0.005
      
    
    if currentKey == 88:
        rotatePos += 0.01
        
    if currentKey == 90:
        rotatePos -= 0.01
        
        
    linearMotor.setPosition(linearPos)  
    rotationalMotor.setPosition(rotatePos)   
        
        
    
    

    