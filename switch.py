from dragonfly import Grammar, CompoundRule, Integer
from detection_strategies import single_tap_detection, loud_detection, medium_detection
import threading
import numpy as np
import pyautogui
from pyautogui import press, hotkey, click, scroll, typewrite, moveRel, moveTo, position
from time import sleep
from subprocess import call
from system_toggles import toggle_eyetracker, turn_on_sound, mute_sound, toggle_speechrec
import os
import pythoncom
from mode_twitch import *
from mode_browse import *
from mode_youtube import *
from mode_switch import *
from excel_grammar import *

class SwitchMode:

	def __init__(self, modeSwitcher):
		self.mode = "regular"
				
		# Create a grammar which contains and loads the command rule.
		self.grammar = Grammar("Switch grammar")                # Create a grammar to contain the command    rule.
		twitchRule = TwitchModeRule()
		twitchRule.setModeSwitch( modeSwitcher )
		self.grammar.add_rule(twitchRule)                     	# Add the command rule to the grammar.
		youtubeRule = YoutubeModeRule()
		youtubeRule.setModeSwitch( modeSwitcher )		
		self.grammar.add_rule(youtubeRule)                     	# Add the command rule to the grammar.
		browseRule = BrowseModeRule()
		browseRule.setModeSwitch( modeSwitcher )
		self.grammar.add_rule(browseRule)                     	# Add the command rule to the grammar.
		heroesRule = HeroesModeRule()
		heroesRule.setModeSwitch( modeSwitcher )
		self.grammar.add_rule(heroesRule)                     	# Add the command rule to the grammar.
		testingRule = TestingModeRule()
		testingRule.setModeSwitch( modeSwitcher )
		self.grammar.add_rule(testingRule)                     	# Add the command rule to the grammar.
		excelLogModeRule = ExcelLogModeRule()
		excelLogModeRule.setModeSwitch( modeSwitcher )
		self.grammar.add_rule(excelLogModeRule)                  # Add the command rule to the grammar.		
		
		excelModeRule = ExcelModeRule()
		excelModeRule.setModeSwitch( modeSwitcher )
		self.grammar.add_rule(excelModeRule)                  # Add the command rule to the grammar.		

		

	def start( self ):
		self.grammar.load()	
		mute_sound()
		toggle_speechrec()
		
		
	def handle_input( self, dataDicts ):
		pythoncom.PumpWaitingMessages()
		sleep(.1)
		
	def exit( self ):
		self.grammar.unload()		
		toggle_speechrec()
		turn_on_sound()

# Voice command rule combining spoken form and recognition processing.
class TwitchModeRule(CompoundRule):
    spec = "Twitchmode"                  # Spoken form of command.
	
    def _process_recognition(self, node, extras):   # Callback when command is spoken.
        self.modeSwitcher.switchMode("twitch")
		
    def setModeSwitch( self, modeSwitcher ):
        self.modeSwitcher = modeSwitcher
		
# Voice command rule combining spoken form and recognition processing.
class YoutubeModeRule(CompoundRule):
    spec = "Chinchilla purge"                  # Spoken form of command.
    def _process_recognition(self, node, extras):   # Callback when command is spoken.
        self.modeSwitcher.switchMode("youtube")
		
    def setModeSwitch( self, modeSwitcher ):
        self.modeSwitcher = modeSwitcher

class BrowseModeRule(CompoundRule):
    spec = "BrowseMode"                  # Spoken form of command.
    def _process_recognition(self, node, extras):   # Callback when command is spoken.
        self.modeSwitcher.switchMode("browse")
		
    def setModeSwitch( self, modeSwitcher ):
        self.modeSwitcher = modeSwitcher

class HeroesModeRule(CompoundRule):
    spec = "HeroesMode"                  # Spoken form of command.
    def _process_recognition(self, node, extras):   # Callback when command is spoken.
        self.modeSwitcher.switchMode("heroes")
		
    def setModeSwitch( self, modeSwitcher ):
        self.modeSwitcher = modeSwitcher
		
class TestingModeRule(CompoundRule):
    spec = "TestingMode"                  # Spoken form of command.
    def _process_recognition(self, node, extras):   # Callback when command is spoken.
        self.modeSwitcher.switchMode("testing")
		
    def setModeSwitch( self, modeSwitcher ):
        self.modeSwitcher = modeSwitcher

class DraftModeRule(CompoundRule):
    spec = "DraftMode"                  # Spoken form of command.
    def _process_recognition(self, node, extras):   # Callback when command is spoken.
        self.modeSwitcher.switchMode("heroes")

    def setModeSwitch( self, modeSwitcher ):
        self.modeSwitcher = modeSwitcher
			
class ExcelLogModeRule(CompoundRule):
    spec = "Captains log"                  # Spoken form of command.
    def _process_recognition(self, node, extras):   # Callback when command is spoken.
        self.modeSwitcher.switchMode("worklog")

    def setModeSwitch( self, modeSwitcher ):
        self.modeSwitcher = modeSwitcher

class ExcelModeRule(CompoundRule):
    spec = "This is Jimmy over"                  # Spoken form of command.
    def _process_recognition(self, node, extras):   # Callback when command is spoken.
        self.modeSwitcher.switchMode("excel")

    def setModeSwitch( self, modeSwitcher ):
        self.modeSwitcher = modeSwitcher
