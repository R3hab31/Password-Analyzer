import re

def analyze(pwd):
    score=0
    sugg=[]

    if len(pwd)>7:
        score+=1
    else:
        sugg.append("Your password should have atleast 8 characters")

    if re.search(r"[A-Z]",pwd):
        score+=1
    else:
        sugg.append("Your password should have atleast one Uppercase Letter")

    if re.search(r"[a-z]",pwd):
        score+=1
    else:
        sugg.append("Your password should have at least one Lowercase Letter ")

    if re.search(r"\d",pwd):
        score+=1
    else:
        sugg.append("Your password should have atleast one Number")

    if re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>/?]", pwd):
        score+=1
    else:
        sugg.append("Your password should have atleast one Symbol")
    

    if score>0 and score<=2:
        strength="Weak"
    elif score>3 and score<=4:
        strength="Medium"
    else:
        strength="Strong"

    return strength,sugg

