import simplejson
import httplib2
import time
import twitterModule
import sys

api_twy=twitterModule.authenticate_twy(twitterModule.USER_NUMBER);

setA=twitterModule.getSetOfSpecificUsersFollowers_twy(api_twy,twitterModule.CLONING_USER)
setB=twitterModule.getSetOfAuthenticatedUsersFriends_twy(api_twy)
setC=twitterModule.getSetOfUnfollowedUsers(api_twy)
setAdB=setA-setB
setAdBdC=setAdB-setC
setAdBdC.discard(twitterModule.getAuthenticatedUserID_twy(api_twy,twitterModule.USER_NUMBER))

print "users to follow: %d"%len(setAdB)
print "users to follow (without removeds): %d"%len(setAdBdC)

for userID in setAdB:
        print "userID: %s"%userID
	print "screen name: %s"%api_twy.show_user(user_id=userID)["name"]
	try:
        	d=api_twy.create_friendship(user_id=userID)
	except Exception as exc:
		print "This user cant be added(%s)"%exc
		continue
	time.sleep(1)






