from controller import Robot

def run_robot(robot):

    time_step = 32
    max_speed = 6.28

    left_motor = robot.getDevice('left wheel motor')
    right_motor = robot.getDevice('right wheel motor')

    left_motor.setPosition(float('inf'))
    right_motor.setPosition(float('inf'))

    left_motor.setVelocity(0.0)
    right_motor.setVelocity(0.0)

    left_ir = robot.getDevice('ir1')
    left_ir.enable(time_step)

    right_ir = robot.getDevice('ir0')
    right_ir.enable(time_step)

    while robot.step(time_step) != -1:
        left_ir_value = left_ir.getValue()
        right_ir_value = right_ir.getValue()

        print(f"LEFT = {left_ir_value} RIGHT {right_ir_value}")

        left_speed = max_speed * 0.25
        right_speed = max_speed * 0.25

        if left_ir_value > right_ir_value and (6 < left_ir_value < 15):
            print("vá para a esquerda")
            left_speed = -max_speed * 0.25
        elif right_ir_value > left_ir_value and (6 < right_ir_value < 15):
            print("vá para a direita")
            right_speed = -max_speed * 0.25

        left_motor.setVelocity(left_speed)
        right_motor.setVelocity(right_speed)

if __name__ == "__main__":
    robot = Robot()
    run_robot(robot)
