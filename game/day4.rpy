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

  image black = Solid("#000")

  image antonio normal = "images/antonio/normal.png"
  image mia normal = "images/mia/normal.png"
  image permione normal = "images/permione/normal.png"

define mc = Character("[player_name]")
define antonio = Character("Antonio")
define mia = Character("Mia")
define permione = Character("Permione")
define teacher = Character("Teacher")

label Day_4 :
  scene bg room
  play music "music/tracks/1_chill_pop.wav" volume 0.5
  show antonio normal
  antonio "\"hmmmm\""
  show antonio at right
  antonio "\"asdjkfp\""
  show antonio normal
  antonio "\"aSDfjP\""
  show antonio at left
  antonio "\"arhggg\""
  show antonio normal
  antonio """\"WhAT to DO! WHAT TO DO!!\"

  \"No no NOOOO\"

  \"This color scheme does NOT go well with my complexion...\"

  \"ahhhh...\"

  \"How about this!?!\""""
  mc "\"Uhh what are you doing Antonibro\""
  antonio """\"Ahhh [player_name]! Your awake!!\"

  \"What do you think looks best on me?\"

  \"Purple or Red!\"

  \"I don't know if I want to go for that POP POP colour purple\"

  \"Or the monochrome minimalistic red vibess\""""
  mc "\"ummm what is this for?\""
  antonio """\"My LOOK for tonight at the cricket club!!\"

  \"I have to look my FINESTT for my DATE\""""
  mc "\"OH NO!! I completly forgot to get something to wear!\""
  antonio """\"Yeah? You silly goose.\"

  \"Aren't you glad you have a bestie like me?\"

  \"You can take my Red SUIT! I think your Ladybug is going to LOVE the POP POP alphit ;)\""""
  mc "\"You are a lifesaver!\""
  mc "huh? Why cant I get up...."
  mc """\"OH MY BERRY!!\"

  \"DID YOU REALIZE IVE BEEN HANGING THE ENTIRE TIME??\""""
  antonio """\"Yes siree\"

  \"I thought you finally getting more comfortable\"

  \"Is that not your natural sleeping position??\""""
  mc "\"ANTONIO!! IM GREEN! AND HARD!\""
  antonio "\"ummm I dont swing that way but uhhh\""
  mc """\"NO!! what??\"

  \"IM GOING UNDER METAMORPHOSIS\"

  \"how am I going to go to the ball like this!!?\""""
  antonio "\"meta.. meta mofo sus??\""
  mc "..."
  mc "\"... Its my... special time\""
  antonio """\"STOP RIGHT THERE BOY!\"

  \"SAY NO MOREE!\"

  \"I will... I will remember you...\"

  \"you were the cutest fat ant I have ever met\"

  \"you were handsome like me but a bit too hairy\"

  \"but you were loyal, and fast and and....\"

  \"I WILL REMEMBER YOU!!!\""""
  mc "..."
  antonio "..."
  mc """\"No.. you slug brain!\"

  \"I'm cocooning... evolving!!\"

  \"WAIT!!\"

  \"YOU THOUGHT I WAS AN ANT?\""""
  antonio """\"...\"

  \"DONT SWEAT THE DETS\"

  \"YOU ARE MY BEST BUD\"

  \"AND NOTHINGS GOING TO CHANGE THAT\""""
  mc """\"...\"

  \"but.. what am I going to do?\""""

  #if Mia_points > Permione_points:
  #  mc "\"Will Mia even recognize me??\""
  #elif Permione_points >= Mia_points:
  #  mc "\"Will Permione even recognize me??\""

  mc """\"What if she doesn't like me anymore!\"

  \"uhh I think I have butterflies in my stomach\""""
  antonio """\"WELL ILL SNAP SOME SENSE INTO ER IF THATS THE CASE\"

  \"YOURE THE BEST DARN MAN ON THIS CAMPUS BESIDES ME!\"

  \"THERES NO WAY SHE WONT LIKE YA\"

  \"NOW GO GET CHANGED AND ILL GO GET HER!\""""
  hide antonio normal
  mc """\"WAIT!! I'm not even out of my cocoon yet...\"

  ...struggle...

  .....struggle...

  ...struggle...

  -pop-

  huh what are these colors?

  Im.. Im a butterfly??"""

  if Mia_points > Permione_points:
    show mia normal
    mia """\"[player_name]??\"

    \"YOU YOU....\"

    \"you are beautiful...\""""
    mc "\"... You are pretty too\""
    mia "..."
    mc "..."
    hide mia normal
    show antonio normal
    antonio "\"LETS GO LETS GO!!\""
    hide antonio normal
    scene bg college_outside
    play music "music/tracks/9_emotional_piano.wav" volume 0.5
    scene bg college_outside
    scene bg flower_bed
    scene bg other_dorm
    scene bg club_2
    show mia normal
    mia "\"Um [player_name]\""
    mc "..."
    mia "..."
    mc "\"yes?\""
    mia "\"Lets go home...\""
    mc "nod"

  elif Permione_points >= Mia_points:
    show permione normal
    permione """\"slurpp.. wow [player_name]\"

    \"you hot\"

    \"Come hereee\""""
    hide permione normal
    play music "music/tracks/7_emotional_piano.wav" volume 0.5
    scene bg college_outside
    scene bg tunnel
    scene bg track
    scene bg club_2
    show permione normal
    permione """\"COME HERE [player_name]\"
    
    \"over here.. OVER HERE!!!\""""
    mc "\"where are we going??\""
    permione "smooch smooch smooch"
    mc "smooch"
    permione "SMOOCH SMOOOCHHHH POP SMOOCH"
    mc "..."
    permione "\"tastyyyyy....\""
return
   