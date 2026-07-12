define playerChar = Character("[player_name]")

define h = Character("Chloe Price")
define p = Character("Pharah")
define g = Character("Gyrados")
define a = Character("Applejack")
define v = Character("Vanilla Mace")
define e = Character("Everyone")

transform size_normal:
    ysize 800
    fit "contain"

# The game starts here.

label start:

    scene main_background
    $ player_name = renpy.input("Please enter your name:")

    "Hello, [player_name]!"
    show chloeprice at left, size_normal
    h "Welcome to Affection Village 20XX! You're the newest bombshell."
    h "I'm your host, Chloe."
    h "During your time here, you will meet other singles and form connections."
    h "Once you meet everyone, you can choose who to couple up with."
    h "While you are in your couple, you can get to know other Villagers."
    h "At the end of the game, there will be a recoupling. Whether or not you win will depend on your compatability with your current couple."
    h "Without further ado, let's meet our fellow Villagers!"

    show applejack at center, size_normal
    a "Howdy everypony!"

    hide applejack
    show vanilla at center, size_normal 
    v "Hiiiiiiiiiiiii.... Emily.... Nice to meet you......"
    hide vanilla

    show gyarados at center, size_normal
    g "'Ello, I am pleased to make your acquaintance."
    hide gyarados 

    show pharah at center, size_normal
    p "Pharah. Group up with me!"
    hide chloeprice

    menu:
      "Now, pick who you want to talk to first."
      "Gyrados":
          scene pool
          show gyarados at center, size_normal
          g "Nice to see you again, beautiful."
          g "... Am I in a couple..?"
          g "I mean.. kinda? It's exclusive but there's no label on it right now."
          g "But nevermind that.. I'd be pretty interested in getting to know you, [player_name]"
          g "..."
          g "........"
          g "You're a great listener..."

      "Applejack":
          scene gym
          show applejack_sad at center, size_normal
          a "... sigh...."
          a "Oh!! I didn't see you there, [player_name]..."
          a "It's awful nice of you to be interested in talking to me... but..."
          a "I'm thinking about my old connection... she got voted out last night..."
          show twi at left, size_normal
          a "The Lord giveth.. and the Lord taketh away..."
          hide twi

      "Vanilla Mace":
          scene dressingroom
          show vanilla at center, size_normal
          v "Oh... heyyyy....."
          v "Ummm.... my name is Emily...."
          v "Oh... I already told you that..."
          v "My job..? I'm a Meowtch streamer..."
          v "I have a connection with Gyrados... but we might not work out...."
          v "He hates my feline familiars... Miso and Chai...."
          v "... Oh you like cats..? Heh.. c-cool..."
          hide vanilla

      "Pharah":
          scene main_background
          show pharah at center, size_normal
          p "... My ultimate is almost ready."
          p "Let's defend as one."
          p "I will fight by your side!"
          p "..."
          p "... My ultimate is ready! Let's work together."
          hide pharah

  
    scene firepit
    show chloeprice at center, size_normal
    h "Hello Villagers!"
    hide chloeprice
    show applejack at center, size_normal
    show pharah at left, size_normal
    show gyarados at right, size_normal
    e "GASP"
    hide applejack
    hide pharah
    hide gyarados
    h "Tonight, there will be a recoupling."
    h "[player_name], please choose who you want to couple up with."
 
    menu:
      "Gyrados":
         show gyarados
         h "Verica has voted..."
         "Bad Ending."
      "Applejack":
         show applejack
         h "Verica has voted..."
         "Neutral Ending"

      "Vanilla Mace":
         show vanilla
         h "Verica has voted..."
         "You win 100 million dollars!"
      "Pharah":
         show pharah
         h "Verica has voted..."
         "You win 100 million dollars!"
  
    return

