import speech_recognition
import pyttsx3
from datetime import date, datetime

#nghe.py

robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""

while True:

	with speech_recognition.Microphone() as mic:
		print("Robot: I'm Listening")
		audio = robot_ear.listen(mic)
	print("Robot:...")
	try:
		you = robot_ear.recognize_google(audio)
	except:
		you = ""
	print("You: " + you)

	#hieu.py (Natural Language Processing)

	if you == "":
		robot_brain = "I can't hear you, please try again"
	elif "hi" in you:
		robot_brain = "Hello Minh Hoang"
	elif "today" in you:
		current_date = date.today()
		robot_brain = current_date.strftime("It's %B %d, %Y")
	elif "girlfriend's" in you:
		robot_brain = "Bao Nguyen"
	elif "time" in you:
		current_time = datetime.now()
		robot_brain = current_time.strftime("It's %H hours %M minutes %S seconds")
	elif"father's" in you:
		robot_brain = "Van Duc"
	elif "mother's" in you:
		robot_brain = "Lan Mai"
	elif "brother's" in you:
		robot_brain = "Gia Huy"
	elif "friend's" in you:
		robot_brain = "Is that Duc Dau Buoi ?"
	elif "yes" in you:
		robot_brain = "Alright ! I got it"
	elif "bye" in you:
		robot_brain = "Bye Minh Hoang. Hope to see you again"
		print("Robot:" + robot_brain)
		robot_mouth.say(robot_brain)
		robot_mouth.runAndWait()
		break
	else:
		robot_brain = "I dont understand"
	print("Robot:" + robot_brain)

	#noi.py

	robot_mouth.say(robot_brain)
	robot_mouth.runAndWait()
