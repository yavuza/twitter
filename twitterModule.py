import simplejson
import httplib2
import time
import twitterModule
from twython import Twython

### PARAMETERS
USERS_FILE = "file/path"
REMOVED_USERS_FILE= "file/path"
USER_NUMBER=0
CLONING_USER="@userName"
###

def readFileLine(fileName,lineNumber):
	fdesc=open(fileName,"r")
	fileLines=fdesc.readlines()
	fileLine=fileLines[lineNumber].split()
	fdesc.close()
	return fileLine

def readAllFileLines(fileName):
	fdesc=open(fileName,"r")
	fileLines=fdesc.readlines()
	fdesc.close()
	return fileLines
	
def appendFile(fileName,lineText):
	fdesc=open(fileName,"a")
	fdesc.write(str(lineText)+"\n")
	fdesc.close()

def authenticate_twy(userNumber):
	authValues=readFileLine(USERS_FILE,userNumber)
	api = Twython(authValues[2],authValues[3],authValues[4],authValues[5])
	print "My username: %s"%authValues[1]
	return api

def getSetOfAuthenticatedUsersFriends_twy(pApi):
	friends=pApi.get_friends_ids().get("ids")
	print "Users which I followed: %d"%len(friends)
	return set(friends)

def getSetOfSpecificUsersFollowers_twy(pApi, screenName):
	usersFollowers=pApi.get_followers_ids(screen_name = screenName).get("ids")
	print "Users that follow this user: %d"%len(usersFollowers)
	return set(usersFollowers)

def getAuthenticatedUserID_twy(pApi,userNumber):
	userName=readFileLine(USERS_FILE,userNumber)
	userInfo=pApi.show_user(screen_name=userName[userNumber])
	return userInfo["id"]

def getSetOfAuthenticatedUsersFollowers_twy(pApi):
	followers=pApi.get_followers_ids().get("ids")
	print "Users that follow me: %d"%len(followers)
	return set(followers)

def getSetOfUnfollowedUsers(pApi):
	users=readAllFileLines(USERS_FILE)
	return set(users)



