#!/usr/bin/env python3
"""
	This is a good foundation to build your robot code on
"""

import wpilib
import wpilib.drive


class MyRobot(wpilib.TimedRobot):

	def robotInit(self):
		self.Encoder = wpilib.Encoder(0, 1)
		self.setpoint = 1337
		self.lift = wpilib.Talon(0)

		self.P = 1
		self.I = 1
		self.D = 1

		self.integral = 0
		self.previous_error = 0

	def teleopPeriodic(self):
		self.PID()

	def setSetpoint(self, setpoint):
		self.setpoint = setpoint

	def PID (self):
		"""PID for angle control"""
		error = self.setpoint - 1900 #self.Encoder.get()
		self.integral = self.integral + (error*.02)
		derivative = (error - self.previous_error) / .02
		self.rcw = self.P*error + self.I*self.integral + self.D*derivative
		print(self.rcw)

	def execute (self):
		"""Called every iteration of teleopPeriodic"""
		self.PID()
		self.lift.set(self.rcw)

if __name__ == "__main__":
	wpilib.run(MyRobot)