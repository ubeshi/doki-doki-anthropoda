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

define mc = Character("[player_name]")
define antonio = DynamicCharacter("Antonio_name")
define mia = DynamicCharacter("Mia_name")
define permione = DynamicCharacter("Permione_name")
define unknown = Character("Unknown")
define internal_dialogue = Character("Internal Dialogue")
define you = Character("You")
define antonio_and_mc = Character("You and Antonio")
define pillbug = Character("Unknown Pillbug")
define banana = Character("Unknown Banana Slug")
define stickbug = Character("Unknown Stickbug")

## TODO: implement point-based game globally

# char_name "\"\""
## TODO: Update character names

label day1:
  
  # Dynamic names
  $ Antonio_name = "Unknown Ant"
  $ Permione_name = "Unknown Mantis"
  $ Mia_name = "Unknown Moth"

  # Relationship Points
  $ Permione_points = 0
  $ Mia_points = 0

  # Choice
  $ Choice = ""

  play music "music/tracks/1_chill_pop.wav" volume 0.5
  scene bg college_outside

  unknown "\"{i}My eyes are so small.{/i}\""

  internal_dialogue "I walk into the corridor and I see the big tree."
  internal_dialogue "I am home I thought"
  internal_dialogue "I am home."
  internal_dialogue "But without the sweet satisfaction of my neonate wings, I am astray."
  internal_dialogue "I am a caterpillar."
  internal_dialogue "A fat"
  internal_dialogue "Chubby"
  internal_dialogue "Caterpillar."
  internal_dialogue "Well, I made it to a good college. Might as well make the most out of it..."

  unknown "\"Oh my fuck damn it I’m so stupid.\""
  unknown "\"Where is my dorm…\""
  unknown "\"If only the map wasn’t so shit\""

  you "\"Hey… need some help?\""

  show antonio normal

  antonio "\"What’s it to you silly boy\""

  you "\"I’m looking for my dorm too.\""

  antonio "\"Alright, let’s take a look here.\""
  antonio "\"Oh, you’re staying in Building B?\""

  you "\"Yeah, it looks that way.\""

  antonio "\"NO WAY\""
  antonio "\"We’re dormies!!!\""

  you "\"Holy fuck\""

  antonio "\"My name is Antonio! Antonio Banderas.\""
  $ Antonio_name = "Antonio"
  antonio "\"Nice to meet you!\""

  you "\"What a coincidence!\""

  $ player_name = renpy.input("My name is...")
  $ player_name = player_name.strip()

  if not player_name:
    $ player_name = "Brother of Mia"
  
  antonio "\"Nice to meet you [player_name]\""

  mc "\"Helter skelter\""
  mc "\"Hang sorrow\""
  mc "\"Care will kill a cat\""
  mc "\"Uptails all\""
  mc "\"And a pox on the hangman\""
  
  antonio "\"What's in a name? That which we call a rose\""
  antonio "\"By any other name would smell as sweet;\""
  antonio "\"So [player_name] would, were they not [player_name] call'd,\""
  antonio "\"Retain that dear perfection which he owes\""
  antonio "\"Without that title. [player_name], doff thy name,\""
  antonio "\"And for that name which is no part of thee\""
  antonio "\"Take all myself.\""
  
  mc "\"You got it\""

  scene bg room

  mc "\"Oh wow… I guess we’re staying here for the next 3 days.\""

  antonio "\"Yes\""

  mc "\"Guess let's choose beds\""

  antonio_and_mc "\"Simultaneously...\""
  antonio_and_mc "\"I choose the bed on the left!\""

  mc "We both laugh and then Antonio takes the bed on the right."

  mc "\"I can give you the bed on the left if you want… It’s only right because I’m still a caterpillar.\""
  mc "\"Caterpillars are the larvae stage of the butterfly lifecycle\""
  mc "\"This means that I am still beneath your station.\""
  mc "\"I guess you could say, I am beneath you.\""
  
  antonio "\"Yeah sure I guess that works.\""
  antonio "\"Thanks.\""

  mc "Antonio and I unpack our belongings and get ready to check out the campus"

  unknown "{i}BUZZ OFF{/i}"

  mc "I look out the window…"
  mc "There’s a large crowd of people"
  mc "Guess I gotta go outside oops"

  antonio "\"Hey! Where are you going?\""

  mc "I should tell Antonio where I’m going. He looks antsy."
  mc "\"I’m going outside to see what’s going on, w-ant to come with?\""

  antonio "\"I c-ant right now, gotta keep unpacking…\""
  antonio "\"Have you seen my deodor-ant?\""

  hide antonio normal

  scene bg college_outside

  mc "I help Antonio for a bit and head outside"
  mc "I can’t help but smell a nice and tasty flower in the distance."
  mc "Gotta go fast. Before {i}they{/i} get to it."
  mc "I slog over towards the smell as fast as I can."
  mc "..."
  mc "..."
  mc "..."
  mc "..."
  mc "..."
  mc "Wait."
  mc "I see a huge crowd around another student but I can’t tell what’s going on."
  mc "Better investigate."
  mc "I walk over and push the other students out to get closer to the front of the crowd."
  mc "I see a beautiful praying mantis at center of the crowd being surrounded by a group of sweaty glasses-bearing insect students."
  
  show permione normal
  
  permione "\"Oh no, I have Math homework due in 15 minutes… Can one of you help me with this??\""

  pillbug "\"Oh please my queen let me do your homework I need this so badly please please please\""

  banana "\"{i}*gurgles*{/i}\""

  mc "Wait. Is she pointing at me?"

  permione "\"Hey caterpillar, you look very handsome and smart and larvae. Could you help a lady out with her math? After all, I’m not an account-ant.\""

  mc "\"Yeah sure. Here let me give it a try.\""
  mc "Hmm, let’s read this question here."
  mc "Nathan has a big ant farm. He decided to sell some of his ants. He started with 965 ants. He sold 213. How many ants does he have now?"
  mc "\"It’s 35!\""
  
  permione "\"Thank you so much!! {i}*blushes*{/i}\""
  permione "\"You’re actually a really cool and smart and handsome caterpillar!\""
  permione "\"My name is Permione the Praying Mantis. I am sultry, physically adept, and popular.\""
  
  $ Permione_name = "Permione"

  mc "\"Wow that’s so awesome.\""
  mc "\"You really do seem sultry.\""
  mc "\"And physically adept.\""
  mc "\"And popular.\""

  permione "\"I’m staying at building 1231415. Make sure to come around some time and hang out.\""
  permione "\"{i}*blushes and scurries away like a bug*{/i}\""

  hide permione normal

  mc "Wow."
  mc "She’s really something, eh fam?"
  
  $ Mia_name = "Unknown soft, but familiar voice"

  mia "\"Oh hey if it isn’t the fuzziest caterpillar I know!\""

  mc "I turn around and see a somewhat familiar face."
  mc "Like a face that you remember from when your childhood."
  mc "Like a face that you remember going to the swings with after getting off the same bus."
  mc "Like a face that you remember…"

  $ Mia_name = "Moth"

  show mia normal

  mia "\"It's-a-me!\""
  mia "\"Mia\""
  mia "\"Mia Moth!\""

  mc "Holy shit"
  mc "..."
  mc "Mia has grown into a beautiful moth that I was completely and utterly SHOCKED by."
  mc "\"You’re so big now. Like a big moth.\""
  mc "\"Not like a big caterpillar.\""
  mc "\"Because you’ve undergone metamorphosis.\""

  mia "\"I have undergone metamorphosis.\""
  mia "\"It will be your time soon my sweet little caterpillar friend.\""
  mia "{i}*she smiles sweetly with a warmth that is equal to a hot bird egg on human concrete in a sunny state during the summer months*{/i}"

  mc "\"Thanks… I really hope so\""
  mc "\"Anyways\""
  mc "\"What are you studying?\""

  mia "\"I’m studying agricultural sciences!\""
  mia "\"I was deciding between that and anthropology but since they both seem hard, I chose the lesser of two weevils.\""

  mc "\"That's a really good one\""

  mia "\"I’ll be studying at the library! Guess I’m a bit of a bookworm hehe {i}*blushes blue*{/i}\""
  mia "\"Come study with me if you’re free!\""
  mia "\"But remember one thing…\""
  mia "\"There are moths outside, ready to die for a light they crave but which is denied to them,\""
  mia "\"shielded from them.\""
  mia "\"Sometimes, in the midst of all I have been given, I watch the moths in us all.\""
  mia "\"Everybody has a light which they think they cannot live without.\""

  mc "\"Alright see you later!\""

  hide mia normal

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

    mc "\"What’s a sultry praying mantis with a wide range of vision and antennas to smell doing at a place like this?\""
    mc "\"Just kidding you told me where you lived.\""

    permione "\"Oh you, you’re so smart!\""
    permione "\"I never caught your name…\""

    mc "\"My name is [player_name]\""

    permione "\"Wow that’s an awesome name. Whoever named you should be so proud.\""
    permione "\"So\""
    permione "\"Proud\""

    mc "\"Anyways, what do you want to do?\""
    mc "\"I’m free all day!\""

    permione "\"Did you ever hear the tragedy of Dark Pit The Wet?\""
    permione "\"I thought not.\""
    permione "\"It’s not a story the Anthropoda would tell you.\""
    permione "\"It’s a Mantis legend.\""
    permione "\"Dark Pit The Wet was a dark and wet tunnel,\""
    permione "\"So dark and wet and so still it could use the damp to influence the fungi to create life…\""
    permione "\"It had such a knowledge of the dark side that it could even keep the ones he cared about from dying.\""
    permione "\"The dark side of the \""

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

    permione "\"Alright we’re here!\""
    permione "\"Let’s go check out this tunnel. I’m sure there’s going to be something funny inside.\""
    
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

    permione "\"Don't worry, it's just a pill bug.\""
    permione "\"Did you know that pill bugs breathe through gills and require moist environments to breathe?\""
    permione "\"However, they cannot survive being submerged in water.\""

    mc "\"Thanks for the fascinating bug fact! That helped calm me down a bit.\""
    mc "\"How did you know that?\""

    permione "\"My father was a pill bug.\""
    
    mc "\"That must have been tough, huh.\""

    permione "\"It was.\""

    mc "\"Well… If you ever want to talk or need a helping mandible\""
    mc "\"Let me know.\""

    permione "{i}*Blushes blue*{/i}"
    permione "\"Thank you...\""

    mc "..."
    mc "We walked around the tunnel for a long time."
    mc "..."
    mc "Time to get back to the dorm"

    hide permione normal

    scene bg college_outside

    stickbug "\"Hey get out of my way you fat caterpillar\""

    mc "He looks pretty angry"
    mc "..."
    mc "I think he's going to hit me"
    mc "..."
    mc "..."
    mc "..."

    scene bg black

  # Mia Path
  if Choice == "Mia":
    mc """...
    ...
    When I'm lonely, well I know I'm gonna be I'm gonna be the man who's lonely without you
    And when I'm dreaming, well I know I'm gonna dream I'm gonna Dream about the time when I'm with you
    ...
    ...
    Oh I’m finally at the library!"""

    scene bg classroom

    mc """I see a feminine bug, very cute.
    She looks studious. And wears her heart on her sleeve.
    Oh it’s Mia!"""
    
    show mia normal

    mc """\"What’s a bubbly moth with two compound eyes, a proboscis, and antennae doing at a place like this?\"
    \"Just kidding you told me where you were going.\"
    """

    mia """\"Oh [player_name], you're being silly again.\"
    \"You little silly guy.\"
    {i}*blushes blue*{/i}
    """

    mc "\"What are you studying\""

    mia """\"What are you studying\"
    ...
    \"Such an interesting topic\"
    """

    mc """\"Wow that's so awesome\"
    \"Can you teach me?\"
    """

    mia """...
    \"If you'd like\"
    ..."""

    mc """\"Thanks Mia Moth\"
    \"You've always been so great to me\"
    \"I’m glad you underwent metamorphosis before me\""""

    mia """\"Hell yeah brother\"
    \"Want to try it out?\""""

    mc "\"What\""

    mia "\"Let's go try something outside\""

    mc """Que pasa?
    También podría salir a verlo en español.
    …
    Nosotros salimos."""

    mia """\"Want to try flying?\"
    \"I’ll let you sit on my back like Falkor\""""

    mc """¡Guau, esto es genial!
    \"That sounds great\""""

    scene bg college_outside

    mc """I slugged my way onto her back
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
    …
    We finally landed after a few hours.
    …"""

    mia "\"How was that my brother?\""

    mc """\"When I rode your back and flew the skies\"
    \"You felt like the biggest moth in the world\"
    \"Like a mam-moth\""""

    mia """\"Yeah well\"
    \"You don’t see many moths fly like me from back home\""""

    mc "\"Yeah not back home in Moth-erland\""

    mia """\"That was so fun!\"
    \"We should do this again sometime.\""""

    mc """\"Yeah for sure!\"
    \"I had a great time\"
    \"Thanks Mia\""""
    
    mia """\"I have to scurry soon\"
    \"I also have to study Mothmatics\""""

    mia "\"No problem sister\""

    mia "{i}*Blushes blue*{/i}"

    hide mia normal

    scene bg black

    mc """...
    We slowly made our way back to the library.
    …
    Time to get back to my dorm."""

    scene bg college_outside

    stickbug "\"Hey get out of my way you fat caterpillar\""

    mc "He looks pretty angry"
    mc "..."
    mc "I think he's going to hit me"
    mc "..."
    mc "..."
    mc "..."

    scene bg black

  return
