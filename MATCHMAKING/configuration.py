class Configuration:
	def __init__( self ):
		#*************
		# Constantes *
		#*************
		self.DEBUGMODE = False
		self.BACKGROUNDCOLOR = 'green'
		self.PAWN = { 
			'GAP': 10, 
			'SIZE': 50, 
			'INCREMENT': 60, 
			'COLOR': { 
				0: 'white', 
				1: 'yellow', 
				2: 'red' 
			}
		}
		self.GRID = { 
			'XGAP': 10,
			'YGAP': 30,
			'LINE': 6,
			'COLUMN': 6,
			'MINRANDOMPAWN': 20
		}
		self.CURSOR = { 
			'WSIZE': self.PAWN['SIZE'], 
			'HSIZE': 10, 
			'XGAP': 0, 
			'YGAP': 10 
		}
		self.DISPLAY = { 
			'WIDTH': self.PAWN['INCREMENT'] * self.GRID['COLUMN'] + self.GRID['XGAP'], 
			'HEIGHT': self.PAWN['INCREMENT'] * self.GRID['LINE'] + self.GRID['YGAP'] 
		}
		self.DIRECTION = {
			'LEFT': 1,
			'RIGHT': 2
		}


		#############
		# Variables #
		#############
		self._EXEC_ = {
			'CONTINUE_PROGRAM': True,
			'DEBUG_MODE': False,
			'HELP_SHOWED': False
		}
 
CONFIGURATION = Configuration()