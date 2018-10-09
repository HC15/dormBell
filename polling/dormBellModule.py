import groupy
import webbrowser
import pickle

# Get group that you want to keep track of
def getGroup():
        groups = groupy.Group.list()
        mainGroup = groups.first
        
        for group in groups:
                # Put group id you want to keep track off
                if(group.group_id == "00000000"):
                        mainGroup = group

        return mainGroup

def dormBell(group):
        newestMessage = group.messages().newest
        message = newestMessage.text.lower()
        poster = newestMessage.user_id

        membersDict = pickle.load(open("members.dat", "rb"))
        lastPoster = pickle.load(open("lastMessage.dat", "rb"))

        if (("door" in message or "back" in message) and
            (poster != lastPoster)):
                if(membersDict[poster] > 0):
                        webbrowser.open("https://www.youtube.com/watch?v=g7_VlmEamUQ")
                        membersDict[poster] -= 1
        pickle.dump(poster, open("lastMessage.dat", "wb"))
