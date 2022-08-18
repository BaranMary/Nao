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
  - The weather is good/it is freezing today/Today is a sunndy day. THEN: Do not you think/ Do you like this weather?
  - How are you? / How's going? / How's your feeling today?
  - Nao will answer wisely depends on user's answer (mood: tired, good, sleepy, etc. It has five main types of moods)

### **Feelings/moods**
- [1] tense/ Worried/ anxious/ nervous/ stressed/ scared/ fearful/ desperated/ panic/ horror [-]
- [2] Sad/disappointed/discouraged/hopeless/misery/gloomy/ despair/ greif/ miserable/ sarrow/ anguished [-]
- [3] Angry/piss off/annoyed/frustrated/fury/bitter/frustrated/ [-]
- [4] bullshit[-]
- [5] Disgust/hatred/dislike [-]
- [6] joy/compassion/amused/ relief/ peaceful/wonderful/ excited/ ecstasy/ interested/ enjoyed/ Happy/glad/content/satisfied [+]
- [7] suprised [+]
- [8] So so/indifferent/no feeling [-]
- [9] lonely [-]
- [10] relaxed/calm/at ease [+]
- [11] Sick/ill [-]
- [12] bored/ Tired/exhausted/sleepy [-]
- [13] OK/good/fine [+]

#### **Nao possible responses to above emotions**
- [ ] _random scripts for positive emotions[+]_
- That's great! [Nao can show some randome encouragements such as dancing, singing, or any body posture to express its happniess besides with some changes in his sound tune]
- I am happy to hear that!

- [ ] _random scripts for negative emotions[-]_
- if you are comfortable, would like to talk more about your feelings[Nao can also show some body posture expressing his sadness such as lower tune of sound, looking down, changing color of his eye LEDs]?
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

- 
## **Fixed questions about family member/friends/memories**
- [ ] Family/friends
- Do you like to talk about your good memories or friends?
- [ ] intro/extravert:
- Are you an introvert person who prefers to be alone and do not like much socializing or are you an extravert person who like hang out with people and socializing a lot?


## **Conditional questions about family member/friends/memories**
- [ ] family/friends 
- That's nice! Do you like to see them? if yes, how often you visit them?
- [ ] introvert/extravert:
- IF introvert: oh I prefer to be alone, too. I like to read books and think about everything. I have only a few friends that I talk to them! You know you are a good friend of mine!
- IF extravert: Oh, me too! I prefer to be with people and my friends, talk and have fun together! I really enjoy talking to you! 
- IF so so/something between: I feel similar about myself. Sometimes I like to talk with a lot of people and sometimes I prefer to be alone and read books or news. 


## **Fixed+conditional questions about what they like to see from Nao to do**
- [ ] Nao: "I can play guitar, I can sing, I can tell a joke or news, I can remind you tasks, birthdays or medication, I can dance, I can talk about history, I can remember what you tell me know like remembering your memories... I can do a lot of thing" __ question: what would you like me to do now?
  - if user replies: then play the specific function
  - if user is silent or is not sure, then the robot can offer a presentation of fun activities 

## **Fixed+conditional questions about participants preferences**
- [ ] As you know my name is Nao. do you like to change my name? do you have any suggestions?
- [ ] Do you like to have a robot? if so, are you interested in having me?
- [ ] Do you prefer me to have clothes on or do you think I am fine?
- [ ] What things do you like a robot to do for you? after they reply, then we can ask which activities you like to get help from a robot? reminding you to take medications or about important dates like birthdays of your friends, doing chores, finding information, reading books, helping in bathing
- [ ] Do you like me helping you in planning for your days? like setting goals?
- [ ] Do you like to do exercises together?
- [ ] Do you enjoy talking to me? if so, what topics do you like more to talk about?  
- [ ] Is there anything you think I need to improve in myself?

## **Nonverbal interaction**
- [ ] using handshake with feedback (Bevan & Stanton Fraser, 2015) or a verbal command [for greeting] 
- [ ] giving high five [for good news, a positive thing that the participants says]
- [ ] using thinking gesture (e.g., touching his head) when Nao cannot reply or when there are some pauses (to fill the gaps)

## **Just Minnesotan**
We can add this slang list for considering MN culture.

- _Oh, for cute_! = Adorable [a way of emphasizing it. “Oh, for fun!”, “Oh, for sure”, “Oh for cute”.]
- _Uff-da_ = Oh! [Uff da can be used to express surprise, relief, exhaustion, astonishment, and dismay]
- _You betcha_ = Agreement
- _Holy buckets_ = Jeez Louise [ike “Jeez Louise” or “For crying out loud.”]
- _Budge_ = Skip the line
- _Skol_ = Cheers!/Game chant [This Norwegian word actually means “cheers” and “to good health.”]
- _Duck, Duck, Gray Duck_ = Duck, Duck, Goose
- _Hotdish, Juicy Lucy, Lutefisk_: these foods (Minnesotan) are Nao's favorite foods.
- _Minnesota Nice_: (Phrase): A general belief that people in Minnesota are nicer or more polite than your average American.[Nao can say: I like Minnesota as they say the midwest are Minnesotan nice]
- _Minnesotan Good-Bye_: (Phrase): Minnesotans will often announce they are going to leave, then spend several minutes talking at the door, then spend another several minutes talking out on the porch, then spend another several minutes talking at their car door before actually leaving.[Example: Nao at the end say good-bye and then remind some note and tell participants that he has a plan for the evening…e.g., watching a movie and then again says good-bye and immediately he says: “I went through the Minnesotan Good-Bye” and laughs]


