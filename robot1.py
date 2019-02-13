#!/usr/bin/env python3
"""
	This is a good foundation to build your robot code on
"""

import wpilib
import wpilib.drive
from state import state

class MyRobot(wpilib.TimedRobot):

	def robotInit(self):
		self.Encoder = wpilib.Encoder(0, 1)
		self.setpoint = 7000 #1337,2674,4011 prueba // 3700, 5800, 7000
		self.lift = wpilib.Talon(0)
		self.P = 1
		self.I = 1
		self.D = 1

		self.integral = 0
		self.previous_error = 0

	def teleopPeriodic(self):
		self.PID()
		"""if state["button_x_active"]:
			if self.rcw >= 68213.74 and self.rcw >= 58009.74:
				self.lift_motor.set(0.7)
			elif self.rcw >= 58009.74 and self.rcw >= 37601.74:
				self.lift_motor.set(0.5)
			elif self.rcw >= 37601.74 and self.rcw >= 12091.74:
				self.lift_motor.set(0.3)
			elif self.rcw >= 12091.74 and self.rcw >= 102.04:
				self.lift_motor.set(0.2)
			elif self.rcw >= 102.04:
				self.lift_motor.set(0)

		elif state["button_y_active"]:
			if self.rcw >= 136427.48 and self.rcw >= 116019.48:
				self.lift_motor.set(0.7)
			elif self.rcw >= 116019.48 and self.rcw >= 68213.74:
				self.lift_motor.set(0.5)
			elif self.rcw >= 68213.74 and self.rcw >= 34387.48:
				self.lift_motor.set(0.3)
			elif self.rcw >= 34387.48 and self.rcw >= 102.08:
				self.lift_motor.set(0.2)
			elif self.rcw >= 102.08:
				self.lift_motor.set(0)

		elif state["button_a_active"]:
			if self.rcw >= 204641.22  and self.rcw >= 128111.22:
				self.lift_motor.set(0.7)
			elif self.rcw >= 128111.22  and self.rcw >= 51581.22:
				self.lift_motor.set(0.5)
			elif self.rcw >= 51581.22 and self.rcw >= 15867.22:
				self.lift_motor.set(0.3)
			elif self.rcw >= 15867.22 and self.rcw >= 561.22:
				self.lift_motor.set(0.2)
			elif self.rcw >= 561.22:
				self.lift_motor.set(0)""
	
				"""
		if state["button_re_active"]:
			if self.rcw >= 151019.2 and self.rcw >= 113264.4:
				self.lift_motor.set(0.7)
			elif self.rcw >= 113264.4 and self.rcw >= 75509.6:
				self.lift_motor.set(0.5)
			elif self.rcw >= 75509.6 and self.rcw >= 37754.8:
				self.lift_motor.set(0.3)
			elif self.rcw >= 37754.8 and self.rcw >= 102.04:
				self.lift_motor.set(0.2)
			elif self.rcw >=102.04:
				self.lift_motor.set(0)

		elif state["button_re_active"]:
			if self.rcw >= 236732.8 and self.rcw >= 177549.6:
				self.lift_motor.set(0.7)
			elif self.rcw >= 177549.6 and self.rcw >= 118366.4:
				self.lift_motor.set(0.5)
			elif self.rcw >= 118366.4 and self.rcw >= 59183.2:
				self.lift_motor.set(0.3)
			elif self.rcw >= 59183.2 and self.rcw >= 102.04:
				self.lift_motor.set(0.2)
			elif self.rcw >= 102.04:
				self.lift_motor.set(0)

		elif state["button_re_active"]:
			if self.rcw >= 285712.0 and self.rcw >= 214284.0:
				self.lift_motor.set(0.7)
			elif self.rcw >= 214284.0 and self.rcw >= 142856.0:
				self.lift_motor.set(0.5)
			elif self.rcw >= 142856.0 and self.rcw >= 71428.0:
				self.lift_motor.set(0.3)
			elif self.rcw >= 71428.0 and self.rcw >= 102.04:
				self.lift_motor.set(0.2)
			elif self.rcw >= 102.04:
				self.lift_motor.set(0)
	


			
	def setSetpoint(self, setpoint):
		self.setpoint = setpoint

	def PID (self):
		error = self.setpoint - 6000 #self.Encoder.get()
		self.integral = self.integral + (error*.02)
		derivative = (error - self.previous_error) / .02
		self.rcw = self.P*error + self.I*self.integral + self.D*derivative
		print(self.rcw)

	def execute (self):

		self.PID()
		self.lift.set(self.rcw)

if __name__ == "__main__":
	wpilib.run(MyRobot)