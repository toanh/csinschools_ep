from csinsc import *
from random import *

# speeds things up a bit
import time
def sleep(n):
    time.sleep(n/3)
    
toptwofivegame = False
timegame = True
print(Colour.blue + "opening software...")
sleep(1)
print("booting up menu...")
sleep(1)
print("23%")
sleep(1)
print("44%")
sleep(1)
print("67%")
sleep(1)
print("99%")
sleep(5)
print("100%")
sleep(1)
print("Done loading up menu now..." + Colour.reset)

label .menu

sleep(2)
print(Colour.cyan + " ------------------------------")
print("{        The Menu              }")
print("|Enter [A] for Chat Bot        |")
print("|Enter [B] for Combat Simulator|")
print(" ------------------------------" + Colour.reset)
game_choice = input("Choose your game: ")

if game_choice == 'A':
  print("                     ")
  print(Colour.blue + "loading up Chat Bot")
  sleep(1)
  print("booting up game")
  sleep(1)
  print("24%")
  sleep(1)
  print("45%")
  sleep(1)
  print("68%")
  sleep(1)
  print("99%")
  sleep(5)
  print("100%")
  sleep(1)
  print("Done loading up Chat Bot now..." + Colour.reset)
  sleep(1)
  print("                    ")
  print("Hello my name is Chatter Bot")
  sleep(1)
  name = input(Colour.yellow + "Whats your name: " + Colour.reset)
  sleep(1)
  name_response = randint(1,3)
  if name_response == 1:    
    print("Thats such a cool name " + str(name))
    sleep(1)
  elif name_response == 2:
    print("I love your name, " + str(name))
    sleep(1)
  elif name_response == 3:
    print("Your name is awesome! "+ str(name))
    sleep(1)

  age_game = input(Colour.green + "Do you want to play a game " + str(name) + " ? :" + Colour.reset)
  sleep(1)
  cb_age = randint(1,100)
  if age_game == "yes":
    print("Okay, try and guess my age...")
    sleep(1)
    print("You have 5 guesses!")
    sleep(1)
    age_guessing = 5
    age_text = 1
    while age_guessing > 0:
      age_guess = input(Colour.red + "Guess " + str(age_text) + " :" + Colour.reset)
      age_guess = int(age_guess)
      age_guessing = age_guessing - 1
      age_text = age_text + 1
      if age_guess < cb_age:
        print("Thats too young!")
      elif age_guess > cb_age:
        print("I'm not that old!!")
      elif age_guess == cb_age:
        print("You got it!")
        age_guessing = 0
      else:
        print("Thats not a number try again!")
  elif age_game == "no":
    print("Aww okay...")
  else:
    print("Thats not an answer try again (all lowercase answer)")
    goto .agegamequestion
  print("I'm " + str(cb_age) + (" years old!"))
  print("                          ")
  age = input("How old are you, " + str(name) + "?")
  age = int(age)
  if age > cb_age:
    print("Wow your older than me, " + str(name))
  elif age < cb_age:
    print("Oh your younger than me, " + str(name))
  else:
    print("Wowww we are the same age, " + str(name))
  cb_bm = randint(1,12)
  print("                          ")
  birth_month = input(Colour.yellow + "What is your birth month, " + str(name) + " ? (all lowercase)" + Colour.reset)

  if birth_month == "january":
    if cb_bm == 1:
      print("Oh same " + str(name))
    else:
      print("Oh, so you were born near valentimes day, " + str(name))
  elif birth_month == "febuary":
    if cb_bm == 2:
      print("Oh same " + str(name))
    else:
      print("Oh, thats cool, " + str(name))
  elif birth_month == "march":
    if cb_bm == 3:
      print("Oh same " + str(name))
    else:
      print("Oh, thats cool, " + str(name))
  elif birth_month == "april":
    if cb_bm == 4:
      print("Oh same " + str(name))
    else:
      print("Oh, thats cool, " + str(name))
  elif birth_month == "may":
    if cb_bm == 5:
      print("Oh same " + str(name))
    else:
      print("Oh, thats cool, " + str(name))
  elif birth_month == "june":
    if cb_bm == 6:
      print("Oh same " + str(name))
    else:
      print("Oh, thats cool, " + str(name))
  elif birth_month == "july":
    if cb_bm == 7:
      print("Oh same " + str(name))
    else:
      print("Oh, thats cool, " + str(name))
  elif birth_month == "august":
    if cb_bm == 8:
      print("Oh same " + str(name))
    else:
      print("Oh, so you were born near fathers day, " + str(name))
  elif birth_month == "september":
    if cb_bm == 9:
      print("Oh same " + str(name))
    else:
      print("Oh, so you were born near halloween, " + str(name))
  elif birth_month == "october":
    if cb_bm == 10:
      print("Oh same " + str(name))
    else:
      print("Oh, thats cool, " + str(name))
  elif birth_month == "november":
    if cb_bm == 11:
      print("Oh same " + str(name))
    else:
      print("Oh, so you were born near thanks giving, " + str(name))
  elif birth_month == "december":
    if cb_bm == 12:
      print("Oh same " + str(name))
    else:
      print("Oh, so you were born at the end of the year, " + str(name))
  else:
    print("Thats not a month?")

  print("                          ")
  hundreadgamequestion = input(Colour.green + "Do you want to know when you will reach 100, " + str(name) + " ? (all lowercase) : " + Colour.reset)
  hundreadyear = 100 - age + 2021
  hundreadyearleft = 100 - age
  cbyearleft = 100 - cb_age
  if hundreadgamequestion == "yes":
    print("You will reach 100 in " + str(hundreadyear) + (" and you have ") + str(hundreadyearleft) + (" years left till you reach 100"))
    if hundreadyearleft < cb_age:
      print("I'm going to reach 100 before you!")
    elif hundreadyearleft > cb_age:
      print("Your going to reach 100 before me!")
    else:
      print("Wow we are going to reach 100 together!")
  elif hundreadgamequestion == "no":
    print("Awww okay")
  else:
    print("Thats not an answer try again!")
    goto .hundreadgamestart
  label .heightgamequestion
  heightgamequestion = input(Colour.yellow + "Do you want to guess my height " + str(name) + " ? :" + Colour.reset)
  cb_height = randint(1,200)
  if heightgamequestion == "yes":
    print("Okay, try and guess my height in centimetres...")
    print("You have 10 guesses!")
    height_guessing = 10
    height_text = 1
    while height_guessing > 0:
      height_guess = input(Colour.red + "Guess " + str(height_text) + " :" + Colour.reset)
      height_guess = int(height_guess)
      height_guessing = height_guessing - 1
      height_text = height_text + 1
      if height_guess < cb_height:
        print("Thats too short!")
      elif height_guess > cb_height:
        print("I'm not that tall!!")
      elif height_guess == cb_height:
        print("You got it!")
        height_guessing = 0
      else:
        print("Thats not a number try again!")
  elif age_game == "no":
    print("Aww okay...")
  else:
    print("Thats not an answer")
  print("I'm " + str(cb_height) + ("cm tall!"))
  print("                          ")
  age = input(Colour.green + "How tall are you in cms, " + str(name) + "?" + Colour.reset)
  age = int(age)
  if age > cb_age:
    print("Wow your taller than me, " + str(name))
  elif age < cb_age:
    print("Oh your shorter than me, " + str(name))
  else:
    print("Wowww we are the same height, " + str(name))
  colour = input(Colour.yellow + "Whats your favourite colour (lowercase), " + str(name) + " : " + Colour.reset)
  if colour == "red":
    print(Colour.red + "Wow I love red too, " + str(name) + " !" + Colour.reset)
  elif colour == "yellow":
    print(Colour.yellow + "I really like yellow too, " + str(name) + " !" + Colour.reset)
  elif colour == "blue":
    print(Colour.blue + "I love blue so much, " + str(name) + " !!!" + Colour.reset)
  elif colour == "green":
    print(Colour.green + "I love green so much, " + str(name) + " !!!" + Colour.reset)
  elif colour == "cyan":
    print(Colour.cyan + "Cyan is the best, " + str(name) + " !" + Colour.reset)
  elif colour == "aqua":
    print(Colour.cyan + "Aqua is the best, " + str(name) + " !" + Colour.reset)
  elif colour == "purple":
    print(Colour.magenta + "Wow i love purple, " + str(name) + " !!" + Colour.reset)
  elif colour == "pink":
    print(Colour.magenta + "I really like pink too, " + str(name) + " !" + Colour.reset)
  elif colour == "white":
    print("I like white its the colour of most of my text!")
  else:
    print("I love that colour!")
  animal = input(Colour.green + "Whats your favourite animal (lowercase)? : " + Colour.reset)
  if animal == "dog":
    print("Woof, Woof")
    toptwofivegamequestion = input("Your animals in the top 25 most searched, would you like to guess its place, " + str(name) + " ? : ")
    if toptwofivegamequestion == "yes":
      secretnum = 1
      toptwofivegame = True
    elif toptwofivegamequestion == "no":
      print("Awww okay... maybe next time...")
    else:
      print("Thats not an answer!")
  elif animal == "cat":
    print("Meow, Meow")
    toptwofivegamequestion = input("Your animals in the top 25 most searched, would you like to guess its place, " + str(name) + " ? : ")
    if toptwofivegamequestion == "yes":
      secretnum = 2
      toptwofivegame = True
    elif toptwofivegamequestion == "no":
      print("Awww okay... maybe next time...")
    else:
      print("Thats not an answer!")
  elif animal == "horse":
    print("Neigh, Neigh")
    toptwofivegamequestion = input("Your animals in the top 25 most searched, would you like to guess its place, " + str(name) + " ? : ")
    if toptwofivegamequestion == "yes":
      secretnum = 3
      toptwofivegame = True
    elif toptwofivegamequestion == "no":
      print("Awww okay... maybe next time...")
    else:
      print("Thats not an answer!")
  elif animal == "chicken":
    print("Bock, Bock")
    toptwofivegamequestion = input("Your animals in the top 25 most searched, would you like to guess its place, " + str(name) + " ? : ")
    if toptwofivegamequestion == "yes":
      secretnum = 4
      toptwofivegame = True
    elif toptwofivegamequestion == "no":
      print("Awww okay... maybe next time...")
    else:
      print("Thats not an answer!")
  elif animal == "fish":
    print("Blub, Blob")
    toptwofivegamequestion = input("Your animals in the top 25 most searched, would you like to guess its place, " + str(name) + " ? : ")
    if toptwofivegamequestion == "yes":
      secretnum = 5
      toptwofivegame = True
    elif toptwofivegamequestion == "no":
      print("Awww okay... maybe next time...")
    else:
      print("Thats not an answer!")
  elif animal == "bear":
    print("Grr, Grrr")
    toptwofivegamequestion = input("Your animals in the top 25 most searched, would you like to guess its place, " + str(name) + " ? : ")
    if toptwofivegamequestion == "yes":
      secretnum = 6
      toptwofivegame = True
    elif toptwofivegamequestion == "no":
      print("Awww okay... maybe next time...")
    else:
      print("Thats not an answer!")
  elif animal == "bird":
    print("Tweet, Tweet")
    toptwofivegamequestion = input("Your animals in the top 25 most searched, would you like to guess its place, " + str(name) + " ? : ")
    if toptwofivegamequestion == "yes":
      secretnum = 7
      toptwofivegame = True
    elif toptwofivegamequestion == "no":
      print("Awww okay... maybe next time...")
    else:
      print("Thats not an answer!")
  elif animal == "shark":
    print("Chomp, Chomp")
    toptwofivegamequestion = input("Your animals in the top 25 most searched, would you like to guess its place, " + str(name) + " ? : ")
    if toptwofivegamequestion == "yes":
      secretnum = 8
      toptwofivegame = True
    elif toptwofivegamequestion == "no":
      print("Awww okay... maybe next time...")
    else:
      print("Thats not an answer!")
  elif animal == "snake":
    print("Hisss, Hisss")
    toptwofivegamequestion = input("Your animals in the top 25 most searched, would you like to guess its place, " + str(name) + " ? : ")
    if toptwofivegamequestion == "yes":
      secretnum = 9
      toptwofivegame = True
    elif toptwofivegamequestion == "no":
      print("Awww okay... maybe next time...")
    else:
      print("Thats not an answer!")
  elif animal == "pig":
    print("Oink, Onik")
    toptwofivegamequestion = input("Your animals in the top 25 most searched, would you like to guess its place, " + str(name) + " ? : ")
    if toptwofivegamequestion == "yes":
      secretnum = 10
      toptwofivegame = True
    elif toptwofivegamequestion == "no":
      print("Awww okay... maybe next time...")
    else:
      print("Thats not an answer!")
  elif animal == "lion":
    print("Roarr, Roarr")
    toptwofivegamequestion = input("Your animals in the top 25 most searched, would you like to guess its place, " + str(name) + " ? : ")
    if toptwofivegamequestion == "yes":
      secretnum = 11
      toptwofivegame = True
    elif toptwofivegamequestion == "no":
      print("Awww okay... maybe next time...")
    else:
      print("Thats not an answer!")
  elif animal == "turkey":
    print("Gobble, Gobble")
    toptwofivegamequestion = input("Your animals in the top 25 most searched, would you like to guess its place, " + str(name) + " ? : ")
    if toptwofivegamequestion == "yes":
      secretnum = 12
      toptwofivegame = True
    elif toptwofivegamequestion == "no":
      print("Awww okay... maybe next time...")
    else:
      print("Thats not an answer!")
  elif animal == "wolf":
    print("Awooo, Awoooo")
    toptwofivegamequestion = input("Your animals in the top 25 most searched, would you like to guess its place, " + str(name) + " ? : ")
    if toptwofivegamequestion == "yes":
      secretnum = 13
      toptwofivegame = True
    elif toptwofivegamequestion == "no":
      print("Awww okay... maybe next time...")
    else:
      print("Thats not an answer!")
  elif animal == "spider":
    print("Hisss, Hisss")
    toptwofivegamequestion = input("Your animals in the top 25 most searched, would you like to guess its place, " + str(name) + " ? : ")
    if toptwofivegamequestion == "yes":
      secretnum = 14
      toptwofivegame = True
    elif toptwofivegamequestion == "no":
      print("Awww okay... maybe next time...")
    else:
      print("Thats not an answer!")
  elif animal == "rabbit":
    print("Hop, Hop")
    toptwofivegamequestion = input("Your animals in the top 25 most searched, would you like to guess its place, " + str(name) + " ? : ")
    if toptwofivegamequestion == "yes":
      secretnum = 15
      toptwofivegame = True
    elif toptwofivegamequestion == "no":
      print("Awww okay... maybe next time...")
    else:
      print("Thats not an answer!")
  elif animal == "duck":
    print("Quack, Quack")
    toptwofivegamequestion = input("Your animals in the top 25 most searched, would you like to guess its place, " + str(name) + " ? : ")
    if toptwofivegamequestion == "yes":
      secretnum = 16
      toptwofivegame = True
    elif toptwofivegamequestion == "no":
      print("Awww okay... maybe next time...")
    else:
      print("Thats not an answer!")
  elif animal == "deer":
    print("Meow,")
    toptwofivegamequestion = input("Your animals in the top 25 most searched, would you like to guess its place, " + str(name) + " ? : ")
    if toptwofivegamequestion == "yes":
      secretnum = 17
      toptwofivegame = True
    elif toptwofivegamequestion == "no":
      print("Awww okay... maybe next time...")
    else:
      print("Thats not an answer!")
  elif animal == "cow":
    print("Mooo, Mooo")
    toptwofivegamequestion = input("Your animals in the top 25 most searched, would you like to guess its place, " + str(name) + " ? : ")
    if toptwofivegamequestion == "yes":
      secretnum = 18
      toptwofivegame = True
    elif toptwofivegamequestion == "no":
      print("Awww okay... maybe next time...")
    else:
      print("Thats not an answer!")
  elif animal == "monkey":
    print("Oooo, Oooo")
    toptwofivegamequestion = input("Your animals in the top 25 most searched, would you like to guess its place, " + str(name) + " ? : ")
    if toptwofivegamequestion == "yes":
      secretnum = 19
      toptwofivegame = True
    elif toptwofivegamequestion == "no":
      print("Awww okay... maybe next time...")
    else:
      print("Thats not an answer!")
  elif animal == "lobster":
    print("Blub, Blob")
    toptwofivegamequestion = input("Your animals in the top 25 most searched, would you like to guess its place, " + str(name) + " ? : ")
    if toptwofivegamequestion == "yes":
      secretnum = 20
      toptwofivegame = True
    elif toptwofivegamequestion == "no":
      print("Awww okay... maybe next time...")
    else:
      print("Thats not an answer!")
  elif animal == "ape":
      print("Oooo, Oooo")
      toptwofivegamequestion = input("Your animals in the top 25 most searched, would you like to guess its place, " + str(name) + " ? : ")
      if toptwofivegamequestion == "yes":
        secretnum = 21
        toptwofivegame = True
      elif toptwofivegamequestion == "no":
        print("Awww okay... maybe next time...")
      else:
        print("Thats not an answer!")
  elif animal == "pony":
    print("Neigh, Neigh")
    toptwofivegamequestion = input("Your animals in the top 25 most searched, would you like to guess its place, " + str(name) + " ? : ")
    if toptwofivegamequestion == "yes":
      secretnum = 22
      toptwofivegame = True
    elif toptwofivegamequestion == "no":
      print("Awww okay... maybe next time...")
    else:
      print("Thats not an answer!")
  elif animal == "eagle":
    print("Caaa, Cawww")
    toptwofivegamequestion = input("Your animals in the top 25 most searched, would you like to guess its place, " + str(name) + " ? : ")
    if toptwofivegamequestion == "yes":
      secretnum = 23
      toptwofivegame = True
    elif toptwofivegamequestion == "no":
      print("Awww okay... maybe next time...")
    else:
      print("Thats not an answer!")
  elif animal == "dolphin":
    print("Eeeee, Eeeee")
    toptwofivegamequestion = input("Your animals in the top 25 most searched, would you like to guess its place, " + str(name) + " ? : ")
    if toptwofivegamequestion == "yes":
      secretnum = 24
      toptwofivegame = True
    elif toptwofivegamequestion == "no":
      print("Awww okay... maybe next time...")
    else:
      print("Thats not an answer!")
  elif animal == "bison":
    print("Grunt, Grunt")
    toptwofivegamequestion = input("Your animals in the top 25 most searched, would you like to guess its place, " + str(name) + " ? : ")
    if toptwofivegamequestion == "yes":
      secretnum = 25
      toptwofivegame = True
    elif toptwofivegamequestion == "no":
      print("Awww okay... maybe next time...")
    else:
      print("Thats not an answer!")
  else:
    print("That animals so cool!!")
  while toptwofivegame == True:
    print("You have 5 guesses to guess what number your animal is ranked in the top 25 most searched!")
    animal_guessing = 5
    animal_text = 1
    while animal_guessing > 0:
      animal_guess = input(Colour.red + "Guess " + str(animal_text) + " :" + Colour.red)
      animal_guessing = animal_guessing - 1
      animal_text = animal_text + 1
      animal_guess = int(animal_guess)
      if animal_guess < secretnum:
        print("Your animals not thattt popluar!!")     
      elif animal_guess > secretnum:
        print("Your animals wayy more popular!")
      elif animal_guess == secretnum:
        print("You got it!")
        animal_guessing = 0
        toptwofivegame = False
      else:
        print("Thats not a number try again!")
    print("Your animal is ranked at " + str(secretnum) + (" out of the top 25 most searched animals!"))
  print("                          ")
  mood = input(Colour.yellow + "How are you feeling today, " + str(name) + " ? : " + Colour.reset)
  if "good" in mood or "great" in mood or "fantastic" in mood or "amazing"in mood or "awesome" in mood:
    print("I'm so happy for you!!!")
  elif "okay" in mood or "meh" in mood or "alright" in mood or "eh" in mood or "bored" in mood:
    print("Oh, its a boring day isnt it, " + str(name + " ."))
  elif "bad" in mood or "terrible" in mood or "sad" in mood or "depressed" in mood or "angry" in mood:
    print("Oh, well I hope you feel better, " + str(name) + " !")
    sadmoodreason = input("Why is that?")
    print("Sorry to hear that, I hope that " + str(sadmoodreason) + " stops bothering you!")
  else:
    print("Okay i haope you enjoy the rest of the day " + str(name) + " !")
  cb_mood = randint(1,15)
  if cb_mood == 1:
    print("I'm feeling good because i'm talking to you, " + str(name) + " !!")
  elif cb_mood == 2:
    print("I'm feeling great because i'm talking to you, " + str(name) + " !!")
  elif cb_mood == 3:
    print("I'm feeling fantasic because i'm talking to you, " + str(name) + " !!")
  elif cb_mood == 4:
    print("I'm feeling amazing because i'm talking to you, " + str(name) + " !!")
  elif cb_mood == 5:
    print("I'm feeling awesome because i'm talking to you, " + str(name) + " !!")
  elif cb_mood == 6:
    print("I'm feeling meh because I met someone who put the milk before the cereal, " + str(name) + " !!")
  elif cb_mood == 7:
    print("I'm feeling okay because todays been boring, " + str(name) + " !!")
  elif cb_mood == 8:
    print("I'm feeling alright because i'm talking to you, " + str(name) + " !!")
  elif cb_mood == 9:
    print("I'm feeling eh because I spilt my milk, " + str(name) + " !!")
  elif cb_mood == 10:
    print("I'm feeling bored because I have to right an essay today, " + str(name) + " !!")
  elif cb_mood == 11:
    print("I'm feeling bad because i, " + str(name) + " !!")
  elif cb_mood == 12:
    print("I'm feeling terrible because my Mum made me eat my veggies, " + str(name) + " !!")
  elif cb_mood == 13:
    print("I'm feeling sad because I got ejected from the spaceship, " + str(name) + " !!")
  elif cb_mood == 14:
    print("I'm feeling angry because I raged at a videogame, " + str(name) + " !!")
  elif cb_mood == 15:
    print("I'm feeling depressed because my program corrupted yesterday, " + str(name) + " !!")
  print("    ")
  timegamequestion = input("Do you want to play a guessing game, " + str(name) + " ? : ")
  if timegamequestion == "yes":
    while timegame == True:    
      print("Okay I am going to try to guess your time")
      amPMGuess = randint(1, 2)
      if amPMGuess == 1:
        amPMGuess = "AM"
      else:
        amPMGuess = "PM"      
      guessCorrect = input("Is it currently " + amPMGuess + " right now? (Y/N)")
      if guessCorrect.islower() == True:
        guessCorrect = guessCorrect.upper()
      if guessCorrect == "N":
        if (amPMGuess == 'AM'):
          amPMGuess = "PM"
        else:
          amPMGuess = "AM"
      lowerHour = 1
      upperHour = 12
      guessCorrect = 'N'
      while guessCorrect != 'Y':
        hourGuess = randint(lowerHour, upperHour)
        guessCorrect = input("Is the current hour " + str(hourGuess) + " o'clock? (Y/N)")
        if guessCorrect.islower() == True:
          guessCorrect = guessCorrect.upper()
        if guessCorrect == 'N':
          earlierOrLater = input("Is the current hour earlier or later than " + str(hourGuess) + " o'clock? (E/L)")
          if earlierOrLater == 'E' or earlierOrLater == 'e':
            upperHour = hourGuess - 1
          elif earlierOrLater == 'L' or earlierOrLater == 'l':
           lowerHour = hourGuess + 1
      lowerMinute = 0
      upperMinute = 59
      guessCorrect = 'N'
      while guessCorrect != 'Y':
        minuteGuess = randint(lowerMinute, upperMinute)
        if minuteGuess >= 10:
          minuteGuessStr = str(minuteGuess)
        else:
          minuteGuessStr = "0" + str(minuteGuess)

        guessCorrect = input("Is the time " + str(hourGuess) + ":" + minuteGuessStr + " " + amPMGuess + "? (Y/N)")
        if guessCorrect.islower() == True:
          guessCorrect = guessCorrect.upper()
        if guessCorrect == 'N':
          earlierOrLater = input("Is the current time earlier or later than " + str(hourGuess) + ":" + minuteGuessStr + "? (E/L)")
          if earlierOrLater == 'E' or earlierOrLater == 'e':
            upperMinute = minuteGuess - 1
          elif earlierOrLater == 'L' or earlierOrLater == 'l':
            lowerMinute = minuteGuess + 1
      print("    ")
      print("=============================================")
      print("Ha! I guess it. The current time is: " + str(hourGuess) + ":" + str(minuteGuess) + " " + amPMGuess)
      print("=============================================")
      print("    ")
  print("     ")
  echat = input("Did you enjoy talking with me??")
  if echat == "yes":
    print("I did tooo, " + str(name) + " !!!")
  elif echat == "no":
    print("Aww okay :(")
  else:
    print("Oh okayyy")
  bye = input("Good bye!!!!")
  goto .menu

if game_choice == 'B':
  print("                     ")
  print("loading up Combat Simulator")
  sleep(1)
  print("booting up game")
  sleep(1)
  print("24%")
  sleep(1)
  print("45%")
  sleep(1)
  print("68%")
  sleep(1)
  print("99%")
  sleep(5)
  print("100%")
  sleep(1)
  print("Done loading up Combat Simulator now...")  
  sleep(1)
  print("                        ")
  label .beginning
  print(Colour.blue + "In a land not very different to ours, there was a world that had magic and lived in peace!" + Colour.reset)
  sleep(3)
  print(Colour.blue + "The land lived peacefully until..." + Colour.reset)
  sleep(3)
  print(Colour.red + "A DARK FORCE CAME AND STARTED TO TAKE OVER THE WORLD!!")
  sleep(3)
  print("BIT BY BIT THEY RID THE MOST POWERFUL WIZARDS OF THERE POWER!!")
  sleep(3)
  print(Colour.blue + "But a brave wizrd arose and challenged the dark force in a battle...")
  sleep(3)
  print(Colour.blue + "If the the brave wizard won all magic would be restored, but if they lost..." + Colour.reset)
  sleep(3)
  print(Colour.red + "MAGIC WOULD BE LOST FOREVER!!" + Colour.reset)
  print("You are that wizard")
  w_name = input("Whats your name brave wizard?") 
  w_type = randint(1,9)
  if w_type == 1:
    print(Colour.cyan + "You are a fire wizard" + Colour.reset)
    print(" ")
    print(" --------------------------------------------------------")
    print("|                      Move Set                          |")
    print("| -Move 1 : Basic Strike ( 25-50 )                       |")
    print("| -Move 2 : Sheild ( 1-25 )                              |")
    print("| -Move 3 : " + Colour.red + "Fire Punch " + Colour.reset + "( 10-65 )                         |" + Colour.reset)
    print("| -Move 3 : " + Colour.red + "Flame Thrower " + Colour.reset + "( 1-75 )                       |" + Colour.reset)
    print(" --------------------------------------------------------")
  elif w_type == 2:
    print(Colour.cyan + "You are a water wizard" + Colour.reset)
    print(" ")
    print(" --------------------------------------------------------")
    print("|                      Move Set                          |")
    print("| -Move 1 : Basic Strike ( 25-50 )                       |")
    print("| -Move 2 : Sheild ( 1-25 )                              |")
    print("| -Move 3 : " + Colour.blue + "Water Squirt " + Colour.reset + "( 10-65 )                       |" + Colour.reset)
    print("| -Move 3 : " + Colour.blue + "Bubble Blast " + Colour.reset + "( 1-75 )                        |" + Colour.reset)
    print(" --------------------------------------------------------")
  elif w_type == 3:
    print(Colour.cyan + "You are an ice wizard" + Colour.reset)
    print(" ")
    print(" --------------------------------------------------------")
    print("|                      Move Set                          |")
    print("| -Move 1 : Basic Strike ( 25-50 )                       |")
    print("| -Move 2 : Sheild ( 1-25 )                              |")
    print("| -Move 3 : " + Colour.cyan + "Icy Blast " + Colour.reset + "( 10-65 )                          |" + Colour.reset)
    print("| -Move 3 : " + Colour.cyan + "Snowflake Breeze " + Colour.reset + "( 1-75 )                    |" + Colour.reset)
    print(" --------------------------------------------------------")
  elif w_type == 4:
    print(Colour.cyan + "You are an air wizard" + Colour.reset)
    print(" ")
    print(" --------------------------------------------------------")
    print("|                      Move Set                          |")
    print("| -Move 1 : Basic Strike ( 25-50 )                       |")
    print("| -Move 2 : Sheild ( 1-25 )                              |")
    print("| -Move 3 : Air Slash ( 10-65 )                          |")
    print("| -Move 3 : Hurricane ( 1-75 )                           |")
    print(" --------------------------------------------------------")
  elif w_type == 5:
    print(Colour.cyan + "You are an earth based wizard" + Colour.reset)
    print(" ")
    print(" --------------------------------------------------------")
    print("|                      Move Set                          |")
    print("| -Move 1 : Basic Strike ( 25-50 )                       |")
    print("| -Move 2 : Sheild ( 1-25 )                              |")
    print("| -Move 3 : " + Colour.green + "Vine Whip " + Colour.reset + "( 10-65 )                       |" + Colour.reset)
    print("| -Move 3 : " + Colour.green + "Grass Trap " + Colour.reset + "( 1-75 )                       |" + Colour.reset)
    print(" --------------------------------------------------------")
  elif w_type == 6:  
    print(Colour.cyan + "You are a fairy wizard" + Colour.reset)
    print(" ")
    print(" --------------------------------------------------------")
    print("|                      Move Set                          |")
    print("| -Move 1 : Basic Strike ( 25-50 )                       |")
    print("| -Move 2 : Sheild ( 1-25 )                              |")
    print("| -Move 3 : " + Colour.magenta + "Sparkle Strike " + Colour.reset + "( 10-65 )                     |" + Colour.reset)
    print("| -Move 3 : " + Colour.magenta + "Charm Trap " + Colour.reset + "( 1-75 )                          |" + Colour.reset)
    print(" --------------------------------------------------------")
  elif w_type == 7:
    print(Colour.cyan + "You are an electric wizard" + Colour.reset)
    print(" ")
    print(" --------------------------------------------------------")
    print("|                      Move Set                          |")
    print("| -Move 1 : Basic Strike ( 25-50 )                       |")
    print("| -Move 2 : Sheild ( 1-25 )                              |")
    print("| -Move 3 : " + Colour.yellow + "Volt Strike " + Colour.reset + "( 10-65 )                       |" + Colour.reset)
    print("| -Move 3 : " + Colour.yellow + "Thunder Wave " + Colour.reset + "( 1-75 )                       |" + Colour.reset)
    print(" --------------------------------------------------------")
  elif w_type == 8:
    print(Colour.cyan + "You are a dark wizard" + Colour.reset)
    print(" ")
    print(" --------------------------------------------------------")
    print("|                      Move Set                          |")
    print("| -Move 1 : Basic Strike ( 25-50 )                       |")
    print("| -Move 2 : Sheild ( 1-25 )                              |")
    print("| -Move 3 : Dark Strike ( 10-65 )                        |")
    print("| -Move 3 : Black Hole ( 1-75 )                          |")
    print(" --------------------------------------------------------")
  elif w_type == 9:
    print(Colour.cyan + "You are a light wizard" + Colour.reset)
    print(" ")
    print(" --------------------------------------------------------")
    print("|                      Move Set                          |")
    print("| -Move 1 : Basic Strike ( 25-50 )                       |")
    print("| -Move 2 : Sheild ( 1-25 )                              |")
    print("| -Move 3 : Sun Strike ( 10-60 )                         |")
    print("| -Move 3 : Blinding Lights ( 1-75 )                     |")
    print(" --------------------------------------------------------")
  else:
    print("hi :)")
  print("   ")
  print("The first wizard you have to fight is Rookie Wizard Hayden")
  print(Colour.cyan + "Ha you think to can beat me, so called " + str(w_name) + " !!!" + Colour.reset)
  print("    ")
  w_rookie = True
  w_rookie_h = 200
  w_HP = 500
  while w_rookie == True:
    if w_rookie_h < 0:
      w_rookie = False
    else:
      print("")
    if w_HP < 0:
      w_rookie = False
      print("You Lost...")
      sleep(1)
      print("...")
      sleep(1)
      print("...")
      sleep(1)
      print("Lets try again....")
      goto .beginning
    else:
      print("")
    print("                           /\                     ")
    print("                          |  |                    ")
    print("                       __|____|__                 ")
    print("                        | o  o |                  ")
    print("                        (_ ^ __)                  ")
    print("              |^|    _____|  |______              ")
    print("              <_>   /      \/       \             ")
    print("             __|   |___|   o|    |___|            ")
    print("            /  |\_ |  |    o|    || |             ")
    print("           |___|     /     o|    || |             ")
    print(Colour.red + "Enemy HP " + str(w_rookie_h) + Colour.reset)
    print("  ")
    print(Colour.blue + "Your HP " + str(w_HP) + Colour.reset)
    w_rookie_ad =  randint(10,60)
    w_HP = w_HP - w_rookie_ad
    if w_type == 1:
      print("                          ")
      print(" --------------------------------------------------------")
      print("|                      Move Set                          |")
      print("| -Move 1 : Basic Strike ( 25-50 )                       |")
      print("| -Move 2 : Sheild ( 1-25 )                              |")
      print("| -Move 3 : " + Colour.red + "Fire Punch " + Colour.reset + "( 10-65 )                         |" + Colour.reset)
      print("| -Move 3 : " + Colour.red + "Flame Thrower " + Colour.reset + "( 1-75 )                       |" + Colour.reset)
      print(" --------------------------------------------------------")
      move = input("Choose your move! (eg : 1)")
      if move == "1":
        moveone_ad = randint(25,50)
        w_rookie_h = w_rookie_h - moveone_ad
        print("You do " + str(moveone_ad) + " damage")
      elif move == "2":
        movetwo_ad = randint(1,25)
        w_rookie_ad = rookie_ad - movetwo_ad
        print("You save " + str(movetwo_ad) + " damage")
      elif move == "3":
        movethree_ad = randint(10,65)
        w_rookie_h = w_rookie_h - movethree_ad
        print("You do " + str(movethree_ad) + " damage")
      elif move == "4":
        movefour_ad = randint(1,75)
        w_rookie_h = w_rookie_h - movefour_ad
        print("You do " + str(movefour_ad) + " damage")
      print(" ")
    elif w_type == 2:
      print(" --------------------------------------------------------")
      print("|                      Move Set                          |")
      print("| -Move 1 : Basic Strike ( Wait 1 turn )                 |")
      print("| -Move 2 : Sheild ( Wait 2 turns )                      |")
      print("| -Move 3 : " + Colour.blue + "Water Squirt " + Colour.reset + "( Wait 2 turns )                |" + Colour.reset)
      print("| -Move 4 : " + Colour.blue + "Bubble Blast " + Colour.reset + "( Wait 4 turns )                |" + Colour.reset)
      print(" --------------------------------------------------------")
      move = input("Choose your move! (eg : 1)")
      if move == "1":
        moveone_ad = randint(25,50)
        w_rookie_h = w_rookie_h - moveone_ad
        print("You do " + str(moveone_ad) + " damage")
      elif move == "2":
        movetwo_ad = randint(1,25)
        w_rookie_ad = rookie_ad - movetwo_ad
        print("You save " + str(movetwo_ad) + " damage")
      elif move == "3":
        movethree_ad = randint(10,65)
        w_rookie_h = w_rookie_h - movethree_ad
        print("You do " + str(movethree_ad) + " damage")
      elif move == "4":
        movefour_h = randint(1,75)
        w_rookie_h = w_rookie_h - movefour_ad
        print("You do " + str(movefour_ad) + " damage")
      print(" ")
    elif w_type == 3:
      print(" ")
      print(" --------------------------------------------------------")
      print("|                      Move Set                          |")
      print("| -Move 1 : Basic Strike ( 25-50 )                       |")
      print("| -Move 2 : Sheild ( 1-25 )                              |")
      print("| -Move 3 : " + Colour.cyan + "Icy Blast " + Colour.reset + "( 10-65 )                          |" + Colour.reset)
      print("| -Move 3 : " + Colour.cyan + "Snowflake Breeze " + Colour.reset + "( 1-75 )                    |" + Colour.reset)
      print(" --------------------------------------------------------")
      move = input("Choose your move! (eg : 1)")
      if move == "1":
        moveone_ad = randint(25,50)
        w_rookie_h = w_rookie_h - moveone_ad
        print("You do " + str(moveone_ad) + " damage")
      elif move == "2":
        movetwo_ad = randint(1,25)
        w_rookie_ad = rookie_ad - movetwo_ad
        print("You save " + str(movetwo_ad) + " damage")
      elif move == "3":
        movethree_ad = randint(10,65)
        w_rookie_h = w_rookie_h - movethree_ad
        print("You do " + str(movethree_ad) + " damage")
      elif move == "4":
        movefour_ad = randint(1,75)
        w_rookie_h = w_rookie_h - movefour_ad
        print("You do " + str(movefour_ad) + " damage")
      print(" ")
    elif w_type == 4:
      print(" --------------------------------------------------------")
      print("|                      Move Set                          |")
      print("| -Move 1 : Basic Strike ( Wait 1 turn )                 |")
      print("| -Move 2 : Sheild ( Wait 2 turns )                      |")
      print("| -Move 3 : Air Slash ( Wait 2 turns )                   |")
      print("| -Move 4 : Hurricane ( Wait 4 turns )                   |")
      print(" --------------------------------------------------------")
      move = input("Choose your move! (eg : 1)")
      if move == "1":
        moveone_ad = randint(25,50)
        w_rookie_h = w_rookie_h - moveone_ad
        print("You do " + str(moveone_ad) + " damage")
      elif move == "2":
        movetwo_ad = randint(1,25)
        w_rookie_ad = rookie_ad - movetwo_ad
        print("You save " + str(movetwo_ad) + " damage")
      elif move == "3":
        movethree_ad = randint(10,65)
        w_rookie_h = w_rookie_h - movethree_ad
        print("You do " + str(movethree_ad) + " damage")
      elif move == "4":
        movefour_ad = randint(1,75)
        w_rookie_h = w_rookie_h - movefour_ad
        print("You do " + str(movefour_ad) + " damage")
      print(" ")
    elif w_type == 5:
      print(" ")
      print(" --------------------------------------------------------")
      print("|                      Move Set                          |")
      print("| -Move 1 : Basic Strike ( Wait 1 turn )                 |")
      print("| -Move 2 : Sheild ( Wait 2 turns )                      |")
      print("| -Move 3 : " + Colour.green + "Vine Whip " + Colour.reset + "( Wait 2 turns )                |" + Colour.reset)
      print("| -Move 4 : " + Colour.green + "Grass Trap " + Colour.reset + "( Wait 4 turns )               |" + Colour.reset)
      print(" --------------------------------------------------------")
      move = input("Choose your move! (eg : 1)")
      if move == "1":
        moveone_ad = randint(25,50)
        w_rookie_h = w_rookie_h - moveone_ad
        print("You do " + str(moveone_ad) + " damage")
      elif move == "2":
        movetwo_ad = randint(1,25)
        w_rookie_ad = rookie_ad - movetwo_ad
        print("You save " + str(movetwo_ad) + " damage")
      elif move == "3":
        movethree_ad = randint(10,65)
        w_rookie_h = w_rookie_h - movethree_ad
        print("You do " + str(movethree_ad) + " damage")
      elif move == "4":
        movefour_ad = randint(1,75)
        w_rookie_h = w_rookie_h - movefour_ad
        print("You do " + str(movefour_ad) + " damage")
      print(" ")
    elif w_type == 6:  
      print(" ")
      print(" --------------------------------------------------------")
      print("|                      Move Set                          |")
      print("| -Move 1 : Basic Strike ( Wait 1 turn )                 |")
      print("| -Move 2 : Sheild ( Wait 2 turns )                      |")
      print("| -Move 3 : " + Colour.magenta + "Sparkle Strike " + Colour.reset + "( Wait 2 turns )              |" + Colour.reset)
      print("| -Move 4 : " + Colour.magenta + "Charm Trap " + Colour.reset + "( Wait 4 turns )                  |" + Colour.reset)
      print(" --------------------------------------------------------")
      move = input("Choose your move! (eg : 1)")
      if move == "1":
        moveone_ad = randint(25,50)
        w_rookie_h = w_rookie_h - moveone_ad
        print("You do " + str(moveone_ad) + " damage")
      elif move == "2":
        movetwo_ad = randint(1,25)
        w_rookie_ad = rookie_ad - movetwo_ad
        print("You save " + str(movetwo_ad) + " damage")
      elif move == "3":
        movethree_ad = randint(10,65)
        w_rookie_h = w_rookie_h - movethree_ad
        print("You do " + str(movethree_ad) + " damage")
      elif move == "4":
        movefour_ad = randint(1,75)
        w_rookie_h = w_rookie_h - movefour_ad
        print("You do " + str(movefour_ad) + " damage")
      print(" ")
    elif w_type == 7:
      print(" --------------------------------------------------------")
      print("|                      Move Set                          |")
      print("| -Move 1 : Basic Strike ( Wait 1 turn )                 |")
      print("| -Move 2 : Sheild ( Wait 2 turns )                      |")
      print("| -Move 3 : " + Colour.yellow + "Volt Strike " + Colour.reset + "( Wait 2 turns )                  |" + Colour.reset)
      print("| -Move 4 : " + Colour.yellow + "Thunder Wave " + Colour.reset + "( Wait 4 turns )               |" + Colour.reset)
      print(" --------------------------------------------------------")
      move = input("Choose your move! (eg : 1)")
      if move == "1":
        moveone_ad = randint(25,50)
        w_rookie_h = w_rookie_h - moveone_ad
        print("You do " + str(moveone_ad) + " damage")
      elif move == "2":
        movetwo_ad = randint(1,25)
        w_rookie_ad = rookie_ad - movetwo_ad
        print("You save " + str(movetwo_ad) + " damage")
      elif move == "3":
        movethree_ad = randint(10,65)
        w_rookie_h = w_rookie_h - movethree_ad
        print("You do " + str(movethree_ad) + " damage")
      elif move == "4":
        movefour_ad = randint(1,75)
        w_rookie_h = w_rookie_h - movefour_ad
        print("You do " + str(movefour_ad) + " damage")
      print(" ")
    elif w_type == 8:
      print(" ")
      print(" --------------------------------------------------------")
      print("|                      Move Set                          |")
      print("| -Move 1 : Basic Strike ( Wait 1 turn )                 |")
      print("| -Move 2 : Sheild ( Wait 2 turns )                      |")
      print("| -Move 3 : Dark Strike ( Wait 2 turns )                 |")
      print("| -Move 4 : Black Hole ( Wait 4 turns )                  |")
      print(" --------------------------------------------------------")
      move = input("Choose your move! (eg : 1)")
      if move == "1":
        moveone_ad = randint(25,50)
        w_rookie_h = w_rookie_h - moveone_ad
        print("You do " + str(moveone_ad) + " damage")
      elif move == "2":
        movetwo_ad = randint(1,25)
        w_rookie_ad = rookie_ad - movetwo_ad
        print("You save " + str(movetwo_ad) + " damage")
      elif move == "3":
        movethree_ad = randint(10,65)
        w_rookie_h = w_rookie_h - movethree_ad
        print("You do " + str(movethree_ad) + " damage")
      elif move == "4":
        movefour_ad = randint(1,75)
        w_rookie_h = w_rookie_h - movefour_ad
        print("You do " + str(movefour_ad) + " damage")
      print(" ")
    elif w_type == 9:
      print(" ")
      print(" --------------------------------------------------------")
      print("|                      Move Set                          |")
      print("| -Move 1 : Basic Strike ( Wait 1 turn )                 |")
      print("| -Move 2 : Sheild ( Wait 2 turns )                      |")
      print("| -Move 3 : Sun Strike ( Wait 2 turns )                  |")
      print("| -Move 4 : Blinding Lights ( Wait 4 turns )             |")
      print(" --------------------------------------------------------")
      move = input("Choose your move! (eg : 1)")
      if move == "1":
        moveone_ad = randint(25,50)
        w_rookie_h = w_rookie_h - moveone_ad
        print("You do " + str(moveone_ad) + " damage")
      elif move == "2":
        movetwo_ad = randint(1,25)
        w_rookie_ad = rookie_ad - movetwo_ad
        print("You save " + str(movetwo_ad) + " damage")
      elif move == "3":
        movethree_ad = randint(10,65)
        w_rookie_h = w_rookie_h - movethree_ad
        print("You do " + str(movethree_ad) + " damage")
      elif move == "4":
        movefour_ad = randint(1,75)
        w_rookie_h = w_rookie_h - movefour_ad
        print("You do " + str(movefour_ad) + " damage")
      print(" ")
    else:
      print("hi :)")
  print("The second wizard you have to fight is Air Wizard Mars")
  print(Colour.cyan + "Ha you think to can beat me rookie, so called " + str(w_name) + " !!!" + Colour.reset)
  print("    ")
  w_rookie = True
  w_rookie_h = 400
  w_HP = 500
  while w_rookie == True:
    if w_rookie_h < 0:
      w_rookie = False
    else:
      print("")
    if w_HP < 0:
      w_rookie = False
      print("You Lost...")
      sleep(1)
      print("...")
      sleep(1)
      print("...")
      sleep(1)
      print("Lets try again....")
      goto .beginning
    else:
      print("")
    print("                           /\                     ")
    print("                          |  |                    ")
    print("                       __|____|__                 ")
    print("                       || o\/o ||                 ")
    print("                       /(_ v __)\                 ")
    print("              |^|    _|___|  |___|__              ")
    print("              <_>   /      \/       \             ")
    print("             __|   |___|   o|    |___|            ")
    print("            /  |\_ |  |    o|    || |             ")
    print("           |___|     /     o|    || |             ")
    print(Colour.red + "Enemy HP " + str(w_rookie_h) + Colour.reset)
    print("  ")
    print(Colour.blue + "Your HP " + str(w_HP) + Colour.reset)
    w_rookie_ad =  randint(10,60)
    w_HP = w_HP - w_rookie_ad
    if w_type == 1:
      print("                          ")
      print(" --------------------------------------------------------")
      print("|                      Move Set                          |")
      print("| -Move 1 : Basic Strike ( 25-50 )                       |")
      print("| -Move 2 : Sheild ( 1-25 )                              |")
      print("| -Move 3 : " + Colour.red + "Fire Punch " + Colour.reset + "( 10-65 )                         |" + Colour.reset)
      print("| -Move 3 : " + Colour.red + "Flame Thrower " + Colour.reset + "( 1-75 )                       |" + Colour.reset)
      print(" --------------------------------------------------------")
      move = input("Choose your move! (eg : 1)")
      if move == "1":
        moveone_ad = randint(25,50)
        w_rookie_h = w_rookie_h - moveone_ad
        print("You do " + str(moveone_ad) + " damage")
      elif move == "2":
        movetwo_ad = randint(1,25)
        w_rookie_ad = rookie_ad - movetwo_ad
        print("You save " + str(movetwo_ad) + " damage")
      elif move == "3":
        movethree_ad = randint(10,65)
        w_rookie_h = w_rookie_h - movethree_ad
        print("You do " + str(movethree_ad) + " damage")
      elif move == "4":
        movefour_ad = randint(1,75)
        w_rookie_h = w_rookie_h - movefour_ad
        print("You do " + str(movefour_ad) + " damage")
      print(" ")
    elif w_type == 2:
      print(Colour.cyan + "You are a water wizard" + Colour.reset)
      print(" ")
      print(" --------------------------------------------------------")
      print("|                      Move Set                          |")
      print("| -Move 1 : Basic Strike ( 25-50 )                       |")
      print("| -Move 2 : Sheild ( 1-25 )                              |")
      print("| -Move 3 : " + Colour.blue + "Water Squirt " + Colour.reset + "( 10-65 )                       |" + Colour.reset)
      print("| -Move 3 : " + Colour.blue + "Bubble Blast " + Colour.reset + "( 1-75 )                        |" + Colour.reset)
      print(" --------------------------------------------------------")
      move = input("Choose your move! (eg : 1)")
      if move == "1":
        moveone_ad = randint(25,50)
        w_rookie_h = w_rookie_h - moveone_ad
        print("You do " + str(moveone_ad) + " damage")
      elif move == "2":
        movetwo_ad = randint(1,25)
        w_rookie_ad = rookie_ad - movetwo_ad
        print("You save " + str(movetwo_ad) + " damage")
      elif move == "3":
        movethree_ad = randint(10,65)
        w_rookie_h = w_rookie_h - movethree_ad
        print("You do " + str(movethree_ad) + " damage")
      elif move == "4":
        movefour_h = randint(1,75)
        w_rookie_h = w_rookie_h - movefour_ad
        print("You do " + str(movefour_ad) + " damage")
      print(" ")
    elif w_type == 3:
      print(" ")
      print(" --------------------------------------------------------")
      print("|                      Move Set                          |")
      print("| -Move 1 : Basic Strike ( 25-50 )                       |")
      print("| -Move 2 : Sheild ( 1-25 )                              |")
      print("| -Move 3 : " + Colour.cyan + "Icy Blast " + Colour.reset + "( 10-65 )                          |" + Colour.reset)
      print("| -Move 3 : " + Colour.cyan + "Snowflake Breeze " + Colour.reset + "( 1-75 )                    |" + Colour.reset)
      print(" --------------------------------------------------------")
      move = input("Choose your move! (eg : 1)")
      if move == "1":
        moveone_ad = randint(25,50)
        w_rookie_h = w_rookie_h - moveone_ad
        print("You do " + str(moveone_ad) + " damage")
      elif move == "2":
        movetwo_ad = randint(1,25)
        w_rookie_ad = rookie_ad - movetwo_ad
        print("You save " + str(movetwo_ad) + " damage")
      elif move == "3":
        movethree_ad = randint(10,65)
        w_rookie_h = w_rookie_h - movethree_ad
        print("You do " + str(movethree_ad) + " damage")
      elif move == "4":
        movefour_ad = randint(1,75)
        w_rookie_h = w_rookie_h - movefour_ad
        print("You do " + str(movefour_ad) + " damage")
      print(" ")
    elif w_type == 4:
      print(" --------------------------------------------------------")
      print("|                      Move Set                          |")
      print("| -Move 1 : Basic Strike ( Wait 1 turn )                 |")
      print("| -Move 2 : Sheild ( Wait 2 turns )                      |")
      print("| -Move 3 : Air Slash ( Wait 2 turns )                   |")
      print("| -Move 4 : Hurricane ( Wait 4 turns )                   |")
      print(" --------------------------------------------------------")
      move = input("Choose your move! (eg : 1)")
      if move == "1":
        moveone_ad = randint(25,50)
        w_rookie_h = w_rookie_h - moveone_ad
        print("You do " + str(moveone_ad) + " damage")
      elif move == "2":
        movetwo_ad = randint(1,25)
        w_rookie_ad = rookie_ad - movetwo_ad
        print("You save " + str(movetwo_ad) + " damage")
      elif move == "3":
        movethree_ad = randint(10,65)
        w_rookie_h = w_rookie_h - movethree_ad
        print("You do " + str(movethree_ad) + " damage")
      elif move == "4":
        movefour_ad = randint(1,75)
        w_rookie_h = w_rookie_h - movefour_ad
        print("You do " + str(movefour_ad) + " damage")
      print(" ")
    elif w_type == 5:
      print(" ")
      print(" --------------------------------------------------------")
      print("|                      Move Set                          |")
      print("| -Move 1 : Basic Strike ( Wait 1 turn )                 |")
      print("| -Move 2 : Sheild ( Wait 2 turns )                      |")
      print("| -Move 3 : " + Colour.green + "Vine Whip " + Colour.reset + "( Wait 2 turns )                |" + Colour.reset)
      print("| -Move 4 : " + Colour.green + "Grass Trap " + Colour.reset + "( Wait 4 turns )               |" + Colour.reset)
      print(" --------------------------------------------------------")
      move = input("Choose your move! (eg : 1)")
      if move == "1":
        moveone_ad = randint(25,50)
        w_rookie_h = w_rookie_h - moveone_ad
        print("You do " + str(moveone_ad) + " damage")
      elif move == "2":
        movetwo_ad = randint(1,25)
        w_rookie_ad = rookie_ad - movetwo_ad
        print("You save " + str(movetwo_ad) + " damage")
      elif move == "3":
        movethree_ad = randint(10,65)
        w_rookie_h = w_rookie_h - movethree_ad
        print("You do " + str(movethree_ad) + " damage")
      elif move == "4":
        movefour_ad = randint(1,75)
        w_rookie_h = w_rookie_h - movefour_ad
        print("You do " + str(movefour_ad) + " damage")
      print(" ")
    elif w_type == 6:  
      print(" ")
      print(" --------------------------------------------------------")
      print("|                      Move Set                          |")
      print("| -Move 1 : Basic Strike ( Wait 1 turn )                 |")
      print("| -Move 2 : Sheild ( Wait 2 turns )                      |")
      print("| -Move 3 : " + Colour.magenta + "Sparkle Strike " + Colour.reset + "( Wait 2 turns )              |" + Colour.reset)
      print("| -Move 4 : " + Colour.magenta + "Charm Trap " + Colour.reset + "( Wait 4 turns )                  |" + Colour.reset)
      print(" --------------------------------------------------------")
      move = input("Choose your move! (eg : 1)")
      if move == "1":
        moveone_ad = randint(25,50)
        w_rookie_h = w_rookie_h - moveone_ad
        print("You do " + str(moveone_ad) + " damage")
      elif move == "2":
        movetwo_ad = randint(1,25)
        w_rookie_ad = rookie_ad - movetwo_ad
        print("You save " + str(movetwo_ad) + " damage")
      elif move == "3":
        movethree_ad = randint(10,65)
        w_rookie_h = w_rookie_h - movethree_ad
        print("You do " + str(movethree_ad) + " damage")
      elif move == "4":
        movefour_ad = randint(1,75)
        w_rookie_h = w_rookie_h - movefour_ad
        print("You do " + str(movefour_ad) + " damage")
      print(" ")
    elif w_type == 7:
      print(" --------------------------------------------------------")
      print("|                      Move Set                          |")
      print("| -Move 1 : Basic Strike ( Wait 1 turn )                 |")
      print("| -Move 2 : Sheild ( Wait 2 turns )                      |")
      print("| -Move 3 : " + Colour.yellow + "Volt Strike " + Colour.reset + "( Wait 2 turns )                  |" + Colour.reset)
      print("| -Move 4 : " + Colour.yellow + "Thunder Wave " + Colour.reset + "( Wait 4 turns )               |" + Colour.reset)
      print(" --------------------------------------------------------")
      move = input("Choose your move! (eg : 1)")
      if move == "1":
        moveone_ad = randint(25,50)
        w_rookie_h = w_rookie_h - moveone_ad
        print("You do " + str(moveone_ad) + " damage")
      elif move == "2":
        movetwo_ad = randint(1,25)
        w_rookie_ad = rookie_ad - movetwo_ad
        print("You save " + str(movetwo_ad) + " damage")
      elif move == "3":
        movethree_ad = randint(10,65)
        w_rookie_h = w_rookie_h - movethree_ad
        print("You do " + str(movethree_ad) + " damage")
      elif move == "4":
        movefour_ad = randint(1,75)
        w_rookie_h = w_rookie_h - movefour_ad
        print("You do " + str(movefour_ad) + " damage")
      print(" ")
    elif w_type == 8:
      print(" ")
      print(" --------------------------------------------------------")
      print("|                      Move Set                          |")
      print("| -Move 1 : Basic Strike ( Wait 1 turn )                 |")
      print("| -Move 2 : Sheild ( Wait 2 turns )                      |")
      print("| -Move 3 : Dark Strike ( Wait 2 turns )                 |")
      print("| -Move 4 : Black Hole ( Wait 4 turns )                  |")
      print(" --------------------------------------------------------")
      move = input("Choose your move! (eg : 1)")
      if move == "1":
        moveone_ad = randint(25,50)
        w_rookie_h = w_rookie_h - moveone_ad
        print("You do " + str(moveone_ad) + " damage")
      elif move == "2":
        movetwo_ad = randint(1,25)
        w_rookie_ad = rookie_ad - movetwo_ad
        print("You save " + str(movetwo_ad) + " damage")
      elif move == "3":
        movethree_ad = randint(10,65)
        w_rookie_h = w_rookie_h - movethree_ad
        print("You do " + str(movethree_ad) + " damage")
      elif move == "4":
        movefour_ad = randint(1,75)
        w_rookie_h = w_rookie_h - movefour_ad
        print("You do " + str(movefour_ad) + " damage")
      print(" ")
    elif w_type == 9:
      print(" ")
      print(" --------------------------------------------------------")
      print("|                      Move Set                          |")
      print("| -Move 1 : Basic Strike ( Wait 1 turn )                 |")
      print("| -Move 2 : Sheild ( Wait 2 turns )                      |")
      print("| -Move 3 : Sun Strike ( Wait 2 turns )                  |")
      print("| -Move 4 : Blinding Lights ( Wait 4 turns )             |")
      print(" --------------------------------------------------------")
      move = input("Choose your move! (eg : 1)")
      if move == "1":
        moveone_ad = randint(25,50)
        w_rookie_h = w_rookie_h - moveone_ad
        print("You do " + str(moveone_ad) + " damage")
      elif move == "2":
        movetwo_ad = randint(1,25)
        w_rookie_ad = rookie_ad - movetwo_ad
        print("You save " + str(movetwo_ad) + " damage")
      elif move == "3":
        movethree_ad = randint(10,65)
        w_rookie_h = w_rookie_h - movethree_ad
        print("You do " + str(movethree_ad) + " damage")
      elif move == "4":
        movefour_ad = randint(1,75)
        w_rookie_h = w_rookie_h - movefour_ad
        print("You do " + str(movefour_ad) + " damage")
      print(" ")
    else:
      print("hi :)")
      tpopcb = input("Whats you wizrd power")
      if tpopcb == "fire" or "ice" or "water":
        print("Have a good day")
      else:
        if tpopcb.isupper:
          print("Thats cool")
        elif tpopcb.islower:
          print(":(((((((")
  print("The first wizard you have to fight is Aprentice Fairy Wizard Charli")
  print(Colour.cyan + "Ha you think to can beat me, so called " + str(w_name) + " !!!" + Colour.reset)
  print("    ")
  w_rookie = True
  w_rookie_h = 600
  w_HP = 500
  while w_rookie == True:
    if w_rookie_h < 0:
      w_rookie = False
    else:
      print("")
    if w_HP < 0:
      w_rookie = False
      print("You Lost...")
      sleep(1)
      print("...")
      sleep(1)
      print("...")
      sleep(1)
      print("Lets try again....")
      goto .beginning
    else:
      print("")
    print("                           /\                     ")
    print("                          |  |                    ")
    print("                      ___|____|___                ")
    print("                      ||  \ /   ||                ")
    print("                      || o   o  ||                ")
    print("                      / \_ n __/  \               ")
    print("              |^|    |____|  |_____|              ")
    print("              <_>   /      \/       \             ")
    print("             __|   |___|   o|    |___|            ")
    print("            /__|\_ |  |    o|    || |             ")
    print("           |___|     /     o|    || |             ")
    print(Colour.red + "Enemy HP " + str(w_rookie_h) + Colour.reset)
    print("  ")
    print(Colour.blue + "Your HP " + str(w_HP) + Colour.reset)
    w_rookie_ad =  randint(10,60)
    w_HP = w_HP - w_rookie_ad
    if w_type == 1:
      print("                          ")
      print(" --------------------------------------------------------")
      print("|                      Move Set                          |")
      print("| -Move 1 : Basic Strike ( 25-50 )                       |")
      print("| -Move 2 : Sheild ( 1-25 )                              |")
      print("| -Move 3 : " + Colour.red + "Fire Punch " + Colour.reset + "( 10-65 )                         |" + Colour.reset)
      print("| -Move 3 : " + Colour.red + "Flame Thrower " + Colour.reset + "( 1-75 )                       |" + Colour.reset)
      print(" --------------------------------------------------------")
      move = input("Choose your move! (eg : 1)")
      if move == "1":
        moveone_ad = randint(25,50)
        w_rookie_h = w_rookie_h - moveone_ad
        print("You do " + str(moveone_ad) + " damage")
      elif move == "2":
        movetwo_ad = randint(1,25)
        w_rookie_ad = rookie_ad - movetwo_ad
        print("You save " + str(movetwo_ad) + " damage")
      elif move == "3":
        movethree_ad = randint(10,65)
        w_rookie_h = w_rookie_h - movethree_ad
        print("You do " + str(movethree_ad) + " damage")
      elif move == "4":
        movefour_ad = randint(1,75)
        w_rookie_h = w_rookie_h - movefour_ad
        print("You do " + str(movefour_ad) + " damage")
      print(" ")
    elif w_type == 2:
      print(Colour.cyan + "You are a water wizard" + Colour.reset)
      print(" ")
      print(" --------------------------------------------------------")
      print("|                      Move Set                          |")
      print("| -Move 1 : Basic Strike ( 25-50 )                       |")
      print("| -Move 2 : Sheild ( 1-25 )                              |")
      print("| -Move 3 : " + Colour.blue + "Water Squirt " + Colour.reset + "( 10-65 )                       |" + Colour.reset)
      print("| -Move 3 : " + Colour.blue + "Bubble Blast " + Colour.reset + "( 1-75 )                        |" + Colour.reset)
      print(" --------------------------------------------------------")
      move = input("Choose your move! (eg : 1)")
      if move == "1":
        moveone_ad = randint(25,50)
        w_rookie_h = w_rookie_h - moveone_ad
        print("You do " + str(moveone_ad) + " damage")
      elif move == "2":
        movetwo_ad = randint(1,25)
        w_rookie_ad = rookie_ad - movetwo_ad
        print("You save " + str(movetwo_ad) + " damage")
      elif move == "3":
        movethree_ad = randint(10,65)
        w_rookie_h = w_rookie_h - movethree_ad
        print("You do " + str(movethree_ad) + " damage")
      elif move == "4":
        movefour_h = randint(1,75)
        w_rookie_h = w_rookie_h - movefour_ad
        print("You do " + str(movefour_ad) + " damage")
      print(" ")
    elif w_type == 3:
      print(" ")
      print(" --------------------------------------------------------")
      print("|                      Move Set                          |")
      print("| -Move 1 : Basic Strike ( 25-50 )                       |")
      print("| -Move 2 : Sheild ( 1-25 )                              |")
      print("| -Move 3 : " + Colour.cyan + "Icy Blast " + Colour.reset + "( 10-65 )                          |" + Colour.reset)
      print("| -Move 3 : " + Colour.cyan + "Snowflake Breeze " + Colour.reset + "( 1-75 )                    |" + Colour.reset)
      print(" --------------------------------------------------------")
      move = input("Choose your move! (eg : 1)")
      if move == "1":
        moveone_ad = randint(25,50)
        w_rookie_h = w_rookie_h - moveone_ad
        print("You do " + str(moveone_ad) + " damage")
      elif move == "2":
        movetwo_ad = randint(1,25)
        w_rookie_ad = rookie_ad - movetwo_ad
        print("You save " + str(movetwo_ad) + " damage")
      elif move == "3":
        movethree_ad = randint(10,65)
        w_rookie_h = w_rookie_h - movethree_ad
        print("You do " + str(movethree_ad) + " damage")
      elif move == "4":
        movefour_ad = randint(1,75)
        w_rookie_h = w_rookie_h - movefour_ad
        print("You do " + str(movefour_ad) + " damage")
      print(" ")
    elif w_type == 4:
      print(" --------------------------------------------------------")
      print("|                      Move Set                          |")
      print("| -Move 1 : Basic Strike ( Wait 1 turn )                 |")
      print("| -Move 2 : Sheild ( Wait 2 turns )                      |")
      print("| -Move 3 : Air Slash ( Wait 2 turns )                   |")
      print("| -Move 4 : Hurricane ( Wait 4 turns )                   |")
      print(" --------------------------------------------------------")
      move = input("Choose your move! (eg : 1)")
      if move == "1":
        moveone_ad = randint(25,50)
        w_rookie_h = w_rookie_h - moveone_ad
        print("You do " + str(moveone_ad) + " damage")
      elif move == "2":
        movetwo_ad = randint(1,25)
        w_rookie_ad = rookie_ad - movetwo_ad
        print("You save " + str(movetwo_ad) + " damage")
      elif move == "3":
        movethree_ad = randint(10,65)
        w_rookie_h = w_rookie_h - movethree_ad
        print("You do " + str(movethree_ad) + " damage")
      elif move == "4":
        movefour_ad = randint(1,75)
        w_rookie_h = w_rookie_h - movefour_ad
        print("You do " + str(movefour_ad) + " damage")
      print(" ")
    elif w_type == 5:
      print(" ")
      print(" --------------------------------------------------------")
      print("|                      Move Set                          |")
      print("| -Move 1 : Basic Strike ( Wait 1 turn )                 |")
      print("| -Move 2 : Sheild ( Wait 2 turns )                      |")
      print("| -Move 3 : " + Colour.green + "Vine Whip " + Colour.reset + "( Wait 2 turns )                |" + Colour.reset)
      print("| -Move 4 : " + Colour.green + "Grass Trap " + Colour.reset + "( Wait 4 turns )               |" + Colour.reset)
      print(" --------------------------------------------------------")
      move = input("Choose your move! (eg : 1)")
      if move == "1":
        moveone_ad = randint(25,50)
        w_rookie_h = w_rookie_h - moveone_ad
        print("You do " + str(moveone_ad) + " damage")
      elif move == "2":
        movetwo_ad = randint(1,25)
        w_rookie_ad = rookie_ad - movetwo_ad
        print("You save " + str(movetwo_ad) + " damage")
      elif move == "3":
        movethree_ad = randint(10,65)
        w_rookie_h = w_rookie_h - movethree_ad
        print("You do " + str(movethree_ad) + " damage")
      elif move == "4":
        movefour_ad = randint(1,75)
        w_rookie_h = w_rookie_h - movefour_ad
        print("You do " + str(movefour_ad) + " damage")
      print(" ")
    elif w_type == 6:  
      print(" ")
      print(" --------------------------------------------------------")
      print("|                      Move Set                          |")
      print("| -Move 1 : Basic Strike ( Wait 1 turn )                 |")
      print("| -Move 2 : Sheild ( Wait 2 turns )                      |")
      print("| -Move 3 : " + Colour.magenta + "Sparkle Strike " + Colour.reset + "( Wait 2 turns )              |" + Colour.reset)
      print("| -Move 4 : " + Colour.magenta + "Charm Trap " + Colour.reset + "( Wait 4 turns )                  |" + Colour.reset)
      print(" --------------------------------------------------------")
      move = input("Choose your move! (eg : 1)")
      if move == "1":
        moveone_ad = randint(25,50)
        w_rookie_h = w_rookie_h - moveone_ad
        print("You do " + str(moveone_ad) + " damage")
      elif move == "2":
        movetwo_ad = randint(1,25)
        w_rookie_ad = rookie_ad - movetwo_ad
        print("You save " + str(movetwo_ad) + " damage")
      elif move == "3":
        movethree_ad = randint(10,65)
        w_rookie_h = w_rookie_h - movethree_ad
        print("You do " + str(movethree_ad) + " damage")
      elif move == "4":
        movefour_ad = randint(1,75)
        w_rookie_h = w_rookie_h - movefour_ad
        print("You do " + str(movefour_ad) + " damage")
      print(" ")
    elif w_type == 7:
      print(" --------------------------------------------------------")
      print("|                      Move Set                          |")
      print("| -Move 1 : Basic Strike ( Wait 1 turn )                 |")
      print("| -Move 2 : Sheild ( Wait 2 turns )                      |")
      print("| -Move 3 : " + Colour.yellow + "Volt Strike " + Colour.reset + "( Wait 2 turns )                  |" + Colour.reset)
      print("| -Move 4 : " + Colour.yellow + "Thunder Wave " + Colour.reset + "( Wait 4 turns )               |" + Colour.reset)
      print(" --------------------------------------------------------")
      move = input("Choose your move! (eg : 1)")
      if move == "1":
        moveone_ad = randint(25,50)
        w_rookie_h = w_rookie_h - moveone_ad
        print("You do " + str(moveone_ad) + " damage")
      elif move == "2":
        movetwo_ad = randint(1,25)
        w_rookie_ad = rookie_ad - movetwo_ad
        print("You save " + str(movetwo_ad) + " damage")
      elif move == "3":
        movethree_ad = randint(10,65)
        w_rookie_h = w_rookie_h - movethree_ad
        print("You do " + str(movethree_ad) + " damage")
      elif move == "4":
        movefour_ad = randint(1,75)
        w_rookie_h = w_rookie_h - movefour_ad
        print("You do " + str(movefour_ad) + " damage")
      print(" ")
    elif w_type == 8:
      print(" ")
      print(" --------------------------------------------------------")
      print("|                      Move Set                          |")
      print("| -Move 1 : Basic Strike ( Wait 1 turn )                 |")
      print("| -Move 2 : Sheild ( Wait 2 turns )                      |")
      print("| -Move 3 : Dark Strike ( Wait 2 turns )                 |")
      print("| -Move 4 : Black Hole ( Wait 4 turns )                  |")
      print(" --------------------------------------------------------")
      move = input("Choose your move! (eg : 1)")
      if move == "1":
        moveone_ad = randint(25,50)
        w_rookie_h = w_rookie_h - moveone_ad
        print("You do " + str(moveone_ad) + " damage")
      elif move == "2":
        movetwo_ad = randint(1,25)
        w_rookie_ad = rookie_ad - movetwo_ad
        print("You save " + str(movetwo_ad) + " damage")
      elif move == "3":
        movethree_ad = randint(10,65)
        w_rookie_h = w_rookie_h - movethree_ad
        print("You do " + str(movethree_ad) + " damage")
      elif move == "4":
        movefour_ad = randint(1,75)
        w_rookie_h = w_rookie_h - movefour_ad
        print("You do " + str(movefour_ad) + " damage")
      print(" ")
    elif w_type == 9:
      print(" ")
      print(" --------------------------------------------------------")
      print("|                      Move Set                          |")
      print("| -Move 1 : Basic Strike ( Wait 1 turn )                 |")
      print("| -Move 2 : Sheild ( Wait 2 turns )                      |")
      print("| -Move 3 : Sun Strike ( Wait 2 turns )                  |")
      print("| -Move 4 : Blinding Lights ( Wait 4 turns )             |")
      print(" --------------------------------------------------------")
      move = input("Choose your move! (eg : 1)")
      if move == "1":
        moveone_ad = randint(25,50)
        w_rookie_h = w_rookie_h - moveone_ad
        print("You do " + str(moveone_ad) + " damage")
      elif move == "2":
        movetwo_ad = randint(1,25)
        w_rookie_ad = rookie_ad - movetwo_ad
        print("You save " + str(movetwo_ad) + " damage")
      elif move == "3":
        movethree_ad = randint(10,65)
        w_rookie_h = w_rookie_h - movethree_ad
        print("You do " + str(movethree_ad) + " damage")
      elif move == "4":
        movefour_ad = randint(1,75)
        w_rookie_h = w_rookie_h - movefour_ad
        print("You do " + str(movefour_ad) + " damage")
      print(" ")
    else:
      print("hi :)")
      tpopcb = input("Whats you wizrd power")
      if tpopcb == "fire" or "ice" or "water":
        print("Have a good day")
      else:
        if tpopcb.isupper:
          print("Thats cool")
        elif tpopcb.islower:
          print(":(((((((")

  print("The first wizard you have to fight is Dark Force Leader, Dark Wizard Helga")
  print(Colour.cyan + "Ha you think to can beat me, so called " + str(w_name) + " !!!" + Colour.reset)
  print("    ")
  w_rookie = True
  w_rookie_h = 1000
  w_HP = 500
  while w_rookie == True:
    if w_rookie_h < 0:
      w_rookie = False
    else:
      print("")
    if w_HP < 0:
      w_rookie = False
      print("You Lost...")
      sleep(1)
      print("...")
      sleep(1)
      print("...")
      sleep(1)
      print("Lets try again....")
      goto .beginning
    else:
      print("")
    print("                           /\                     ")
    print("                          |  |                    ")
    print("                          /  \                    ")
    print("                         |    |                   ")
    print("                    ____/______\____              ")
    print("                      ||  \ /   ||                ")
    print("                      || o   O  ||                ")
    print("                      ||  c     ||                ")
    print("                      / \_ O __/  \               ")
    print("              |^|    |____|  |_____|              ")
    print("              <_>   /      \/       \             ")
    print("             __|   |___|   o|    |___|            ")
    print("            /__|\_ |  |    o|    || |             ")
    print("           |___|     /     o|    || |             ")

    print(Colour.red + "Enemy HP " + str(w_rookie_h) + Colour.reset)
    print("  ")
    print(Colour.blue + "Your HP " + str(w_HP) + Colour.reset)
    w_rookie_ad =  randint(10,60)
    w_HP = w_HP - w_rookie_ad
    if w_type == 1:
      print("                          ")
      print(" --------------------------------------------------------")
      print("|                      Move Set                          |")
      print("| -Move 1 : Basic Strike ( 25-50 )                       |")
      print("| -Move 2 : Sheild ( 1-25 )                              |")
      print("| -Move 3 : " + Colour.red + "Fire Punch " + Colour.reset + "( 10-65 )                         |" + Colour.reset)
      print("| -Move 3 : " + Colour.red + "Flame Thrower " + Colour.reset + "( 1-75 )                       |" + Colour.reset)
      print(" --------------------------------------------------------")
      move = input("Choose your move! (eg : 1)")
      if move == "1":
        moveone_ad = randint(25,50)
        w_rookie_h = w_rookie_h - moveone_ad
        print("You do " + str(moveone_ad) + " damage")
      elif move == "2":
        movetwo_ad = randint(1,25)
        w_rookie_ad = rookie_ad - movetwo_ad
        print("You save " + str(movetwo_ad) + " damage") 
      elif move == "3":
        movethree_ad = randint(10,65)
        w_rookie_h = w_rookie_h - movethree_ad
        print("You do " + str(movethree_ad) + " damage")
      elif move == "4":
        movefour_ad = randint(1,75)
        w_rookie_h = w_rookie_h - movefour_ad
        print("You do " + str(movefour_ad) + " damage")
      print(" ")
    elif w_type == 2:
      print(Colour.cyan + "You are a water wizard" + Colour.reset)
      print(" ")
      print(" --------------------------------------------------------")
      print("|                      Move Set                          |")
      print("| -Move 1 : Basic Strike ( 25-50 )                       |")
      print("| -Move 2 : Sheild ( 1-25 )                              |")
      print("| -Move 3 : " + Colour.blue + "Water Squirt " + Colour.reset + "( 10-65 )                       |" + Colour.reset)
      print("| -Move 3 : " + Colour.blue + "Bubble Blast " + Colour.reset + "( 1-75 )                        |" + Colour.reset)
      print(" --------------------------------------------------------")
      move = input("Choose your move! (eg : 1)")
      if move == "1":
        moveone_ad = randint(25,50)
        w_rookie_h = w_rookie_h - moveone_ad
        print("You do " + str(moveone_ad) + " damage")
      elif move == "2":
        movetwo_ad = randint(1,25)
        w_rookie_ad = rookie_ad - movetwo_ad
        print("You save " + str(movetwo_ad) + " damage")
      elif move == "3":
        movethree_ad = randint(10,65)
        w_rookie_h = w_rookie_h - movethree_ad
        print("You do " + str(movethree_ad) + " damage")
      elif move == "4":
        movefour_h = randint(1,75)
        w_rookie_h = w_rookie_h - movefour_ad
        print("You do " + str(movefour_ad) + " damage")
      print(" ")
    elif w_type == 3:
      print(" ")
      print(" --------------------------------------------------------")
      print("|                      Move Set                          |")
      print("| -Move 1 : Basic Strike ( 25-50 )                       |")
      print("| -Move 2 : Sheild ( 1-25 )                              |")
      print("| -Move 3 : " + Colour.cyan + "Icy Blast " + Colour.reset + "( 10-65 )                          |" + Colour.reset)
      print("| -Move 3 : " + Colour.cyan + "Snowflake Breeze " + Colour.reset + "( 1-75 )                    |" + Colour.reset)
      print(" --------------------------------------------------------")
      move = input("Choose your move! (eg : 1)")
      if move == "1":
        moveone_ad = randint(25,50)
        w_rookie_h = w_rookie_h - moveone_ad
        print("You do " + str(moveone_ad) + " damage")
      elif move == "2":
        movetwo_ad = randint(1,25)
        w_rookie_ad = rookie_ad - movetwo_ad
        print("You save " + str(movetwo_ad) + " damage")
      elif move == "3":
        movethree_ad = randint(10,65)
        w_rookie_h = w_rookie_h - movethree_ad
        print("You do " + str(movethree_ad) + " damage")
      elif move == "4":
        movefour_ad = randint(1,75)
        w_rookie_h = w_rookie_h - movefour_ad
        print("You do " + str(movefour_ad) + " damage")
      print(" ")
    elif w_type == 4:
      print(" --------------------------------------------------------")
      print("|                      Move Set                          |")
      print("| -Move 1 : Basic Strike ( Wait 1 turn )                 |")
      print("| -Move 2 : Sheild ( Wait 2 turns )                      |")
      print("| -Move 3 : Air Slash ( Wait 2 turns )                   |")
      print("| -Move 4 : Hurricane ( Wait 4 turns )                   |")
      print(" --------------------------------------------------------")
      move = input("Choose your move! (eg : 1)")
      if move == "1":
        moveone_ad = randint(25,50)
        w_rookie_h = w_rookie_h - moveone_ad
        print("You do " + str(moveone_ad) + " damage")
      elif move == "2":
        movetwo_ad = randint(1,25)
        w_rookie_ad = rookie_ad - movetwo_ad
        print("You save " + str(movetwo_ad) + " damage")
      elif move == "3":
        movethree_ad = randint(10,65)
        w_rookie_h = w_rookie_h - movethree_ad
        print("You do " + str(movethree_ad) + " damage")
      elif move == "4":
        movefour_ad = randint(1,75)
        w_rookie_h = w_rookie_h - movefour_ad
        print("You do " + str(movefour_ad) + " damage")
      print(" ")
    elif w_type == 5:
      print(" ")
      print(" --------------------------------------------------------")
      print("|                      Move Set                          |")
      print("| -Move 1 : Basic Strike ( Wait 1 turn )                 |")
      print("| -Move 2 : Sheild ( Wait 2 turns )                      |")
      print("| -Move 3 : " + Colour.green + "Vine Whip " + Colour.reset + "( Wait 2 turns )                |" + Colour.reset)
      print("| -Move 4 : " + Colour.green + "Grass Trap " + Colour.reset + "( Wait 4 turns )               |" + Colour.reset)
      print(" --------------------------------------------------------")
      move = input("Choose your move! (eg : 1)")
      if move == "1":
        moveone_ad = randint(25,50)
        w_rookie_h = w_rookie_h - moveone_ad
        print("You do " + str(moveone_ad) + " damage")
      elif move == "2":
        movetwo_ad = randint(1,25)
        w_rookie_ad = rookie_ad - movetwo_ad
        print("You save " + str(movetwo_ad) + " damage")
      elif move == "3":
        movethree_ad = randint(10,65)
        w_rookie_h = w_rookie_h - movethree_ad
        print("You do " + str(movethree_ad) + " damage")
      elif move == "4":
        movefour_ad = randint(1,75)
        w_rookie_h = w_rookie_h - movefour_ad
        print("You do " + str(movefour_ad) + " damage")
      print(" ")
    elif w_type == 6:  
      print(" ")
      print(" --------------------------------------------------------")
      print("|                      Move Set                          |")
      print("| -Move 1 : Basic Strike ( Wait 1 turn )                 |")
      print("| -Move 2 : Sheild ( Wait 2 turns )                      |")
      print("| -Move 3 : " + Colour.magenta + "Sparkle Strike " + Colour.reset + "( Wait 2 turns )              |" + Colour.reset)
      print("| -Move 4 : " + Colour.magenta + "Charm Trap " + Colour.reset + "( Wait 4 turns )                  |" + Colour.reset)
      print(" --------------------------------------------------------")
      move = input("Choose your move! (eg : 1)")
      if move == "1":
        moveone_ad = randint(25,50)
        w_rookie_h = w_rookie_h - moveone_ad
        print("You do " + str(moveone_ad) + " damage")
      elif move == "2":
        movetwo_ad = randint(1,25)
        w_rookie_ad = rookie_ad - movetwo_ad
        print("You save " + str(movetwo_ad) + " damage")
      elif move == "3":
        movethree_ad = randint(10,65)
        w_rookie_h = w_rookie_h - movethree_ad
        print("You do " + str(movethree_ad) + " damage")
      elif move == "4":
        movefour_ad = randint(1,75)
        w_rookie_h = w_rookie_h - movefour_ad
        print("You do " + str(movefour_ad) + " damage")
      print(" ")
    elif w_type == 7:
      print(" --------------------------------------------------------")
      print("|                      Move Set                          |")
      print("| -Move 1 : Basic Strike ( Wait 1 turn )                 |")
      print("| -Move 2 : Sheild ( Wait 2 turns )                      |")
      print("| -Move 3 : " + Colour.yellow + "Volt Strike " + Colour.reset + "( Wait 2 turns )                  |" + Colour.reset)
      print("| -Move 4 : " + Colour.yellow + "Thunder Wave " + Colour.reset + "( Wait 4 turns )               |" + Colour.reset)
      print(" --------------------------------------------------------")
      move = input("Choose your move! (eg : 1)")
      if move == "1":
        moveone_ad = randint(25,50)
        w_rookie_h = w_rookie_h - moveone_ad
        print("You do " + str(moveone_ad) + " damage")
      elif move == "2":
        movetwo_ad = randint(1,25)
        w_rookie_ad = rookie_ad - movetwo_ad
        print("You save " + str(movetwo_ad) + " damage")
      elif move == "3":
        movethree_ad = randint(10,65)
        w_rookie_h = w_rookie_h - movethree_ad
        print("You do " + str(movethree_ad) + " damage")
      elif move == "4":
        movefour_ad = randint(1,75)
        w_rookie_h = w_rookie_h - movefour_ad
        print("You do " + str(movefour_ad) + " damage")
      print(" ")
    elif w_type == 8:
      print(" ")
      print(" --------------------------------------------------------")
      print("|                      Move Set                          |")
      print("| -Move 1 : Basic Strike ( Wait 1 turn )                 |")
      print("| -Move 2 : Sheild ( Wait 2 turns )                      |")
      print("| -Move 3 : Dark Strike ( Wait 2 turns )                 |")
      print("| -Move 4 : Black Hole ( Wait 4 turns )                  |")
      print(" --------------------------------------------------------")
      move = input("Choose your move! (eg : 1)")
      if move == "1":
        moveone_ad = randint(25,50)
        w_rookie_h = w_rookie_h - moveone_ad
        print("You do " + str(moveone_ad) + " damage")
      elif move == "2":
        movetwo_ad = randint(1,25)
        w_rookie_ad = rookie_ad - movetwo_ad
        print("You save " + str(movetwo_ad) + " damage")
      elif move == "3":
        movethree_ad = randint(10,65)
        w_rookie_h = w_rookie_h - movethree_ad
        print("You do " + str(movethree_ad) + " damage")
      elif move == "4":
        movefour_ad = randint(1,75)
        w_rookie_h = w_rookie_h - movefour_ad
        print("You do " + str(movefour_ad) + " damage")
      print(" ")
    elif w_type == 9:
      print(" ")
      print(" --------------------------------------------------------")
      print("|                      Move Set                          |")
      print("| -Move 1 : Basic Strike ( Wait 1 turn )                 |")
      print("| -Move 2 : Sheild ( Wait 2 turns )                      |")
      print("| -Move 3 : Sun Strike ( Wait 2 turns )                  |")
      print("| -Move 4 : Blinding Lights ( Wait 4 turns )             |")
      print(" --------------------------------------------------------")
      move = input("Choose your move! (eg : 1)")
      if move == "1":
        moveone_ad = randint(25,50)
        w_rookie_h = w_rookie_h - moveone_ad
        print("You do " + str(moveone_ad) + " damage")
      elif move == "2":
        movetwo_ad = randint(1,25)
        w_rookie_ad = rookie_ad - movetwo_ad
        print("You save " + str(movetwo_ad) + " damage")
      elif move == "3":
        movethree_ad = randint(10,65)
        w_rookie_h = w_rookie_h - movethree_ad
        print("You do " + str(movethree_ad) + " damage")
      elif move == "4":
        movefour_ad = randint(1,75)
        w_rookie_h = w_rookie_h - movefour_ad
        print("You do " + str(movefour_ad) + " damage")
      print(" ")
    else:
      print("hi :)")
      tpopcb = input("Whats you wizrd power")
      if tpopcb == "fire" or "ice" or "water":
        print("Have a good day")
      else:
        if tpopcb.isupper:
          print("Thats cool")
        elif tpopcb.islower:
          print(":(((((((")
  print(Colour.blue + "As you defeat Helga leader of the dark force i blinding light arises...")
  print("You see that light split into colourful circles that scattered quickly in differnt directions...")
  print("Bit by Bit magic was restored in the world...")
  print("You have Succeeded!!!" + Colour.reset)
  goto .menu
else:
  goto .menu