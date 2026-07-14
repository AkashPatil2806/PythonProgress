import pyttsx3
engine = pyttsx3.init()
current_rate = engine.getProperty('rate')
# print(f"Current rate: {current_rate}")
engine.setProperty('rate', 200)

engine.say('''"I am just leaving this comment to remind everyone that you are gonna be the good programmer, just be consistent and practice every day You're welcome''')
engine.runAndWait()