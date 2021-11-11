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

  return
