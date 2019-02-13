from state import state
import wpilib 
import ControlPico as robot_controller

def read_all_controller_inputs():

	#Chasis Inputs

	controller = wpilib.Joystick(0)


	x = controller.getX()
	state["mov_x"] = x

	y = controller.getY()
	state["mov_y"] = y

	z = controller.getZ()
	state["mov_z"] = z

	button_x = controller.getRawButton(3)
	state["button_x_active"] = button_x

	button_y = controller.getRawButton(2)
	state["button_y_active"] = button_y

	button_a = controller.getRawButton(1)
	state["button_a_active"] = button_a

	button_re = controller.getRawButton(4)
	state["button_re_active"] = button_re 


