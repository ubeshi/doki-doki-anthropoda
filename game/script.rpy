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
  image bugs normal = "images/extra_bugs/normal.png"
  image ladybug normal = "images/extra_bugs/ladybug.png"

  image black = Solid("#000")

  define config.layers =['master', 'transient', 'screens', 'overlay','layer2','layer3']

init python:
  def antonio_voice(event, interact=True, **kwargs):
    if not interact:
      return 
    if event == "begin":
      renpy.sound.play("music/sfx/human/man_gargle1.mp3", relative_volume = 0.15)
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

  def stickbug_voice(event, interact=True, **kwargs):
    if not interact:
      return 
    if event == "begin":
      renpy.sound.play("music/sfx/human/running1.mp3", relative_volume = 0.25)
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

# day1 specific characters
define unknown_ant = Character("Unknown Ant", callback = antonio_voice)
define unknown_moth = Character("Unknown soft, but familiar voice", callback = mia_voice)
define unknown_mantis = Character("Unknown Mantis", callback = permione_voice)
define stickbug = Character("Unknown Stickbug", callback = stickbug_voice)
define antonio_and_mc = Character("You and Antonio", callback = antonio_voice)
define banana = Character("Unknown Banana Slug")
define internal_dialogue = Character("")
define pillbug = Character("Unknown Pillbug")
define unknown = Character("Unknown")
define you = Character("You")

# day2 specific characters
define teacher = Character("Teacher")

# day3 specific characters
define ladybugs = Character("Ladybug Fan Club", callback = ladybugs_voice)
define announcement = Character("Announcement")
define announcer = Character ("Announcer", callback = announcer_voice)

label start:
  call Day_1
  call Day_2
  call Day_3
  call Day_4

  return
