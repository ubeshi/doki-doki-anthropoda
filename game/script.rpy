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

  def announcer_voice(event, interact=True, **kwargs):
    if not interact:
      return 
    if event == "begin":
      renpy.sound.play("music/sfx/human/hiccup.mp3", relative_volume = 0.25) 
    elif event == "end":
      renpy.sound.stop()

define mc = Character("[player_name]")
define antonio = Character("Antonio", callback = antonio_voice)
define mia = Character("Mia", callback = mia_voice)
define permione = Character("Permione", callback = permione_voice)
define ladybugs = Character("Ladybug Fan Club")
define announcement = Character("Announcement")
define announcer = Character ("Announcer", callback = announcer_voice)

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
  antonio """\"You came back pretty late last night with…(insert yesterdays choice)\"

  \"I thought you mightve been interested in (insert other choice name) instead…\"
  
  \"Maybe you can decide who you want to take to the cricket club today at the track and field event!\"

  \"OH! Don’t forget that the ladybug fan club signed you up for the 100m sprint!\"

  \"There’ll be some tough competition but they dont stand a chance against you!!\""""

  mc """\"Thanks...\"

  I can’t remember much from last night after listening to music with (insert yesterdays choice)...

  I wonder how I got back to my dorm….

  Best to focus on the sprint later today,

  I better start stretching if I'm going to stand a chance with my soft lumps and juicy body."""

  hide antonio normal
  stop music
  
  show bg college_outside
  with fade
  #TODO add random bugs in to scene
  play music "music/tracks/1_chill_pop.wav" volume 0.5
  voice "music/sfx/human/girl_voice1.mp3"

  "The ladybug fan club hovers over you!!"

  ladybugs """\"goooOOOOOO [player_name]!!! You're the most handsomest bug on campus!\"

  \"You're going to kill the 100m Sprint!\"

  \"WE LOVE YOU\"

  \"WE WILL BE WAITING FOR YOU AT THE FINISH LINE <3\"

  \"HEHEHEHHE\""""
  
  mc """\"Thanks ladies...\"
  
  \"I'll do my best\"
  
  I wonder where Moth and Mantis are…

  So many things are happening
  
  How am I going to choose which one to ask to go to cricket club…
  
  Will they even want to go with me? 
  
  …"""

  announcement """ \"THE 100M SPRINT IS BEGINNING SOON…\"
  
    \"IF YOU ARE PARTICIPATING, PLEASE MAKE YOUR WAY OVER TO THE TRACK\""""

  show antonio normal

  antonio """\"FOCUS UP [player_name]!\"

  \"WE GOTTA GET YOU TO THE RACE OR YOU'LL BE DISQUALIFIED!\"

  \"LETS GOO\""""

  hide antonio normal

  show bg track
  with fade

  "You arrive at the 100 metre sprint."

  mc """\"What the fuck is this\"

  \"How do I compete with the hornet jocks, the bees, and a spider!!??\""""

  show antonio normal

  antonio """\"HMM…THIS IS GOING TO BE  A TOUGH ONE BUT IF YOU DONT BELIEVE YOU DONT SUCCEEED\"

  \"They may be fast but I’m sure you will pull through\"

  \"Look! I see Moth and Mantis over there\"

  \"I’ll go cheer you on with them\"

  \"YOU GOT THIS\""""

  hide antonio normal

  mc "Guess theres nothing to do but try..."

  announcer """\"WELCOME WELCOME\"

  \"THIS IS THE ANNUAL TRACK MEET AND WE BEGIN WITH A 100M SPRINT\"

  \"WE HAVE GOT THE GREATEST VARIETY OF BUGS IN THIS RACE THAN EVER BEFORE\"

  \"ARE WE READY RACERS?\"

  \"ON\"

  \"YOUR\"

  \"MARKS\"

  \"GOOOOO!!!!\""""

  stop music
  play music "music/tracks/8_cinematic.wav" volume 0.5

  show mia normal
  mia "\"GO [player_name]! YOU CAN DO IT\""

  show permion normal
  permione "\"YOU CAN DO IT SEXY! SHOW THEM WHAT YOU GOT!\""

  mc """\*sweats profusely\*
  
  I’m already using 100\% and im…..DEADLAST?!?!

  I have to keep going…"""

  announcer """\"HOMER THE HORNET JOCK IS IN THE LEAD\"

  \"FOLLOWING CLOSE BEHIND IS BARRY BEE\"

  \"[player_name] IS BEGINNING TO FALL BEHIND THE REST OF THE COMPETITION!!\"
  
  …!!!

  \"WHATS THIS??\"

  \"IT APPEARS SOMEONE HAS DROPPED A SLICE OF RED VELVET CAKE ON THE SIDE OF THE TRACK\"

  \"OH NO!!\"

  \"HOMER THE HORNET HAS FALLEN FOR THE DELICIOUS SCENT AND HAS COMPLETELY GONE OFF THE TRACKS\"

  \"NO NONO !!! THE BEES ARE FOLLOWING\"

  \"THEY MUST BE TUNNEL VISIONING WITH HOW FAST THEYRE GOING\"

  \"EVEN THE SPIDERS HAVE NOW HEADED TOWARDS THE CAKE\"

  \"WHATS THIS….?!?!!\"

  \"MC HAS SPRINTED RIGHT PAST THE VELVET CAKE \"

  \"HES HEADED TOWARDS THE FINISH LINE\"

  \"HE HAS OVERTAKEN ALL HIS COMPETITION AND IS ABOUT TO FINISH THE SPRINT\""""

  antonio """\"RUN MC RUN!!!!\"

  \"LIKE YOUR LIFE DEPENDS ON IT!!!\"

  \"THIS IS YOUR TIME TO SHINE BABY!\""""
  
  mc "\"AHHHHH!!!!\""

  show antonio normal
  antonio "\"YOU'RE BLOODY AMAZING!\""

  show mia normal
  mia "\"OH MY GOSH!!! WOOO!\""

  show permion normal
  permione "\"YES BABY I KNEW YOU COULD DO IT!\""

  ladybug """\"[player_name]! [player_name]! [player_name]!\"

  \"WE KNEW YOU COULD DO IT!\"

  \"WE LOVE YOU!!!\"

  \"AHHHH!\""""

  mc """\"OH MY GOD! How did this happen?!?!\"

  \"I’ve never won anything before this is insane!\""""

  permione  """\"[player_name]! You were amazing! I knew if anyone could do it you could!!!\"

  \"We HAVE to celebrate together ;)\"

  \"Come watch my long jump event and after we can go celebrate just us?\""""

  mia """\"WAHHHHHHH \*sniffles\* Im so happy for you! \"

  \"Congratulations!\"

  \"I wish I was as good as you…\"

  \"I came dead last in my discus event.. \*sniffles\*\""""

  


  return