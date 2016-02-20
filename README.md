# Introduction
This is a doorbell for a dorm room. If anyone posts "door" or other keywords in a GroupMe chatroom it plays a little melody alerting people to open the door. I run this script that checks the latest message on a Raspberry Pi connected to a speaker.

# Motivation
I created this because I am in GroupMe chat with around 25 people and we often hang out in my suite room on campus. Not everyone in the group lives in the building so at times the group chat is just spammed with request to tell someone to open the door. I tried to think of a way so the people who were already in the main suite room to be alerted that someone needed to get the door so I created the obviously solution which is a doorbell.

# Install
In order to run this you need Python and the GroupyAPI which can be found [here] (https://pypi.python.org/pypi/GroupyAPI).

# Running
1. Properly setup GroupyAPI with your key
2. Find the ID of your GroupMe chatroom and modify dormBellModule.py
3. Run main.py (make sure you have both .dat files before hand)

# Future Changes
Play music not through a youtube link but by opening a file. Instead of having the script constantly checking (someone might post something before doorbell is checked) make it work through a bot with a callback url instead.
