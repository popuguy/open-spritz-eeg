# python version >= 2.5
import win32api, win32con
import ctypes
import sys
import os
from ctypes import *
from numpy import *
import time
from ctypes.util import find_library
libEDK = cdll.LoadLibrary(".\\edk.dll")

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
write = sys.stdout.write
EE_EmoEngineEventCreate = libEDK.EE_EmoEngineEventCreate
EE_EmoEngineEventCreate.restype = c_void_p
eEvent      = EE_EmoEngineEventCreate()

EE_EmoEngineEventGetEmoState = libEDK.EE_EmoEngineEventGetEmoState
EE_EmoEngineEventGetEmoState.argtypes=[c_void_p,c_void_p]
EE_EmoEngineEventGetEmoState.restype = c_int

ES_GetTimeFromStart = libEDK.ES_GetTimeFromStart
ES_GetTimeFromStart.argtypes=[ctypes.c_void_p]
ES_GetTimeFromStart.restype = c_float

EE_EmoStateCreate = libEDK.EE_EmoStateCreate
EE_EmoStateCreate.restype = c_void_p
eState=EE_EmoStateCreate()

ES_GetWirelessSignalStatus=libEDK.ES_GetWirelessSignalStatus
ES_GetWirelessSignalStatus.restype = c_int
ES_GetWirelessSignalStatus.argtypes = [c_void_p]

ES_ExpressivIsBlink=libEDK.ES_ExpressivIsBlink
ES_ExpressivIsBlink.restype = c_int
ES_ExpressivIsBlink.argtypes= [c_void_p]

ES_ExpressivIsLeftWink=libEDK.ES_ExpressivIsLeftWink
ES_ExpressivIsLeftWink.restype = c_int
ES_ExpressivIsLeftWink.argtypes= [c_void_p]

ES_ExpressivIsRightWink=libEDK.ES_ExpressivIsRightWink
ES_ExpressivIsRightWink.restype = c_int
ES_ExpressivIsRightWink.argtypes= [c_void_p]

ES_ExpressivIsLookingLeft=libEDK.ES_ExpressivIsLookingLeft
ES_ExpressivIsLookingLeft.restype = c_int
ES_ExpressivIsLookingLeft.argtypes= [c_void_p]

ES_ExpressivIsLookingRight=libEDK.ES_ExpressivIsLookingRight
ES_ExpressivIsLookingRight.restype = c_int
ES_ExpressivIsLookingRight.argtypes= [c_void_p]

ES_ExpressivGetUpperFaceAction=libEDK.ES_ExpressivGetUpperFaceAction
ES_ExpressivGetUpperFaceAction.restype = c_int
ES_ExpressivGetUpperFaceAction.argtypes= [c_void_p]

ES_ExpressivGetUpperFaceActionPower=libEDK.ES_ExpressivGetUpperFaceActionPower
ES_ExpressivGetUpperFaceActionPower.restype = c_float
ES_ExpressivGetUpperFaceActionPower.argtypes= [c_void_p]

ES_ExpressivGetLowerFaceAction=libEDK.ES_ExpressivGetLowerFaceAction
ES_ExpressivGetLowerFaceAction.restype = c_int
ES_ExpressivGetLowerFaceAction.argtypes= [c_void_p]

ES_ExpressivGetLowerFaceActionPower=libEDK.ES_ExpressivGetLowerFaceActionPower
ES_ExpressivGetLowerFaceActionPower.restype = c_float
ES_ExpressivGetLowerFaceActionPower.argtypes= [c_void_p]

ES_AffectivGetExcitementShortTermScore=libEDK.ES_AffectivGetExcitementShortTermScore
ES_AffectivGetExcitementShortTermScore.restype = c_float
ES_AffectivGetExcitementShortTermScore.argtypes= [c_void_p]

ES_AffectivGetExcitementLongTermScore=libEDK.ES_AffectivGetExcitementLongTermScore
ES_AffectivGetExcitementLongTermScore.restype = c_float
ES_AffectivGetExcitementLongTermScore.argtypes= [c_void_p]


ES_AffectivGetEngagementBoredomScore=libEDK.ES_AffectivGetEngagementBoredomScore
ES_AffectivGetEngagementBoredomScore.restype = c_float
ES_AffectivGetEngagementBoredomScore.argtypes= [c_void_p]

ES_CognitivGetCurrentAction=libEDK.ES_CognitivGetCurrentAction
ES_CognitivGetCurrentAction.restype = c_int
ES_CognitivGetCurrentAction.argtypes= [c_void_p]

ES_CognitivGetCurrentActionPower=libEDK.ES_CognitivGetCurrentActionPower
ES_CognitivGetCurrentActionPower.restype = c_float
ES_CognitivGetCurrentActionPower.argtypes= [c_void_p]
    
ES_AffectivGetExcitementShortTermModelParams=libEDK.ES_AffectivGetExcitementShortTermModelParams
ES_AffectivGetExcitementShortTermModelParams.restype = c_void_p
ES_AffectivGetExcitementShortTermModelParams.argtypes = [c_void_p, POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    
ES_AffectivGetMeditationModelParams = libEDK.ES_AffectivGetMeditationModelParams
ES_AffectivGetMeditationModelParams.restype = c_void_p
ES_AffectivGetMeditationModelParams.argtypes = [c_void_p, POINTER(c_double), POINTER(c_double), POINTER(c_double)]

ES_AffectivGetEngagementBoredomModelParams = libEDK.ES_AffectivGetEngagementBoredomModelParams
ES_AffectivGetEngagementBoredomModelParams.restype = c_void_p
ES_AffectivGetEngagementBoredomModelParams.argtypes = [c_void_p, POINTER(c_double), POINTER(c_double), POINTER(c_double)]

ES_AffectivGetFrustrationModelParams = libEDK.ES_AffectivGetFrustrationModelParams
ES_AffectivGetFrustrationModelParams.restype = c_void_p
ES_AffectivGetFrustrationModelParams.argtypes = [c_void_p, POINTER(c_double), POINTER(c_double), POINTER(c_double)]
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
userID            = c_uint(0)
user                    = pointer(userID)
composerPort          = c_uint(1726)
timestamp = c_float(0.0)
option      = c_int(0)
state     = c_int(0)
def press_right():
	win32api.keybd_event(0x41, 0, 0, 0)
def get_engagement():
	return ES_AffectivGetEngagementBoredomScore(eState)
if __name__ == "__main__":
	libEDK.EE_EngineConnect("Emotiv Systems-5")
	while (True):
		state = libEDK.EE_EngineGetNextEvent(eEvent)
		if state == 0:
			eventType = libEDK.EE_EmoEngineEventGetType(eEvent)
			libEDK.EE_EmoEngineEventGetUserId(eEvent, user)
			if eventType == 64:
				libEDK.EE_EmoEngineEventGetEmoState(eEvent,eState)
				engagement = get_engagement()
				print "Engagement: " + str(engagement)
				if engagement > 0.65:
					press_right()