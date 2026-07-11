import pyttsx3
engine = pyttsx3.init()
current_rate = engine.getProperty('rate')
# print(f"Current rate: {current_rate}")
                                                                                                                    
engine.setProperty('rate', 240)
engine.say('''"Uhhh,summa-lumma,dooma-lumma,you assumin'I'm a human What I gotta do to get it through to you I'm superhuman,innovativeand I'm made of rubberSo that anything you say is ricochetin' off of me,and it'll glue to youAnd I'm devastating,more than ever demonstrating How to give a motherfuckin'audience a feeling like it's levitatingNever fading,and I know the haters are forever waiting For the day that they can say I fell off,they'll be celebrating''')
engine.runAndWait()
