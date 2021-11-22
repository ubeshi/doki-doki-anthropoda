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
      renpy.sound.play("music/sfx/magic01/unknown_animal2.mp3", relative_volume = 0.20) 
    elif event == "end":
      renpy.sound.stop()

  def permione_voice(event, interact=True, **kwargs):
    if not interact:
      return 
    if event == "begin":
      renpy.sound.play("music/sfx/human/woman_gargle.mp3", relative_volume = 0.25) 
    elif event == "end":
      renpy.sound.stop()

  def ladybugs_voice(event, interact=True, **kwargs):
    if not interact:
      return 
    if event == "begin":
      renpy.sound.play("music/sfx/human/girl_voice1.mp3", relative_volume = 0.25) 
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
define ladybugs = Character("Ladybug Fan Club", callback = ladybugs_voice)
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

  "The ladybug fan club hovers over you!!"

  ladybugs """\"goooOOOOOO [player_name]!!! You're the most handsomest bug on campus!\"

  \"You're going to kill the 100m Sprint!\"

  \"WE LOVE YOU\"

  \"WE WILL BE WAITING FOR YOU AT THE FINISH LINE <3\"

  \"HEHEHEHHE\""""
  
  mc """\"Thanks ladies...\"
  
  \"I'll do my best\"
  
  I wonder where Mia and Permione are…

  So many things are happening
  
  How am I going to choose which one to ask to go to cricket club…
  
  Will they even want to go with me? 
  
  …"""

  play sound "music/sfx/human/whistling2.mp3"
  announcement """ \"THE 100M SPRINT IS BEGINNING SOON…\"
  
  \"IF YOU ARE PARTICIPATING, PLEASE MAKE YOUR WAY OVER TO THE TRACK\""""
  stop sound

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

  \"Look! I see Mia and Permione over there\"

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
  play music "music/tracks/8_cinematic.wav" volume 1.2
  
  show mia normal at topright:
    zoom 0.5
  mia "\"GO [player_name]! YOU CAN DO IT\""

  show permione normal at left:
    xzoom -1.0
  permione "\"YOU CAN DO IT SEXY! SHOW THEM WHAT YOU GOT!\""

  hide mia normal
  hide permione normal

  play sound "music/sfx/human/running_on_the_gravel.mp3" volume 0.25
  mc "\*sweats profusely\*"
  
  play sound "music/sfx/human/running_on_the_gravel.mp3" volume 0.25
  mc "I’m already using 100\% of my power and I'm…..DEADLAST?!?!"
  
  play sound "music/sfx/human/running_on_the_gravel.mp3" volume 0.25
  mc "I have to keep going…"
  stop sound

  announcer """\"HOMER THE HORNET JOCK IS IN THE LEAD\"

  \"FOLLOWING CLOSE BEHIND IS BARRY BEE\"

  \"[player_name] IS BEGINNING TO FALL BEHIND THE REST OF THE COMPETITION!!\""""
  
  voice("music/sfx/human/surprising_girl.mp3")
  announcer """…!!!

  \"WHATS THIS??\"

  \"IT APPEARS SOMEONE HAS DROPPED A SLICE OF RED VELVET CAKE ON THE SIDE OF THE TRACK\"

  \"OH NO!!\"

  \"HOMER THE HORNET HAS FALLEN FOR THE DELICIOUS SCENT AND HAS COMPLETELY GONE OFF THE TRACKS\"

  \"NO NONO !!! THE BEES ARE FOLLOWING\"

  \"THEY MUST BE TUNNEL VISIONING WITH HOW FAST THEYRE GOING\"

  \"EVEN THE SPIDERS HAVE NOW HEADED TOWARDS THE CAKE\"

  \"WHATS THIS….?!?!!\"

  \"[player_name] HAS SPRINTED RIGHT PAST THE VELVET CAKE \"

  \"HES HEADED TOWARDS THE FINISH LINE\"

  \"HE HAS OVERTAKEN ALL HIS COMPETITION AND IS ABOUT TO FINISH THE SPRINT\""""

  show antonio normal
  antonio """\"RUN [player_name] RUN!!!!\"

  \"LIKE YOUR LIFE DEPENDS ON IT!!!\"

  \"THIS IS YOUR TIME TO SHINE BABY!\""""
  hide antonio normal
  
  play sound "music/sfx/human/running_on_the_gravel.mp3" volume 0.25
  mc "\"AHHHHH!!!!\""
  stop sound

  announcer "\"OH MY GOD!!! [player_name] HAS FINISHED IN FIRST PLACE!!!!!!\""

  stop music
  play music "music/tracks/10_emotional_piano.wav"
  play audio "music/sfx/human/clapping_alone1.mp3"
  play audio "music/sfx/human/clapping_alone2.mp3"
  play audio "music/sfx/human/clapping_alone3.mp3"

  show antonio normal at center:
    xalign 0.80
  antonio "\"YOU'RE BLOODY AMAZING!\""

  show mia normal at topright :
    zoom 0.5
    xalign 1.1
  mia "\"OH MY GOSH!!! WOOO!\""

  show permione normal at left:
    xzoom -1.0
    xalign -0.1
  permione "\"YES BABY I KNEW YOU COULD DO IT!\""

  ladybugs """\"[player_name]! [player_name]! [player_name]!\"

  \"WE KNEW YOU COULD DO IT!\"

  \"WE LOVE YOU!!!\"

  \"AHHHH!\""""

  mc """\"OH MY GOD! How did this happen?!?!\"

  \"I’ve never won anything before this is insane!\""""

  permione """\"[player_name]! You were amazing! I knew if anyone could do it you could!!!\"

  \"We HAVE to celebrate together ;)\"

  \"Come watch my long jump event and after we can go celebrate just us?\""""

  mia """\"WAHHHHHHH \*sniffles\* Im so happy for you! \"

  \"Congratulations!\"

  \"I wish I was as good as you…\"

  \"I came dead last in my discus event.. \*sniffles\*\""""

  menu:
    "Who should I go with?"

    #TODO add in choice variable
    "Go to Permione's Long Jump Event.":
      mc """\"I'd love to watch your event Permione!\"

      Thanks Mia, I'll catch you later!\""""

      jump Day_3_Permione

    #TODO add in choice variable
    "Comfort Mia.":
      mc """\"Oh no Mia!\"
      
      \"I'll catch up with you later Permione. Good luck at your event!\""""
      jump Day_3_Mia
  
  return

label Day_3_Permione:
  stop music
  scene bg track
  with fade
  play music "music/tracks/1_chill_pop.wav"
  show permione normal

  permione """\"I'm so glad to have you cheering for me at my event!\"

  \"I hope I can win first place just like you \:\)\""""

  mc """\"I'm sure you'll do great!\"

  \"You're Permione! You're always good at everything you do!\""""

  play sound "music/sfx/human/kiss1.mp3"
  permione "\"Make sure to keep you eyes on me \;\)\""
  stop sound

  announcer """\"WELCOME TO THE LONG JUMP EVENT!!\"
  
  \"FIRST UP IS PERMIONE...\""""

  stop music
  hide permione normal
  scene bg flower_bed
  with fade
  play music "music/tracks/9_emotional_piano.wav"
  show permione normal

  mc """\"Permione, you amaze me every time!\"

  \"I knew you were going to win 1st place!\""""

  permione """\"Thanks [player_name]!\"

  \"You’re not so bad yourself Mr.100m sprint!\"

  \"I’m just glad you're celebrating with me and not anyone else!\""""

  mc "\"Ahaha well actually I’ve been meaning to ask you something…\""
  
  play sound "music/sfx/human/heartbeats.mp3"
  mc """\"Do you want to go to the cricket club with me tomorrow…\"
  
  \"as my date?\""""
  stop sound

  permione """\"I thought you'd never ask!\"

  \"I'd LOVE to go with you!\""""

  play audio "music/sfx/magic01/chorus_of_angels1.mp3" volume 0.25
  
  #TODO check if day 4 is called Day_4
  jump Day_4
  return

label Day_3_Mia:
  stop music
  scene bg track
  with fade
  play music "music/tracks/1_chill_pop.wav"
  show mia normal at top:
    zoom 0.5

  play sound "/music/sfx/human/blowing_nose.mp3"
  mia "\*sniffles\*"
  stop sound

  mc """\"Oh Mia I just got lucky!\"

  \"I was dead last until someone dropped that piece of cake!\"

  \"Who cares about Track and Field anyways!\"

  \"It doesn't define you!\"

  \"You tried your best and thats all that matters!\""""

  play sound "/music/sfx/human/catching_a_cold.mp3"
  mia "\*sniffles\*"
  stop sound

  mia """\"Youre right!\"

  \"Talking to you always makes me feel better!\""""

  mc "\"Lets go to the flower field to take your mind off of it!\""

  hide mia normal
  scene bg flower_bed
  with fade
  play music "music/tracks/9_emotional_piano.wav"
  show mia normal at top:
    zoom 0.5

  mia """\"You are so sweet for cheering me up by bringing me to the flower field...\"

  \"Thank you [player_name]!\""""

  mc """\"Anything for you Mia…\"
  
  \"I’ve actually been meaning to ask you something…\""""

  play sound "music/sfx/human/heartbeats.mp3"
  mc """\"Do you want to go to the cricket club with me tomorrow… \"
  
  \"as my date?\""""
  stop sound

  mia """\"Here I thought that you only saw me as a sister!\"

  \"I would love to go as your date!\""""

  play audio "music/sfx/magic01/chorus_of_angels1.mp3" volume 0.25

  mia "\"Hehe!\""

  jump Day_4
  return