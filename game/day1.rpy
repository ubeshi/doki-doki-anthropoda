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
  image bg black = Solid("#000000")

  image antonio normal = "images/antonio/normal.png"
  image mia normal = "images/mia/normal.png"
  image permione normal = "images/permione/normal.png"

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

  def stickbug_voice(event, interact=True, **kwargs):
    if not interact:
      return 
    if event == "begin":
      renpy.sound.play("music/sfx/human/running1.mp3", relative_volume = 0.25) 
    elif event == "end":
      renpy.sound.stop()

define mc = Character("[player_name]")

define antonio_ = Character("Antonio", callback = antonio_voice)
define mia_ = Character("Mia", callback = mia_voice)
define permione_ = Character("Permione", callback = permione_voice)

define unknown_ant = Character("Unknown Ant", callback = antonio_voice)
define unknown_moth = Character("Unknown soft, but familiar voice", callback = mia_voice)
define unknown_mantis = Character("Unknown Mantis", callback = permione_voice)
define stickbug = Character("Unknown Stickbug", callback = stickbug_voice)

define antonio_and_mc = Character("You and Antonio", callback = antonio_voice)
define banana = Character("Unknown Banana Slug")
define internal_dialogue = Character("Internal Dialogue")
define pillbug = Character("Unknown Pillbug")
define unknown = Character("Unknown")
define you = Character("You")

## TODO: implement point-based game globally

label day1:

  # Relationship Points
  $ Permione_points = 0
  $ Mia_points = 0

  # Choice
  $ Choice = ""

  play music "music/tracks/1_chill_pop.wav" volume 0.5
  scene bg college_outside

  unknown "\"{i}My eyes are so small.{/i}\""

  internal_dialogue "I walk into the corridor and I see the big tree."
  internal_dialogue "I am home, I thought."
  internal_dialogue "I am home."
  internal_dialogue "But without the sweet satisfaction of my neonate wings, I am astray."
  internal_dialogue "I am a caterpillar."
  internal_dialogue "A fat."
  internal_dialogue "Chubby."
  internal_dialogue "Caterpillar."
  internal_dialogue "Well, I made it to a good college. Might as well make the most out of it..."

  stop music
  play music "music/tracks/4_hiphop.wav" volume 0.5

  unknown "\"Oh my fuck damn it I’m so stupid.\""
  unknown "\"Where is my dorm…\""
  unknown "\"If only the map wasn’t so shit\""

  you "\"Hey… need some help?\""

  show antonio normal

  unknown_ant "\"What’s it to you silly boy\""

  you "\"I’m looking for my dorm too.\""

  unknown_ant "\"Alright, let’s take a look here.\""
  unknown_ant "\"Oh, you’re staying in Building B?\""

  you "\"Yeah, it looks that way.\""

  unknown_ant "\"NO WAY\""
  unknown_ant "\"We’re dormies!!!\""

  you "\"Holy fuck\""

  unknown_ant "\"My name is Antonio! Antonio Banderas.\""

  antonio_ "\"Nice to meet you!\""

  you "\"What a coincidence!\""

  $ player_name = renpy.input("My name is...")
  $ player_name = player_name.strip()

  if not player_name:
    $ player_name = "Brother of Mia"
  
  antonio_ "\"Nice to meet you [player_name]\""

  mc "\"Helter skelter\""
  mc "\"Hang sorrow\""
  mc "\"Care will kill a cat\""
  mc "\"Uptails all\""
  mc "\"And a pox on the hangman\""
  
  antonio_ "\"What's in a name? That which we call a rose\""
  antonio_ "\"By any other name would smell as sweet;\""
  antonio_ "\"So [player_name] would, were they not [player_name] call'd,\""
  antonio_ "\"Retain that dear perfection which he owes\""
  antonio_ "\"Without that title. [player_name], doff thy name,\""
  antonio_ "\"And for that name which is no part of thee\""
  antonio_ "\"Take all myself.\""
  
  mc "\"You got it\""

  scene bg room

  show antonio normal

  stop music
  play music "music/tracks/1_chill_pop.wav" volume 0.5

  mc "\"Oh wow… I guess we’re staying here for the next 3 days.\""

  antonio_ "\"Yes\""

  mc "\"Guess let's choose beds\""

  antonio_and_mc "\"Simultaneously...\""
  antonio_and_mc "\"I choose the bed on the left!\""

  mc "We both laugh and then Antonio takes the bed on the right."

  mc "\"I can give you the bed on the left if you want… It’s only right because I’m still a caterpillar.\""
  mc "\"Caterpillars are the larvae stage of the butterfly lifecycle\""
  mc "\"This means that I am still beneath your station.\""
  mc "\"I guess you could say, I am beneath you.\""
  
  antonio_ "\"Yeah sure I guess that works.\""
  antonio_ "\"Thanks.\""

  mc "Antonio and I unpack our belongings and get ready to check out the campus"

  stop music
  play music "music/tracks/8_cinematic.wav" volume 0.5
  unknown "{i}BUZZ OFF{/i}"

  mc "I look out the window…"
  mc "There’s a large crowd of people"
  mc "Guess I gotta go outside oops"

  antonio_ "\"Hey! Where are you going?\""

  mc "I should tell Antonio where I’m going. He looks antsy."
  mc "\"I’m going outside to see what’s going on, w-ant to come with?\""

  antonio_ "\"I c-ant right now, gotta keep unpacking…\""
  antonio_ "\"Have you seen my deodor-ant?\""

  hide antonio normal

  scene bg college_outside

  mc "I help Antonio for a bit and head outside"
  mc "I can’t help but smell a nice and tasty flower in the distance."
  mc "Gotta go fast. Before {i}they{/i} get to it."
  mc "I slog over towards the smell as fast as I can."
  mc "..."
  mc "Wait."
  mc "I see a huge crowd around another student but I can’t tell what’s going on."
  mc "Better investigate."
  mc "I walk over and push the other students out to get closer to the front of the crowd."

  stop music
  play music "music/tracks/9_emotional_piano.wav" volume 0.5

  mc "I see a beautiful praying mantis at center of the crowd being surrounded by a group of sweaty glasses-bearing insect students."
  
  show permione normal
  
  unknown_mantis "\"Oh no, I have Math homework due in 15 minutes… Can one of you help me with this??\""

  pillbug "\"Oh please my queen let me do your homework I need this so badly please please please\""

  banana "{i}*gurgles*{/i}"

  mc "Wait. Is she pointing at me?"

  unknown_mantis "\"Hey caterpillar, you look very handsome and smart and larvae. Could you help a lady out with her math? After all, I’m not an account-ant.\""

  mc "\"Yeah sure. Here let me give it a try.\""
  mc "Hmm, let’s read this question here."
  mc "Nathan has a big ant farm. He decided to sell some of his ants. He started with 965 ants. He sold 213. How many ants does he have now?"
  mc "\"It’s 35!\""
  
  unknown_mantis "\"Thank you so much!!\""
  unknown_mantis "{i}*blushes*{/i}"
  unknown_mantis "\"You’re actually a really cool and smart and handsome caterpillar!\""
  unknown_mantis "\"My name is Permione the Praying Mantis. I am sultry, physically adept, and popular.\""
  
  mc "\"Wow that’s so awesome.\""
  mc "\"You really do seem sultry.\""
  mc "\"And physically adept.\""
  mc "\"And popular.\""

  permione_ "\"I’m staying at building 1231415. Make sure to come around some time and hang out.\""
  permione_ "{i}*blushes and scurries away like a bug*{/i}"

  hide permione normal

  stop music
  play music "music/tracks/5_acoustic.wav" volume 0.5

  mc "..."
  mc "Wow."
  mc "She’s really something, eh fam?"
  
  unknown_moth "\"Oh hey if it isn’t the fuzziest caterpillar I know!\""

  stop music
  play music "music/tracks/9_emotional_piano.wav" volume 0.5

  mc "I turn around and see a somewhat familiar face."
  mc "Like a face that you remember from when your childhood."
  mc "Like a face that you remember going to the swings with after getting off the same bus."
  mc "Like a face that you remember…"

  show mia normal

  mia_ "\"It's-a-me!\""
  mia_ "\"Mia\""
  mia_ "\"Mia Moth!\""

  mc "Holy shit"
  mc "..."
  mc "Mia has grown into a beautiful moth that I was completely and utterly SHOCKED by."
  mc "\"You’re so big now. Like a big moth.\""
  mc "\"Not like a big caterpillar.\""
  mc "\"Because you’ve undergone metamorphosis.\""

  mia_ "\"I have undergone metamorphosis.\""
  mia_ "\"It will be your time soon my sweet little caterpillar friend.\""
  mia_ "{i}*she smiles sweetly with a warmth that is equal to a hot bird egg on human concrete in a sunny state during the summer months*{/i}"

  mc "\"Thanks… I really hope so\""
  mc "\"Anyways\""
  mc "\"What are you studying?\""

  mia_ "\"I’m studying agricultural sciences!\""
  mia_ "\"I was deciding between that and anthropology but since they both seem hard, I chose the lesser of two weevils.\""

  mc "\"That's a really good one\""

  mia_ "\"I’ll be studying at the library! Guess I’m a bit of a bookworm hehe\""
  mia_ "{i}*blushes blue*{/i}"
  mia_ "\"Come study with me if you’re free!\""
  mia_ "\"But remember one thing…\""
  mia_ "\"There are moths outside, ready to die for a light they crave but which is denied to them,\""
  mia_ "\"shielded from them.\""
  mia_ "\"Sometimes, in the midst of all I have been given, I watch the moths in us all.\""
  mia_ "\"Everybody has a light which they think they cannot live without.\""

  mc "\"Alright see you later!\""

  hide mia normal

  stop music
  play music "music/tracks/5_acoustic.wav" volume 0.5

  mc "Hmm better see what I have planned for the day."
  mc "I check my itinerary."
  
  menu:
    "It seems like I’m free all day. Should I hangout with someone?"
    "Go to building 1231415 to see Permione.":
      $ Choice = "Permione"
      $ Permione_points += 1
    "Go to the Library to see Mia.":
      $ Choice = "Mia"
      $ Mia_points += 1

  # Permione Path
  if Choice == "Permione":
    mc "..."
    mc "..."
    mc "When I'm lonely, well I know I'm gonna be I'm gonna be the man who's lonely without you"
    mc "And when I'm dreaming, well I know I'm gonna dream I'm gonna Dream about the time when I'm with you"
    mc "..."
    mc "..."
    mc "Oh I’m finally at building 1231415!"
    mc "I see a big feminine bug, very beautiful."
    mc "She looks like she’s physically adept. And popular."
    mc "Oh it’s Permione!"

    show permione normal

    stop music
    play music "music/tracks/1_chill_pop.wav" volume 0.5

    mc "\"What’s a sultry praying mantis with a wide range of vision and antennas to smell doing at a place like this?\""
    mc "\"Just kidding you told me where you lived.\""

    permione_ "\"Oh you, you’re so smart!\""
    permione_ "\"I never caught your name…\""

    mc "\"My name is [player_name]\""

    permione_ "\"Wow that’s an awesome name. Whoever named you should be so proud.\""
    permione_ "\"So\""
    permione_ "\"Proud\""

    mc "\"Anyways, what do you want to do?\""
    mc "\"I’m free all day!\""

    stop music
    play music "music/tracks/8_cinematic.wav" volume 0.5

    permione_ "\"Did you ever hear the tragedy of Dark Pit The Wet?\""
    permione_ "\"I thought not.\""
    permione_ "\"It’s not a story the Anthropoda would tell you.\""
    permione_ "\"It’s a Mantis legend.\""
    permione_ "\"Dark Pit The Wet was a dark and wet tunnel,\""
    permione_ "\"So dark and wet and so still it could use the damp to influence the fungi to create life…\""
    permione_ "\"It had such a knowledge of the dark side that it could even keep the ones he cared about from dying.\""
    permione_ "\"The dark side of the \""

    mc "\"Alright let's go check it out then\""
    mc "..."
    mc "We walked for what seemed like ages towards Dark Pit the Wet."
    mc "..."
    mc "..."
    mc "I can't get this song out of my head"
    mc "..."
    mc "..."
    mc "But I would crawl 500 miles And I would crawl 500 more"
    mc "Just to be the man who crawls a thousand miles To fall down at your door"
    mc "..."
    
    scene bg tunnel

    mc "We're here"
    mc "My eruciform body is quite damp."

    permione_ "\"Alright we’re here!\""
    permione_ "\"Let’s go check out this tunnel. I’m sure there’s going to be something funny inside.\""
    
    mc "\"I sure hope so Permione.\""
    mc "\"I sure hope so.\""
    
    mc "We walk into the tunnel."
    mc "It's dark."
    mc "It's damp."
    mc "It's a little scary."
    mc "Permione looks excited and completely fearless."
    mc "Wa Sugoi desu"

    unknown "PSPSPSPSPPSPSPSPS"

    mc "\"AAAAAAAAAAAAAAAAAA\""
    mc "\"Ooooooooooooooo\""

    permione_ "\"Don't worry, it's just a pill bug.\""
    permione_ "\"Did you know that pill bugs breathe through gills and require moist environments to breathe?\""
    permione_ "\"However, they cannot survive being submerged in water.\""

    mc "\"Thanks for the fascinating bug fact! That helped calm me down a bit.\""
    mc "\"How did you know that?\""

    permione_ "\"My father was a pill bug.\""
    
    mc "\"That must have been tough, huh.\""

    permione_ "\"It was.\""

    mc "\"Well… If you ever want to talk or need a helping mandible\""
    mc "\"Let me know.\""

    stop music
    play music "music/tracks/9_emotional_piano.wav" volume 0.5

    permione_ "{i}*Blushes blue*{/i}"
    permione_ "\"Thank you...\""

    mc "..."
    mc "We walked around the tunnel for a long time."
    mc "..."
    mc "Time to get back to the dorm"

    hide permione normal

    scene bg college_outside

    stop music
    play music "music/tracks/8_cinematic.wav" volume 0.5

    stickbug "\"Hey get out of my way you fat caterpillar\""

    mc "He looks pretty angry"
    mc "..."
    mc "I think he's going to hit me"
    mc "..."

    scene bg black

    stop music

    jump day2

  # Mia Path
  if Choice == "Mia":
    mc """
    ...

    When I'm lonely, well I know I'm gonna be I'm gonna be the man who's lonely without you

    And when I'm dreaming, well I know I'm gonna dream I'm gonna Dream about the time when I'm with you

    ...
    
    Oh I’m finally at the library!
    """

    scene bg classroom

    mc """
    I see a feminine bug, very cute.

    She looks studious. And wears her heart on her sleeve.

    Oh it’s Mia!
    """
    
    show mia normal

    stop music
    play music "music/tracks/1_chill_pop.wav" volume 0.5

    mc """
    \"What’s a bubbly moth with two compound eyes, a proboscis, and antennae doing at a place like this?\"

    \"Just kidding you told me where you were going.\"
    """

    mia_ """
    \"Oh [player_name], you're being silly again.\"

    \"You little silly guy.\"

    {i}*blushes blue*{/i}
    """

    mc "\"What are you studying\""

    mia_ """
    \"I’m getting prepared for my first exam on Electral Relations in Anthropoda\"

    ...

    \"Such an interesting topic\"
    """

    mc """
    \"Wow that's so awesome\"

    \"Can you teach me?\"
    """

    mia_ """
    ...

    \"If you'd like\"

    ...
    """

    mc """
    \"Thanks Mia Moth\"

    \"You've always been so great to me\"

    \"I’m glad you underwent metamorphosis before me\"
    """

    mia_ """
    \"Hell yeah brother\"

    \"Want to try it out?\"
    """

    mc "\"What\""

    mia_ "\"Let's go try something outside\""

    mc """
    Que pasa?

    También podría salir a verlo en español.

    …

    Nosotros salimos.
    """

    mia_ """
    \"Want to try flying?\"
    
    \"I’ll let you sit on my back like Falkor\"
    """

    mc """
    ¡Guau, esto es genial!

    \"That sounds great\"
    """

    scene bg college_outside

    stop music
    play music "music/tracks/9_emotional_piano.wav" volume 0.5

    mc """
    I slugged my way onto her back

    …

    And soared through the sky.

    Holding back salty caterpillar tears,

    All I could think was

    ...

    To me, fair friend, you never can be old,
    For as you were, when first your eye I ey’d,

    Such seems your beauty still. Three winters cold
    Have from the forests shook three summers’ pride,

    Three beauteous springs to yellow autumn turn’d
    In process of the seasons have I seen,

    Three April perfumes in three hot Junes burn’d,
    Since first I saw you fresh, which yet are green.

    Ah! yet doth beauty, like a dial-hand,
    Steal from his figure and no pace perceiv’d;

    So your sweet hue, which methinks still doth stand,
    Hath motion and mine eye may be deceiv’d:

    For fear of which, hear this, thou age unbred;
    Ere you were born, was beauty’s summer dead.

    …

    We finally landed after a few hours.
    
    …
    """

    mia_ "\"How was that my brother?\""

    mc """
    \"When I rode your back and flew the skies\"

    \"You felt like the biggest moth in the world\"

    \"Like a mam-moth\"
    """

    mia_ """
    \"Yeah well\"

    \"You don’t see many moths fly like me from back home\"
    """

    mc "\"Yeah not back home in Moth-erland\""

    mia_ """
    \"That was so fun!\"

    \"We should do this again sometime.\"
    """

    mc """
    \"Yeah for sure!\"

    \"I had a great time\"

    \"Thanks Mia\"
    """
    
    mia_ """
    \"I have to scurry soon\"

    \"I also have to study Mothmatics\"
    """

    mia_ "\"No problem sister\""

    mia_ "{i}*Blushes blue*{/i}"

    hide mia normal

    scene bg black

    stop music
    play music "music/tracks/1_chill_pop.wav" volume 0.5

    mc """
    ...

    We slowly made our way back to the library.

    …
    
    Time to get back to my dorm.
    """

    scene bg college_outside

    stop music
    play music "music/tracks/8_cinematic.wav" volume 0.5

    stickbug "\"Hey get out of my way you fat caterpillar\""

    mc "He looks pretty angry"
    mc "..."
    mc "I think he's going to hit me"
    mc "..."

    scene bg black

    stop music

    jump day2

  return
