# Tecno Timers script for Streamlabs Chatbot
# Copyright (C) 2020 Luis Sanchez
#
# Versions:
#   - 1.0.0 19/09/2020 - Release

import os
import re
import sys
import clr
import time
import json
import codecs
from System import Environment
clr.AddReference("System.Windows.Forms")
from System.Windows.Forms import OpenFileDialog, DialogResult
from System.Windows.Forms.MessageBox import Show
msgbox = lambda obj: Show(str(obj))

# Script Information
ScriptName = "Tecno Timers"
Description = "Need a simple timer? Do a command and get a timer!"
Creator = "LuisSanchezDev"
Version = "1.0.0"
Website = "https://www.fiverr.com/luissanchezdev"

# Define Global Variables
global PATH, SETTINGS, CONFIG_FILE, SOUND_START, SOUND_END
PATH = os.path.dirname(os.path.realpath(__file__))
SETTINGS = {}
CONFIG_FILE = os.path.join(PATH, "config.json")
SOUND_START = os.path.join(PATH, "sound_start.mp3")
SOUND_END = os.path.join(PATH, "sound_end.mp3")

global timers
timers = []

# Initialize Data (Only called on load)
def Init():
  global SETTINGS, CONFIG_FILE
  try:
    with codecs.open(CONFIG_FILE, encoding="utf-8-sig", mode='r') as file:
      SETTINGS = json.load(file, encoding="utf-8-sig")
  except:
    SETTINGS = {
      "command": "!timer",
      "permission": "Moderator",
      "min_duration": 10,
      "background_color": "rgba(255,180,180,1.0)",
      "foreground_color": "rgba(150,20,20,1.0)",
      "text_color": "rgba(255,255,255,1.0)",
    }
  timers = []
  Parent.BroadcastWsEvent("EVENT_FORCE_RELOAD", "{")

# Execute Data / Process messages
def Execute(data):
  if not data.IsChatMessage():
    return
  command = data.GetParam(0)
  if command == SETTINGS["command"]:
    if not Parent.HasPermission(data.User, SETTINGS["permission"], ""):
      return Parent.SendStreamMessage("Sorry {0}, you don't have permission to use this command".format(data.UserName))
    usage = lambda: Parent.SendStreamMessage("Usage: !timer <number><h/m/s> <reason> for example !timer 1h blindfold game, !timer 5m drink water, !timer 30s run around")
    if data.GetParamCount() < 3:
      return usage()
    requested_time = data.GetParam(1)
    time_segment = requested_time[-1].lower()
    if time_segment not in ["h", "m", "s"]:
      return usage()
    duration = requested_time[:-1]
    try:
      duration = int(duration)
    except:
      return usage()
    
    start_timer(duration, time_segment, " ".join(data.Message.split(" ")[2:]))


# Tick method (Gets called during every iteration even when there is no incoming data)
def Tick():
  global timers
  if len(timers) == 0:
    return
  for t in timers:
    elapsed = time.time() - t["start"]
    if elapsed >= t["duration"]:
      Parent.SendStreamMessage("Time's up for: " + t["reason"])
      timers.remove(t)


# Reload Settings (Called when a user clicks the Save Settings button in the Chatbot UI)
def ReloadSettings(jsonData):
  Init()

# Parse method (Allows you to create your own custom $parameters)
def Parse(parseString, userid, username, targetid, targetname, message):
  if not "$ttimer" in parseString:
    return parseString
  # test = "$timer(1m,Play with one hand)"
  # test = "$bgtimer(#FF60FF)"
  # test = "$fgtimer(#FF3333)"
  # test = "$texttimer(#FFCDEF)"
  tmp_parse_string = parseString
  new_timer = {
    "duration": None,
    "reason": None,
    "background_color": None,
    "foreground_color": None,
    "text_color": None
  }
  
  timer_pattern = r'\$ttimer\("([0-9]+[hms])","(.*?)"\)'
  timer_match = re.search(timer_pattern, parseString)
  if not timer_match:
    # msgbox("Pattern didnt match")
    return parseString
  new_timer["duration"], new_timer["reason"] = timer_match.groups()
  tmp_parse_string = re.sub(r'\$ttimer\(".*?"\)', "", tmp_parse_string)
  
  if "$bgtimer" in parseString:
    bg_pattern = r'\$bgtimer\("(.*?)"\)'
    bg_match = re.search(bg_pattern, parseString)
    if not bg_match:
      return parseString
    new_timer["background_color"], = bg_match.groups() 
    tmp_parse_string = re.sub(r'\$bgtimer\(".*?"\)', "", tmp_parse_string)
  if "$fgtimer" in parseString:
    fg_pattern = r'\$fgtimer\("(.*?)"\)'
    fg_match = re.search(fg_pattern, parseString)
    if not fg_match:
      return parseString
    new_timer["foreground_color"], = fg_match.groups() 
    tmp_parse_string = re.sub(r'\$fgtimer\(".*?"\)', "", tmp_parse_string)
  if "$texttimer" in parseString:
    text_pattern = r'\$texttimer\("(.*?)"\)'
    text_match = re.search(text_pattern, parseString)
    if not text_match:
      return parseString
    new_timer["text_color"], = text_match.groups() 
    tmp_parse_string = re.sub(r'\$texttimer\(".*?"\)', "", tmp_parse_string)
  # msgbox("\n".join([k+": "+str(v) for k,v in new_timer.iteritems()]))
  for k, v in new_timer.iteritems():
    if v:
      new_timer[k] = v.strip()
  start_timer(
    int(new_timer["duration"][:-1]),
    new_timer["duration"][-1:],
    new_timer["reason"],
    new_timer["background_color"],
    new_timer["foreground_color"],
    new_timer["text_color"]
  )
  return tmp_parse_string


def start_timer(duration, time_segment, reason, background_color=None, foreground_color=None, text_color=None):
  global SETTINGS, timers
  background_color = background_color or SETTINGS["background_color"]
  foreground_color = foreground_color or SETTINGS["foreground_color"]
  text_color = text_color or SETTINGS["text_color"]
  
  if time_segment == "h":
    duration_seconds = duration * 60 * 60
  elif time_segment == "m":
    duration_seconds = duration * 60
  elif time_segment == "s":
    duration_seconds = duration
  if duration_seconds < SETTINGS["min_duration"]:
    return Parent.SendStreamMessage("Minimum time is 10s")
  new_timer = {
    "start": time.time(),
    "duration": duration_seconds,
    "reason": reason,
    "foreground_color": foreground_color,
    "background_color": background_color,
    "text_color": text_color
  }
  timers.append(new_timer)
  Parent.BroadcastWsEvent("EVENT_NEW_TIMER", json.dumps(new_timer))
  Parent.SendStreamMessage("Started timer: " + reason + "(" + str(duration)+time_segment+")")

# Script UI Buttons
def _pick_sound_file(title, local_path):
  dialog = OpenFileDialog()
  dialog.Title = title
  dialog.InitialDirectory = Environment.GetEnvironmentVariable("USERPROFILE")
  dialog.Filter = "mp3 files (*.mp3)|*.mp3"
  if dialog.ShowDialog() == DialogResult.OK:
    os.system('copy "{0}" "{1}"'.format(
      dialog.FileName,
      local_path
    ))
    Parent.PlaySound(local_path, 1)

def pick_starting_sound():
  global SOUND_START
  _pick_sound_file("Selct a starting sound file", SOUND_START)

def pick_ending_sound():
  global SOUND_END
  _pick_sound_file("Selct a ending sound file", SOUND_END)


# UI Buttons
def donate():
  os.startfile("https://streamlabs.com/luissanchezdev/tip")
def open_contact_me():
  os.startfile("https://www.fiverr.com/luissanchezdev")
def open_contact_td():
  os.startfile("https://www.fiverr.com/tecno_diana")
def open_readme():
  os.startfile("https://github.com/LuisSanchez-Dev/TecnoTimers")