from state import state
import wpilib 

def read_all_controller_inputs():

	#Chasis Inputs

	joystick = wpilib.Joystick(0)


	button_x = joystick.getRawButton(3)
	state["button_x_active"] = button_x

	button_y = joystick.getRawButton(2)
	state["button_y_active"] = button_y

	button_a = joystick.getRawButton(1)
	state["button_a_active"] = button_a

	button_y = joystick.getRawButton(4)
	state["button_y_active"] = button_y


