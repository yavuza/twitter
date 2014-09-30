import simplejson
import httplib2
import twitterModule
import sys
from twython import Twython

api_twy=twitterModule.authenticate_twy(twitterModule.USER_NUMBER);

setA=twitterModule.getSetOfAuthenticatedUsersFriends_twy(api_twy)
setB=twitterModule.getSetOfAuthenticatedUsersFollowers_twy(api_twy)
setAdB=setA-setB

print "users that I follow without their following: %d"%len(setAdB)

for userID in setAdB:
    try:
        print "userID: %s"%userID
        d=api_twy.destroy_friendship(user_id=userID)
        twitterModule.appendFile(twitterModule.REMOVED_USERS_FILE,userID)
    except Exception as exc:
        print "This user cant be removed(%s)"%exc
        continue
