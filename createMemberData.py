import groupy
import dormBellModule
import pickle

# Create a data file with amount of times someone can use doorbell in a day
# Put in place so people don't spam it and if they do they can stay in the cold
def createMemberData(group):
    members = group.members()
    membersDict = {}
    for member in members:
        memberID = member.user_id
        membersDict[memberID] = 2
    pickle.dump(membersDict, open("members.dat", "wb"))

def main():
    group = dormBellModule.getGroup()
    createMemberData(group)

main()
