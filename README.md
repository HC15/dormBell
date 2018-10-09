# Introduction
This is a doorbell for a dorm room. If anyone posts "door" or other keywords in specified GroupMe chatroom, it plays a song alerting people to open the door. It uses websockets to check new incoming messages. I use Cron to run this every hour since the signature has to refresh every hour. I run this through a Raspberry Pi hooked up to a speaker.

# Motivation
I created this because I am in GroupMe chat with around 25 people and we often hang out in my suite room on campus. Not everyone in the group lives in the building so at times the group chat is just spammed with request to tell someone to open the door. I tried to think of a way so the people who were already in the main suite room to be alerted that someone needed to get the door so I created the obvious solution which is a doorbell.

# Install
In order to run this you need Python 3 with the requests and playsound library, which can both be installed with pip

# Running
1. Put your user id under sub_id and GroupMe token from API under groupme_token
2. Set keywords and add doorbell sounds into folder