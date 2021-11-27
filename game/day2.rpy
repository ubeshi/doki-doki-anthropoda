label Day_2 :
  scene bg room
  show antonio normal
  antonio "\"92, 93, 94!\""
  hide antonio normal
  antonio "\"95, 96, 97!\""
  show antonio normal
  antonio "\"98, 99, 100!\""
  mc "\"Zzzz... huh?\""
  
  "I am so dizzy, how did I make it back to the dorm..."
  antonio "\"198, 199, 200!\""
  antonio "\"Oh, you're awake!\""
  antonio "\"You were out {b}cold{/b}! I almost thought I lost you.\""
  antonio "\"You got all your limbs? Damn, all 16? You'd do fine without a few.\""
  antonio "\"I remember fighting alongside Four-armed Jack, Antman, and Bent-leg Billy.\""
  antonio "\"{b}Battle scars is what makes you a man!{b}\""
  mc "\"What... happened yesterday?\""
  antonio "\"Who knows? Did you fight someone mano-a-mano?\""
  antonio "\"I just saw you laying there, twitching on my 10km run.\""
  antonio "\"So I thought, extra weight training!\""
  mc "\"...thanks.\""

  if Mia_points > Permione_points:
    "I hope Mia didn't see me on his back."
    "So embarassing."
  elif Permione_points >= Mia_points:
    "I hope Permione didn't see me on his back."
    "So embarassing."

  antonio "\"Boy! You better sober up!\""
  antonio "\"There's a worse war incoming today!\""
  mc "\"War?\""
  antonio "\"Yeah! I heard that barely anyone can make it through without a head injury!\""
  antonio "\"Brace yourself...\""
  antonio "\"...\""
  antonio "\"....\""
  antonio "\"...\""
  antonio "\"It's the written exam!\""
  mc "\"...\""
  antonio "\"Don't be scared brother! I got your back!\""
  antonio "\"Psht... Inside tip.\""
  antonio "\"I hear they come wave after wave...\""
  antonio "\"But! If you hold on long enough,\""
  antonio "\"You will hear a bell,\""
  antonio "\"And then it'll all be over!\""
  mc "\"...\""
  mc "\"Let's go get breakfast.\""
  antonio "\"That's the spirit!\""
  antonio "\"We need {b}all the carbs{/b} to bulk up!\""
  antonio "\"{b}Charge!{/b}\""
  hide antonio normal
  scene bg classroom
  play music "music/tracks/3_acoustic_pop.wav" volume 0.5
  "Oh, there is Mia... and Permione."
  play sound "music/sfx/human/heartbeats.mp3" volume 0.5
  "Should I go say hi?"
  play music "music/tracks/3_acoustic_pop.wav" volume 0.5
  show mia normal at topright: 
    zoom 0.5
    xalign 1.1
  show permione normal at left
  mia "\"What do you mean, you never asked me to!\""
  mia "\"You always {i}say{/i} you will clean up afterwards,\""
  mia "\"And then you {b}never{/b} do!\""
  mia "\"So I go and spend all night cleaning!\""
  mia "\"And {b}all{/b} you can say is, \'Don't touch my stuff\'?\""
  permione "\"Girl, you do you.\""
  permione "\"Don't come crying to me when you pick up the wrong magazine... and...\""
  permione "\"Oh, is that what it is, couldn't sleep well last night?\""
  permione "\"Did little mothy girl have too much to think about?\""
  mia "\"{b}You{/b}!\""
  permione "\"Haha, how 'bout this?\""
  permione "\"We make a bet with the test today...\""
  permione "\"And whoever wins listens to the other!\""
  mia "\"Deal!\""
  mia "\"You are going to lose for sure!\""
  mia "\"I am at the top of the class!\""
  mia "\"You are going down!\""
  play sound "music/sfx/human/man_coughing.mp3" volume 0.5
  mc "\"Um... Good morning?\""
  play music "music/tracks/3_acoustic_pop.wav" volume 0.5
  hide mia normal
  show permione normal
  permione "\"Morning [player_name].\""
  permione "\"Looking fine... tasty...\""
  hide permione normal
  play sound "music/sfx/daily/door_chime3.mp3" volume 0.5
  teacher "\"Okay class! Find a seat and we'll begin.\""

  menu:
    "Where should I sit?"
    "Sit with Permione.":
      $ Choice = "Permione"
      $ Permione_points += 1
    "Go find Mia and sit with her.":
      $ Choice = "Mia"
      $ Mia_points += 1

  if Choice == "Permione":
    show permione normal
    permione "\"Good luck!\""
    permione "\"I'll bring you somewhere spicy when we are done.\""
    hide permione normal
    scene black
    play sound "music/sfx/daily/door_chime3.mp3" volume 0.5
    antonio "\"I'm {b}free{/b}!\""
    scene bg college_outside
    show permione normal
    permione "\"Quick! Follow me!\""
    hide permione normal
    mc "\"Wait for me!\""
    scene bg tunnel
    play sound "music/sfx/magic01/in_a_cave.mp3" volume 0.5
    mc"\"Pe.. Permione?\""
    show permione normal
    permione "\"{i}Boo{/i}!\""
    permione "\"Haha, look at your face!\""
    permione "\"Over here!\""
    hide permione normal
    "Wow, that's a very hidden entrance."
    scene black
    play music "music/tracks/2_chill_beats.wav" volume 0.2
    "I wonder where we are going..."
    play music "music/tracks/2_chill_beats.wav" volume 0.5
    scene bg club
    show permione normal
    permione "\"Loosen up! It's not every day DJ CiciDada is here!\""
    play music "music/tracks/2_chill_beats.wav" volume 0.8
    hide permione normal
    scene black

    "..."

  if Choice == "Mia":
    show mia normal at top:
      zoom 0.5
    mc "\"Oh uh... good morning Mia.\""
    mia "\"Ah, I didn't read the magazine.\""
    mia "\"I uh, just... looked at the cover!\""
    mia "\"...\""
    mia "\"And, uh, cleaned the inside. Yep!\""
    mia "\"I made sure all the pages were clean. That's it!\""
    mc "\"...\""
    mia "\"No! I can explain...\""
    play sound "music/sfx/daily/door_chime3.mp3" volume 0.5
    mia "\"We'll talk after!\""
    mia "\"Good luck! I know you'll do well.\""
    mia "\"You always did...!\""
    scene black
    play sound "music/sfx/daily/door_chime3.mp3" volume 0.5
    antonio "\"I'm {b}free{/b}!'\""
    scene bg college_outside
    scene bg other_dorm
    mia "\"...And then Permione complains that I shouldn't touch her stuff!\""
    mia "\"And she yells at me!\""
    mia "\"Like... you would have cleaned up too right?\""
    mc "*nod nod*"
    mia "\"Anyways. enough about me!\""
    mia "\"How have you been?\""
    mia "\"I haven't heard from you ever since I cocooned...\""
    mc "\"...\""
    mia "\"...\""
    mia "\'I'm so sorry.\""
    mia "\"I didn't mean to bring that up.\""
    mia "\"You are perfect the way you are!\""
    mia "\"...\""
    mia "\"Oh right, do you want to see some pictures I took?\""
    mia "\"I've always wanted to show you how much I've grown!\""
    mia "\"Here and here, and this one too!\""
    scene black

    "..."
  return
