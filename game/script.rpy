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

  image black = Solid("#000")

init python:
  def antonio_voice(event, interact=True, **kwargs):
    if not interact:
      return 
    if event == "begin":
      renpy.sound.play("music/sfx/human/man_gargle1.mp3", relative_volume = 0.25) 
    elif event == "end":
      renpy.sound.stop()

  def mia_voice(event, interact=True, **kwargs):
    if not interact:
      return 
    if event == "begin":
      renpy.sound.play("music/sfx/magic01/magic_elevator.mp3", relative_volume = 0.10) 
    elif event == "end":
      renpy.sound.stop()

  def permione_voice(event, interact=True, **kwargs):
    if not interact:
      return 
    if event == "begin":
      renpy.sound.play("music/sfx/human/woman_gargle.mp3", relative_volume = 0.25) 
    elif event == "end":
      renpy.sound.stop()


define mc = Character("[player_name]")
define antonio = Character("Antonio", callback = antonio_voice)
define mia = Character("Mia", callback = mia_voice)
define permione = Character("Permione", callback = permione_voice)


label start:

  play music "music/tracks/1_chill_pop.wav" volume 0.5
  scene bg room
  show antonio normal

  $ player_name = renpy.input("What is your name, Magical Boy?")
  $ player_name = player_name.strip()

  #if not player_name:
  #  $ player_name = "Brother of Mia"

  #mc "I'm [player_name]!"
  #antonio "I'm an ant!"

  #hide antonio normal
  #show mia normal

  #mia "I'm a moth and one of the main love interests!"
  
  #hide mia normal
  #show permione normal

  #permione "I'm a praying mantis and another of the main love interests!"

  #scene bg classroom

  #mc "I'm in a classroom? WOAH"

  #scene bg club 

  #mc "I'm in a club?! Wow!"

  #scene bg club_2

  #mc "I'm in a club again!? Sheeesh."

  #scene bg college_outside 

  #mc "I'm outside of my college."

  #scene bg flower_bed

  #mc "I hope I don't see any sexy plants here."

  #scene bg other_dorm

  #mc "I sure hope not to see any other bugs in this other dorm."

  #scene bg track

  #mc "Wow! I am so good at track and field."

  #scene bg tunnel 

  #mc "This is a very scary tunnel."

  hide antonio normal
  
  #return

label Day_3:
  scene black
  play music "music/sfx/human/snoring.mp3" volume 0.5
  
  mc "Zzzz....ZZzzz...."

  play music "music/sfx/magic01/strange_bell.mp3" volume 0.5

  mc "!!!"
  
  play music "music/sfx/human/walking_in_a_house1.mp3" volume 0.5
  scene bg room
  show antonio normal

  antonio "\"RISE N SHINE MY BOY!\""
  
  stop music
  play music "music/tracks/7_emotional_piano.wav" volume 0.5

  #TODO add in choice names
  antonio "\"You came back pretty late last night with…(insert yesterdays choice)\n
  I thought you mightve been interested in (insert other choice name) instead…\""
  
  antonio "\"Maybe you can decide who you want to take to the cricket club today at the track and field event!\n
  OH! Don’t forget that the ladybug fan club signed you up for the 100m sprint!\n
  There’ll be some tough competition but they dont stand a chance against you!!\""

  mc "\"Thanks...\""

  mc "I can’t remember much from last night after listening to music with (insert yesterdays choice)...\n
  I wonder how I got back to my dorm…."

  mc "Best to focus on the sprint later today,\n
  I better start stretching if I'm going to stand a chance with my soft lumps and juicy body."

  mia "testing"

  permione "testing"

  hide antonio normal
  stop music
  
  show bg track
  with fade

  

  
  
  
  return