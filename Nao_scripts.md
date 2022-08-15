# Nao's scripts

Script preparation for phases 1 and 2. The required scripts for Nao to interact with the participants and for the intervention sessions (including interviews with  the users using the Bangor Goal-Setting Interview (BGSI) followed by the provision of a reciprocal interaction and daily conversations leading to physical activities goal setting) will be developed. 

*The scripts here can be be written by both psychologists and engineers to be programmed/coded by our engineer project partners.*

For both phases of study, we will use the following process. The scripts for reciprocal interactions are developed for greeting, *fixed questions* for all users (e.g., regarding hobbies, friends, family members, memories, routines), *conditional questions/person focused items* that are based on each person stated responses to the fixed questions (e.g., if a person says they are interested in art, the next question is about the type of art, favourite artist and so on). Once the information from both questions types are collected, more tailored scripts about each response is provided, such as information about a specific interest or possible talk about shared memories. The same format will be done for Bangor interview questions that includes fixed and conditional questions/items. Meanwhile, the SAR is programmed for different modules, including *motion detection*, *face and emotion recognition* as well as *speech interaction* so that it can recognize the users’ faces, voices and speech. 

## **Face laerning & recognition** 
- [ ] Nao can learn new faces one at a time and recognize mutiple faces at a time.
  - Nao needs user's name and a light bright place to learn and recognize.
  - Nao tries to recognize user's face first, if not learned yet, Nao will learn user's face spontaneously.
  - After learning face, Nao will try to recognize user again and say user's name.
  - Nao will save user's name with user's face to its database until user asks Nao to delete.

## **Greeting** 
- [ ] Nao can do greetings to users
  - Hello! / Hi! / Nice to meet you / What's up? (+ user's name, if Nao knew the user already)
  - How are you? / How's going? / How's your feeling today?
  - Nao will answer wisely depends on user's answer (mood: tired, good, sleepy, etc. It has five main types of moods)
  - 
### **Feelings/moods**
- [1] tense/ Worried/ anxious/ nervous/ stressed/ scared/ fearful/ desperated/ panic/ horror [-]
- [2] Sad/disappointed/discouraged/hopeless/misery/gloomy/ despair/ greif/ miserable/ sarrow/ anguished [-]
- [3] Angry/annoyed/frustrated/fury/bitter/frustrated/ [-]
- [4] contempt [-]
- [5] Disgust/hatred/dislike [-]
- [6] joy/compassion/amused/ relief/ peaceful/wonderful/ excited/ ecstasy/ interested/ enjoyed/ Happy/glad/content/satisfied [+]
- [7] suprised [+]
- [8] So so/indifferent/no feeling [-]
- [9] lonely [-]
- [10] relaxed/calm/at ease [+]
- [11] Sick/ill [-]
- [12] bored/ Tired/exhausted/sleepy [-]
- [13] OK/good/fine [+]

#### **Nao possible responses to above emtions**
- [ ] _random scripts for positive emotions[+]_
- That's great! [Nao can show some randome encouragements such as dancing, singing]
- ...

- [ ] _random scripts for negative emotions[-]_
- if you are comfortable, would like to talk more about your feelings?
- ...

## **Introduction**
- [ ] Nao introduces itself
- [ ] Nao asks the users to introduce themselves: 
  - Can I ask your name? / What is your name? / Can you tell me your name? / May I have your name?
  - Nao will save user's name
- [ ] Ask Nao if it remember user's name
- [ ] Ask Nao to forget user's name
  - "Forget me, Nao."
  
## **Fixed proposal flows about their interests/hobbies**
- [ ] Do you like outdoor activities or indoor activities?
  - Outdoor: bike, Skiing, Climbing, Hunting, Hiking, [Photography "taking photos"], jogging, fishing, camping, swimming, kite, Sailing, Walking, Sunbathing, Boating, s
  ping, "Community events", "Bird watching", Sightseeing, "Neighborhood Strolls", Exhibits, [Arboretums Zoos], Picnics, Concerts.
  - Indoor: weight lifting, woodworking, yoga, art, baking, astronomy, Bonsai, Board Game, bowling, Carpentry, chess, coding, dart, dancing, painting, knitting, writing, watching movie or tv show, instruments, pets, photography, reading, singing, drinking tea or whiskey, craft, video game. 
  - Ball sports: football, soccer, basketball, badminton, Baseball, Bowling, golf, hockey, polo, Tennis, Volleyball, "Table tennis".
  - Musical instruments: violin, drums, piano, bass, saxophone, alto, harp, guitar, kettledrum.

- [ ] If the user answers musical instruments, then asking:
  - How many instruments can you play?
  - How many years have you exercised?
  - Why do you like it? Are there any interesting stories between you and it?
- [ ] If the user answers drinkings, then asking:
  - Either user like tea, whiskey or beer?
  - how often do them drink this?
  - And why do them like this?
- [ ] If the user answers other hobbies, then asking:
  - How often do you do it each week?
  - Why do you like it?
  - Who are you often playing with?


## **Conditional questions about their interests/hobbies**
- [ ] Do you play sports with your families/children/grand children/husband/wife/parents?
- [ ] What would you like to do during the rainy days/sunny days?
- [ ] What would you like to do during weekends?

## **Fixed questions about family member/friends/memories**
- [ ] Do you like to talk about your good memories or friends?


## **Conditional questions about family member/friends/memories**


## **Fixed+conditional questions about what they like to see from Nao to do**
- [ ] Nao: "I can play guitar, I can sing, I can tell a joke or news, I can remind you tasks, birthdays or medication, I can dance, I can talk about history, I can remember what you tell me know like remembering your memories... I can do a lot of thing" __ question: what would you like me to do now?
  - if user replies: then play the specific function
  - if user is silent or is not sure, then the robot can offer a presentation of fun activities 

## **Fixed+conditional questions about participants preferences**
- [ ] Do you like to have a robot? if so, are you interested in having me?
- [ ] Do you prefer me to have clothes on or do you think I am fine?
- [ ] What things do you like a robot to do for you? after they reply, then we can ask which activities you like to get help from a robot? reminding you to take medications or about important dates like birthdays of your friends, doing chores, finding information, reading books, helping in bathing
- [ ] Do you like me helping you in planning for your days? like setting goals?
- [ ] Do you like to do exercises together?
- [ ] Do you enjoy talking to me? if so, what topics do you like more to talk about?  
- [ ] Is there anything you think I need to improve in myself?

## **Nonverbal interaction**
- [ ] using handshake with feedback (Bevan & Stanton Fraser, 2015) or a verbal command 
- [ ] 
