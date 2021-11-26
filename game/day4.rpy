label Day_4 :
  scene bg room
  play music "music/tracks/1_chill_pop.wav" volume 0.5
  show antonio normal
  antonio "\"Hmmmm...\""
  show antonio at right
  antonio "\"Asdjkfpnaoidsnadaidoasdisaodniasodnasdas...\""
  show antonio normal
  antonio "\"Masfawionqmooqpmdaasnopfasksdoapasodk...\""
  show antonio at left
  antonio "\"Arhggg...\""
  show antonio normal
  antonio """\"What to do? What to do!\"

  \"No, no, no!\"

  \"This color scheme does {b}not{/b} go well with my complexion.\"

  \"Ahhhh...\"

  \"How about this!\"
  """
  mc "\"Uh, what are you doing Antonibro?\""
  antonio """\"Ah [player_name]! You're awake!\"

  \"What do you think looks best on me?\"

  \"Purple or red?\"

  \"I don't know if I want to go for that {i}pop pop{/i} purple.\"

  \"Or the monochrome minimalistic red vibes...\""""
  mc "\"What is this for?\""
  antonio """
  \"My look for tonight at the Cricket Club!\"

  \"I have to look my {i}finest{/i} for my date!\"
  """
  mc "\"Oh no! I completly forgot to get something to wear!\""
  antonio """\"Yeah? You silly goose.\"

  \"Aren't you glad you have a bestie like me?\"

  \"You can take my red suit! I think your ladybug is going to {i}love{/i} the alphit.\""""
  mc "\"You are a lifesaver!\""
  
  "Huh? Why can't I get up?"

  mc """
  \"Oh my berry!\"

  \"Did you realize, I've been hanging the entire time?!\"
  """
  antonio """\"Yes siree!\"

  \"I thought you finally getting more comfortable.\"

  \"Is that not your natural sleeping position?\""""
  mc "\"Antonio! I'm green! And hard!\""
  antonio "\"Hey! That's a DLC scene!\""
  mc """\"No! I mean...\"

  \"I'm going under {b}metamorphosis{/b}!\"

  \"How am I going to go to the ball like this?\""""
  antonio "\"Meta... Meta mofo sus?\""
  
  "..."

  mc "\"It's my... special time...\""
  antonio """\"{b}Stop right there, boy{/b}!\"

  \"Say no more!\"

  \"I will... I will remember you...\"

  \"You were the cutest fat ant I have ever met,\"

  \"You were handsome like me, but a bit too hairy,\"

  \"But you were loyal, and fast and, and...\"

  \"I will remember you!\""""

  mc """\"No, you slug brain.\"

  \"I'm cocooning... evolving!\"

  \"Wait!\"

  \"You thought I was an ant?\""""

  antonio """\"...\"

  \"Don't sweat the deets!\"

  \"You are my best bud!\"

  \"And nothing's gonna change that!\""""
  
  mc """\"...\"

  \"But.. what am I going to do?\""""

  if Choice == "Mia":
    mc "\"Will Mia even recognize me?\""
  
  if Choice == "Permioine":
    mc "\"Will Permione even recognize me?\""

  mc """\"What if she doesn't like me anymore?\"

  \"I think I have butterflies in my stomach...\""""

  antonio """\"Well, I'll snap some sense into 'er if that's the case!\"

  \"You're the best darn man on this campus, besides me!\"

  \"There's no way she won't like ya!\"

  \"Now go get changed, and I'll go get her!\""""

  hide antonio normal

  mc "\"Wait! I'm not even out of my cocoon yet...\""

  "...struggle..."

  ".....struggle..."

  "...struggle..."

  "-pop-"

  "Huh. What are these colors?"

  "I'm.. I'm a butterfly?"

  if Choice == "Mia":
    show mia normal
    mia """\"[player_name]?\"

    \"You... you...\"

    \"You are beautiful!\""""

    mc "\"You are pretty too!\""

    hide mia normal
    show antonio normal
    antonio "\"Let's go! Or we'll be late!\""
    hide antonio normal
    scene bg college_outside
    play music "music/tracks/9_emotional_piano.wav" volume 0.5
    scene bg college_outside
    scene bg flower_bed
    scene bg other_dorm
    scene bg club_2
    show mia normal
    mia "\"Um, [player_name]...\""
    mc "\"Yes?\""
    mia "\"Let's go home.\""
    
    "I nod. Time to go home."
    "THE END"

  if Choice == "Permioine":
    show permione normal
    permione """\"*Slurp* Wow, [player_name].\"

    \"You hot.\"

    \"Come here 😘!\""""
    hide permione normal
    play music "music/tracks/7_emotional_piano.wav" volume 0.5
    scene bg college_outside
    scene bg tunnel
    scene bg track
    scene bg club_2
    show permione normal
    permione """\"Come here [player_name]!\"
    
    \"Over here.. Over here!\""""
    mc "\"Where are we going?\""
    
    "{i}smooch{/i}"
    "{i}smooch smooch smooch{/i}"
    "{b}SMOOCH SMOOOCHHHH POP SMOOCH{/b}"
    "..."

    permione "\"Tasty...\""

    # fight scene with hercules beetle

    mc "\"You think I took tai chi for fun?\""

    "THE END"
return
   