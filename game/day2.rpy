init:
  image bg room = "images/backgrounds/bg_bedroom.png"
  image bg classroom = "images/backgrounds/bg_classroom.png"
  image bg club = "images/backgrounds/bg_club.png"
  image bg club_2 = "images/backgrounds/bg_club_2.png"
  image bg college_outside = "images/backgrounds/bg_college_outside.png"
  image bg flower_bed = "images/backgrounds/bg_flower_bed.png"
  image bg other_dorm = "images/backgrounds/bg_other_dorm.png"
  image bg track = "images/backgrounds/bg_track.png"
  image bg tunnel = "images/backgrounds/bg_tunnel.jpg"

  image antonio normal = "images/antonio/normal.png"
  image mia normal = "images/mia/normal.png"
  image permione normal = "images/permione/normal.png"

define mc = Character("[player_name]")
define antonio = Character("Antonio")
define mia = Character("Mia")
define permione = Character("Permione")
define teacher = Character("Teacher")

label start:

  play music "music/tracks/1_chill_pop.wav" volume 0.5
  scene bg room
  show antonio normal

  $ player_name = renpy.input("What is your name, Magical Boy?")
  $ player_name = player_name.strip()

  if not player_name:
    $ player_name = "Brother of Mia"

  mc "I'm [player_name]!"
  antonio "I'm an ant!"

  hide antonio normal
  show mia normal

  mia "I'm a moth and one of the main love interests!"

  hide mia normal
  show permione normal

  permione "I'm a praying mantis and another of the main love interests!"

  scene bg classroom

  mc "I'm in a classroom? WOAH"

  scene bg club

  mc "I'm in a club?! Wow!"

  scene bg club_2

  mc "I'm in a club again!? Sheeesh."

  scene bg college_outside

  mc "I'm outside of my college."

  scene bg flower_bed

  mc "I hope I don't see any sexy plants here."

  scene bg other_dorm

  mc "I sure hope not to see any other bugs in this other dorm."

  scene bg track

  mc "Wow! I am so good at track and field."

  scene bg tunnel

  mc "This is a very scary tunnel."

  jump Day_2

  return

label Day_2 :
  scene bg room
  show antonio normal
  antonio "\"92, 93, 94!\""
  hide antonio normal
  image black = Solid("#000")
  scene black
  mc "..."
  scene bg room
  show antonio normal
  antonio "\"95, 96, 97!\""
  hide antonio normal
  scene black
  mc "..."
  scene bg room
  show antonio normal
  antonio "\"98, 99, 100!\""
  mc "\"Zzzz... huh?\""
  mc "I am so dizzy, how did I make it back to the dorm..."
  antonio "\"98, 99, 100!\""
  antonio "\"Oh you're awake!\""
  antonio "\"YOU were OUT COLD! I almost thought I lost you.\""
  antonio "\"You got all your limbs? ... Damn all 16? You'd do fine without a few\""
  antonio "\"I remember fighting alongside 4 armed Jack, Antman and Bent leg Billy\""
  antonio "\"BATTLE SCARS IS WHAT MAKES YOU A MAN!!!\""
  mc "\"What... happened yesterday?\""
  antonio "\"Who knows? Did you fight someone mano-a-mano?\""
  antonio "\"I just saw you  laying there twitching on my 10km run\""
  antonio "\"So I thought... Extra weight training!!!\""
  mc "\"... Thanks\""

  define Mia_points = 1
  define Permione_points = 2

  if Mia_points > Permione_points:
    mc "I hope Mia see me on his back..."
    mc "So embarassing...."
  elif Permione_points >= Mia_points:
    mc "I hope Mia see me on his back..."
    mc "So embarassing...."

  antonio "\"Boy! You better sober up!\""
  antonio "\"There's a worse war incoming today!!!\""
  mc "\"WAR??\""
  antonio "\"Yea!! I hear even if you train everyday barely anyone can make it through without a head injury\""
  antonio "\"Brace yourself...\""
  antonio "\"...\""
  antonio "\"....\""
  antonio "\"...\""
  antonio "\"It's the written exam!\""
  mc "..."
  antonio "..."
  antonio "..."
  antonio "\"Don't be scared brother! I got your back!\""
  antonio "\"Psht.. Inside tip...\""
  antonio "\"I hear they come wave after wave...\""
  antonio "\"BUT.. if you hold on long enough\""
  antonio "\"You will hear a bell\""
  antonio "\"and then it'll all be over!!\""
  mc "..."
  mc "\"Lets... go get breakfast\""
  antonio "\"That's the spirit!\""
  antonio "\"We need ALL THE CARBS to bulk up!\""
  antonio "\"CHARGEEE!!!\""
  hide antonio normal
  mc "..."
  mc "..."
  scene bg college_outside
  scene bg classroom
  play music "music/tracks/3_acoustic_pop.wav" volume 0.5
  mc "oh, There is Mia... and Permione."
  play music "music/sfx/human/heartbeats.mp3" volume 0.5
  mc "should I go say hi?"
  play music "music/tracks/3_acoustic_pop.wav" volume 0.5
  show mia normal
  mia "\"What do you mean you never asked me to!!\""
  mia "\"You always say you will clean up afterwards\""
  mia "\"and then NEVER DO!\""
  mia "\"SO I go and spend all night cleaning\""
  mia "\"AND ALL YOU CAN SAY IS Don’t touch my stuff?\""
  hide mia normal
  show permione normal
  permione "\"Girl, you do you.\""
  permione "\"Don’t come crying to me when you pick up the wrong magazine… and...\""
  permione "\"Oh is that what it is, couldn’t sleep well last night?\""
  permione "\"Did little mothy girl have too much to think about. ;)\""
  mia "\"YOU!!!\""
  permione "\"Haha, how bout this\""
  permione "\"we make a bet with the test today...\""
  permione "\"and whoever wins listens to the other!\""
  hide permione normal
  show mia normal
  mia "\"DEAL!!!\""
  mia "\"You are goint to lose FOR SURE!\""
  mia "\"I was top of the class!\""
  mia "\"you are going DOWN!\""
  play music "music/sfx/human/man_coughing.mp3" volume 0.5
  mc "\"um.. Good morning?\""
  play music "music/tracks/3_acoustic_pop.wav" volume 0.5
  mia "\"AHHH!\""
  hide mia normal
  mc "..."
  show permione normal
  permione "\"Morning [player_name] \""
  permione "\"Looking fine... tasty...\""
  mc "..."
  hide permione normal
  play music "music/sfx/daily/door_chime3.mp3" volume 0.5
  teacher "\"OKAY CLASS FIND A SEAT AND WE WILL BEGIN\""

  menu:
    "Where should I sit?"
    "Sit with Permione.":
      $ Choice = "Permione"
      $ Permione_points += 1
    "Go find Mia and sit with her.":
      $ Choice = "Mia"
      $ Mia_points += 1

  if Choice == "Permione":
    show permione normal
    permione "\"Good luck!\""
    permione "\"I’ll bring you somewhere spicy when we are done.\""
    mc "..."
    hide permione normal
    scene black
    play music "music/sfx/daily/door_chime3.mp3" volume 0.5
    antonio "\"IM FREE\""
    scene bg college_outside
    show permione normal
    permione "\"Quick! Follow me!\""
    hide permione normal
    mc "\" Wait for me!\""
    scene bg tunnel
    play music "music/sfx/magic01/in_a_cave.mp3" volume 0.5
    mc"\"Pe.. permione??\""
    show permione normal
    permione "\"BOO!!\""
    permione "\"haha, look at your face\""
    permione "\"Over here!!\""
    hide permione normal
    mc "Wow, that's a very hidden entrance"
    scene black
    play music "music/tracks/2_chill_beats.wav" volume 0.2
    mc "I wonder where we are going..."
    play music "music/tracks/2_chill_beats.wav" volume 0.5
    scene bg club
    show permione normal
    permione "\"loosen up!, it's not every day DJ CiciDada is here!\""
    play music "music/tracks/2_chill_beats.wav" volume 0.8
    hide permione normal
    scene black
  if Choice == "Mia":
    show mia normal
    mc "\"oh uh... good morning Mia\""
    mia "\"Good luck!\""
  return