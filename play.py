begin = """

George the Panda is trying to feed his needy family. He must be home before dark so his family will still love him. Help him get home before dark.
"""
finished = False
print(begin)
senario1 = """George sees his friend, Steve the monkey. To stay and chat, press 'a', or to avoid eye contact with Steve press 'b'"""
print(senario1)
decision1 = input("a_or_b")
if decision1 == "a":
    print('Oh no! Poor George. Steve was talking for hours, and it has gotten darker. Hurry, George is running out of time.')
    scenerio2 = """George comes upon a burning tree that is covering the pathway. To find another way around the tree it press 'a', or to jump over press 'b'"""
    print(scenerio2)
    decision2 = input("a_or_b")
    if decision2 == "a":
        finished = True
        print("George found another way, buuuuut its even darker outside. George eventually got home, but unfortunately his family is nowhere to be found.")
    elif decision2 == "b":
        finished = True
        print("Yay! George was able to get to his hungry family on time, and they still love him.")

elif decision1 == "b":
    print("Steve didn't see George. Its all good, keep moving.")




if not finished:
    scenerio3 = "Geeshhhhh clumsy George fell into a pit! What should he do?? Press 'a' to try to get out, or press 'b' to call for help"
    print(scenerio3)
    decision3 = input("a_or_b")
    if decision3 == "a":
        print("George got out safely and was able to return home without problems and disgrace.")
    elif decision3 == "b":
        print("AW mannnnnnnnnnn help came, but it took way too long. Poor George returned home only to find that his family hates him.")
