label Day_3:
  scene black
  play sound "music/sfx/human/snoring.mp3" volume 0.5

  "Zzz... ZZzz..."

  play sound "music/sfx/magic01/strange_bell.mp3" volume 0.5

  "!!!"

  play sound "music/sfx/human/walking_in_a_house1.mp3" volume 0.5
  scene bg room
  show antonio normal

  antonio "\"{b}Rise 'n shine, my boy{/b}!\""

  play music "music/tracks/7_emotional_piano.wav" volume 0.5

  if Choice == "Permione":
    antonio """
    \"You came back pretty late last night with Permione.\"

    \"I thought you might've been interested in Mia instead.\"
    """
  
  if Choice == "Mia":
    antonio """
    \"You came back pretty late last night with Mia.\"

    \"I thought you might've been interested in Permione instead.\"
    """
 
  antonio """
  \"Maybe you can decide who you want to take to the Cricket Club today at the track and field event!\"

  \"Oh! Don't forget that the ladybug fan club signed you up for the 100m sprint!\"

  \"There'll be some tough competition, but they don't stand a chance against you!\"
  """

  mc """
  \"Thanks...\"
  """

  if Choice == "Permione":
    "I can't remember much from last night after hanging out with Permione."
  if Choice == "Mia":
    "I can't remember much from last night after hanging out with Mia."
    
  """
  I wonder how I got back to my dorm.

  Best to focus on the sprint later today.

  I better start stretching if I'm going to stand a chance, with my soft lumps and juicy body.
  """

  hide antonio normal
  stop music
  show bg college_outside
  with fade
  #TODO add random bugs in to scene
  play music "music/tracks/1_chill_pop.wav" volume 0.5
  show ladybug normal at truecenter:
    zoom 0.5
    xzoom -1.0
    xalign 0.4
  show ladybug normal onlayer layer2 at truecenter:
    zoom 0.5
    xzoom -1.0
    xalign 0.4
    yalign 0.3
  show ladybug normal onlayer layer3 at truecenter:
    zoom 0.5
    xzoom -1.0
    xalign 0.55

  "The ladybug fan club hovers over you!"

  ladybugs """\"GoooOOOOOO [player_name!u]! You're the most handsomest bug on campus!\"

  \"You're going to kill the 100m sprint!\"

  \"We love you!\"

  \"We will be waiting for you at the finish line ❤️!\"

  \"HEHEHEHHE.\""""
  
  mc """\"Thanks ladies.\"
  
  \"I'll do my best!\"
  """

  """
  I wonder where Mia and Permione are.

  So many things are happening,
  
  How am I going to choose which one to ask to go to Cricket Club?
  
  Will they even want to go with me? 
  """

  play sound "music/sfx/human/whistling2.mp3"
  announcement """\"{i}{b}The hundred meter sprint is beginning soon!{/b}{/i}\"
  
  \"{i}{b}If you are participating, please make your way over to the track.{b}{/i}\""""
  stop sound
  hide ladybug normal 
  hide ladybug normal onlayer layer2
  hide ladybug normal onlayer layer3
  show antonio normal
  antonio """\"FOCUS UP [player_name!u]!\"

  \"We gotta get you to the race, or you'll be disqualified!\"

  \"Let's go!\""""
  hide antonio normal
  show bg track
  with fade
  show bugs normal

  "You arrive at the 100 meter sprint."

  mc """\"What the fuck is this?\"

  \"How do I compete with the hornet jocks, the bees... and a spider!?\""""

  show antonio normal
  antonio """\"Hmm. This is going to be a tough one! But if you don't believe {b}you don't succeed{/b}!\"

  \"They may be fast, but I'm sure you will pull through.\"

  \"Look! I see Mia and Permione over there.\"

  \"I'll go cheer you on with them!\"

  \"You got this!\""""
  hide antonio normal

  "Guess there's nothing to do but try..."

  announcer """\"{b}Welcome, welcome!{/b}\"

  \"{i}{b}This is the annual track meet! We will begin with a hundred meter sprint!{/b}{/i}\"

  \"{i}{b}We have got a greater variety of bugs in this race, than ever before!{/b}{/i}\"

  \"{i}{b}Are we ready racers?{/b}{/i}\"

  \"{i}{b}On!{/b}{/i}\"

  \"{i}{b}Your!{/b}{/i}\"

  \"{i}{b}Mark!{/b}{/i}\"

  \"{i}{b}GOOOOO!{/b}{/i}\""""

  hide bugs normal
  stop music
  play music "music/tracks/8_cinematic.wav" volume 1.2
  
  show mia normal at topright:
    zoom 0.5
  mia "\"GO [player_name!u]! YOU CAN DO IT!\""

  show permione normal at left:
    xzoom -1.0
  permione "\"YOU CAN DO IT SEXY! SHOW THEM WHAT YOU GOT!\""

  hide mia normal
  hide permione normal
  show bugs normal

  play sound "music/sfx/human/running_on_the_gravel.mp3" volume 0.25
  "I'm sweating profusely."
  
  play sound "music/sfx/human/running_on_the_gravel.mp3" volume 0.25
  "I'm already using 100\% of my power, and I'm... {b}dead last{/b}?!"
  
  play sound "music/sfx/human/running_on_the_gravel.mp3" volume 0.25
  "I have to keep going..."
  stop sound

  announcer """\"{i}{b}Homer the hornet jock is in the lead!{/b}{/i}\"

  \"{i}{b}Following close behind is Barry Bee!{/b}{/i}\"

  \"{i}{b}[player_name] is beginning to fall behind the rest of the competition!{/b}{/i}\""""
  
  voice("music/sfx/human/surprising_girl.mp3")
  announcer """

  \"{i}{b}What's this?{/b}{/i}\"

  \"{i}{b}It appears someone has dropped a slice of red velvet cake on the side of the tracks!{/b}{/i}\"

  \"{i}{b}Oh no!{/b}{/i}\"

  \"{i}{b}Homer the hornet has fallen for the delicious scent, and has completely gone off the tracks!{/b}{/i}\"

  \"{i}{b}No! Now the bees are falling for it as well!{/b}{/i}\""""

  hide bugs normal with moveoutright

  announcer """\"{i}{b}They must be tunnel visioning with how fast they're going!{/b}{/i}\"

  \"{i}{b}Even the spiders have now headed towards the cake!{/b}{/i}\"

  \"{i}{b}Wait, what's this?{/b}{/i}\"

  \"{i}{b}[player_name] has sprinted right past the velvet cake!{/b}{/i}\"

  \"{i}{b}He's headed towards the finish line!{/b}{/i}\"

  \"{i}{b}He has overtaken all his competition, and is about the finish the sprint!{/b}{/i}\""""

  show antonio normal
  antonio """\"RUN [player_name!u], RUN!\"

  \"LIKE YOUR LIFE DEPENDS ON IT!\"

  \"THIS IS YOUR TIME TO SHINE, BABY!\""""
  hide antonio normal
  
  play sound "music/sfx/human/running_on_the_gravel.mp3" volume 0.25
  mc "\"Ahh!\""
  stop sound

  announcer "\"{i}{b}Oh my god! [player_name] has finished in first place!{/b}{/i}\""

  stop music
  play music "music/tracks/10_emotional_piano.wav"
  play audio "music/sfx/human/clapping_alone1.mp3"
  play audio "music/sfx/human/clapping_alone2.mp3"
  play audio "music/sfx/human/clapping_alone3.mp3"

  show antonio normal at center:
    xalign 0.80
  antonio "\"You're bloody amazing!\""

  show mia normal at topright :
    zoom 0.5
    xalign 1.1
  mia "\"Oh my gosh! Woo!\""

  show permione normal at left:
    xzoom -1.0
    xalign -0.1
  permione "\"Yes baby, I knew you could do it!\""

  show ladybug normal at top:
    zoom 0.5
    xzoom -1.0
    xalign 0.4
  show ladybug normal onlayer layer2 at top:
    zoom 0.5
    xzoom -1.0
    xalign 0.5
    yalign 0.2
  show ladybug normal onlayer layer3 at top:
    zoom 0.5
    xzoom -1.0
    xalign 0.55
  
  ladybugs """\"[player_name!u]! [player_name!u]! [player_name!u]!\"

  \"WE KNEW YOU COULD DO IT!\"

  \"WE LOVE YOU!\"

  \"AHH!\""""

  mc """\"Oh my god! How did this happen?!\"

  \"I've never won anything before! This is insane!\""""

  permione """\"[player_name]! You were amazing! I knew if anyone could do it, you could!\"

  \"We {i}have{/i} to celebrate together 😉.\"

  \"Come watch my long jump event, and after we can go celebrate - just us.\""""

  mia """\"WAHHH! \*sniffles\* I'm so happy for you!\"

  \"Congratulations!\"

  \"I wish I was as good as you...\"

  \"I came dead last in my discus event... \*sniffles\*\""""

  hide ladybug normal 
  hide ladybug normal onlayer layer2
  hide ladybug normal onlayer layer3

  menu:
    "Who should I go with?"

    #TODO add in choice variable
    "Go to Permione's long jump event.":
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

  \"I hope I can win first place, just like you 😉.\""""

  mc """\"I'm sure you'll do great!\"

  \"You're Permione! You're always good at everything you do!\""""

  play sound "music/sfx/human/kiss1.mp3"
  permione "\"Make sure to keep you eyes on me 😘.\""
  stop sound

  announcer """\"{i}{b}Welcome to the long jump event!{/b}{/i}\"
  
  \"{i}{b}First up is Permione!{/b}{/i}\""""

  "..."

  stop music
  hide permione normal
  scene bg flower_bed
  with fade
  play music "music/tracks/9_emotional_piano.wav"
  show permione normal

  mc """\"Permione, you amaze me every time!\"

  \"I knew you were going to win first place!\""""

  permione """\"Thanks [player_name]!\"

  \"You're not so bad yourself, Mr. Hundred-Meter Sprint!\"

  \"I'm just glad you're celebrating with me, and not anyone else!\""""

  mc "\"Haha, well actually... I've been meaning to ask you something.\""
  
  play sound "music/sfx/human/heartbeats.mp3"
  mc """\"Do you want to go to the Cricket Club with me tomorrow,\"
  
  \"As my date?\""""
  stop sound

  play audio "music/sfx/magic01/chorus_of_angels1.mp3" volume 0.25

  permione """\"I thought you'd never ask!\"

  \"I'd LOVE to go with you!\""""

  hide permione normal
  scene black

  "..."

  return

label Day_3_Mia:
  stop music
  scene bg track
  with fade
  play music "music/tracks/1_chill_pop.wav"
  show mia normal at top:
    zoom 0.5

  play sound "/music/sfx/human/blowing_nose.mp3" volume 0.25
  mia "\*sniffles\*"
  stop sound

  mc """\"Oh Mia, I just got lucky!\"

  \"I was dead last until someone dropped that piece of cake.\"

  \"Who cares about track and field anyways!\"

  \"It doesn't define you!\"

  \"You tried your best and thats all that matters!\""""

  play sound "/music/sfx/human/catching_a_cold.mp3"
  mia "\*sniffles\*"
  stop sound

  mia """\"Thanks [player_name].\"

  \"Talking to you always makes me feel better.\""""

  mc "\"Let's go to the flower field to take your mind off of it.\""

  hide mia normal
  scene bg flower_bed
  with fade
  play music "music/tracks/9_emotional_piano.wav"
  show mia normal at top:
    zoom 0.5

  mia """\"You are so sweet for cheering me up by bringing me to the flower field.\"

  \"Thank you [player_name]!\""""

  mc """\"Anything for you Mia.\"
  
  \"I've actually been meaning to ask you something.\""""

  play sound "music/sfx/human/heartbeats.mp3"
  mc """\"Do you want to go to the Cricket Club with me tomorrow, \"
  
  \"As my date?\""""
  stop sound

  mia """\"And here I thought that you only saw me as a sister!\"

  \"I would love to go as your date!\""""

  play audio "music/sfx/magic01/chorus_of_angels1.mp3" volume 0.25

  mia "\"Hehe!\""

  hide mia normal
  scene black

  "..."

  return