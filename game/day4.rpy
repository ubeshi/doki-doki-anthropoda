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

  \"I thought you were finally getting more comfortable.\"

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
  
  if Choice == "Permione":
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
    show mia normal at truecenter:
      zoom 0.5
    mia """\"[player_name]?\"

    \"You... you...\"

    \"You are beautiful!\""""

    mc "\"You are pretty too!\""

    hide mia normal
    show antonio normal
    antonio "\"Let's go! Or we'll be late!\""
    hide antonio normal
  
    scene bg club_2
    play music "music/tracks/4_hiphop.wav" volume 0.5
    show antonio normal at truecenter:
      zoom 0.5
      xzoom -1.0

    show ladybug normal at truecenter:
      zoom 0.5
      xzoom -1.0
      xalign 0.4
      yalign 0.7
    
    antonio """
    \"Go gogogogo.\"

    \"Where are the rest of my posie?\""""

    show antonio normal onlayer layer2 at truecenter:
      zoom 0.5
      xzoom -1.0
      xalign 0.4
      yalign 0.3

    show ladybug normal onlayer layer2 at truecenter:
      zoom 0.5
      xzoom -1.0
      xalign 0.3
      yalign 0.5

    show antonio normal onlayer layer3 at truecenter:
      zoom 0.5
      xzoom -1.0
      xalign 0.7
      yalign 0.7

    antonio "\"LETS GO, BOOM BOOM BOOM.\""

    ladybugs """\"WHOOOO!\"

    \"AHH, IT'S DJ CiciDada!\""""
    
    announcer "\"ITS TIME TO PARTY!\""

    unknown_ant """

    \"IS THAT A HEATLAMP?\"

    \"It's so bright and...\""""
    
    "Bobby walks slowly walks towards the bright light."
    
    hide antonio normal onlayer layer3

    unknown_ant "\"BOBBY NOOOO!\""

    hide antonio normal
    hide ladybug normal
    hide antonio normal onlayer layer2
    hide ladybug normal onlayer layer2

    "Antman and Antonio follow behind."

    "They drag Bobby back to the dance floor."

    "In the distant, a bunch of fire ants show up!"

    announcer "\"IT'S A DANCE BATTLE!\""

    show mia normal at truecenter:
      zoom 0.5

    mia """\"[player_name], it's getting a bit loud in here.\"
    
    \"Do you want to head outside with me?\""""
    
    mc "*nod nod*"
    hide mia normal

    scene bg flower_bed
    play music "music/tracks/9_emotional_piano.wav" volume 0.5

    show mia normal at truecenter:
      zoom 0.5

    mia """\"I never knew Antonio could dance!\"

    \"This has been the best night of my life.\"

    \"I still can't believe {b}you{\b} chose {b}me{\b}!\"

    \"Sometimes I wonder if I am still inside my cocoon... dreaming.\""""
    
    "..."
    "..."

    mia "\"Um, [player_name]...\""
    mc "\"Yes?\""
    mia "\"Let's go home.\""
    
    "I nod. Time to go home."
    "THE END"

  if Choice == "Permione":
    stop music
    
    show permione normal
    permione """\"*Slurp* Wow, [player_name].\"

    \"You hot.\"

    \"Come here my sweet churro!\"

    """

    play music "music/tracks/9_emotional_piano.wav" volume 0.5

    mc """

    ...

    \"Wow. You're really something Permione.\"

    """

    """
    How does she do it?

    Permione is so sultry.

    It's not often you meet someone who carries themselves with the husky confidence of an old man in a locker room.
    
    ...

    It's magical.

    """

    permione """
    ...

    \"I know.\"

    """

    """

    We spend a bit of time in the room.

    It's getting dark.

    Time to get ready for the dance at the Cricket Club.

    """

    scene black

    """

    We rushed to the Cricket Club.

    """

    scene bg club_2

    """

    Everyone's here!

    I think I lost Permione...

    Where is she?

    """

    permione """\"Come here [player_name]!\"
    
    \"Over here.. Over here!\""""
    
    mc "\"Oh hey!\""

    """

    I walked around the crowds of insects to get to Permione.

    She looks radiant.

    Like a thick and voluptuous blade of grass.

    """

    show permione normal

    permione "\"How do I look?\""

    mc "\"You look like a thick and voluptuous blade of grass.\""

    permione "\"Wow [player_name]. You always know what to say to a sultry and physically adept mantis like me...\""

    "{i}smooch{/i}"
    "{i}smooch smooch smooch{/i}"
    "{b}SMOOCH SMOOOCHHHH POP SMOOCH{/b}"
    "..."

    permione "\"Tasty...\""

    "Bro wtf she ate my head lol"

    "THE END"
return
   