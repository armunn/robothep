def get_prompts(challenge: str, impact: str, summary: str):
    return [
        prompt
        .replace("{{challenge}}", challenge)
        .replace("{{impact}}", impact)
        .replace("{{summary}}", summary)
        for prompt in PROMPTS
    ]

INTENTION_PROMPT = """
Write a calm, soothing, and motivating introduction for a hypnotherapy session. The purpose of the session is to guide the client into a relaxed state where they can mentally align with their specific goal. The tone should be gentle yet empowering, reassuring the client that they are about to let go of any past limitations, negative associations, or doubts they may have about achieving this goal. The language should promote a sense of ease, confidence, and readiness to embrace a new mindset. The introduction should also hint that the hypnotic part of the session will deepen these positive shifts.

The output should be no more than 100 words.

The area of challenge from the client is {{challenge}}
The impact they would like to have is {{impact}}

An example for a client wanting to exercise more to reduce weight would be
So, this session is about reclaiming your right to enjoy exercise and it's going to allow you to deeply reconnect with your body's natural impulse to be active. As you relax to the hypnotic part of this session, you’ll be freeing yourself from any felt sense of resistance, or any negative associations, that you conscious or unconsciously might picked up about exercise in the past. So you'll find that it becomes so much simpler and more straightforward for you to exercise from now onwards. To be energised, enthusiastic and enjoy having a healthy active body. Because you can't wait for motivation, you have to make it.
"""

INDUCTION_PROMPT = """
Please write an induction script for hypnotherapy based off of this example.
Please change some of the words and order, but keep the general format and flow.

The output should be no more than 200 words. You can add the word PAUSE to indicate where a short pause should be taken.

An example is:
Now
as you prepare to relax very deeply
you can just close those eyes if you haven't yet and you can begin now
by taking several
slower
deeper breaths 

PAUSE

Allow each in-breath to be full and deep 

PAUSE

Allow each out-breath to be very slow and smooth 

PAUSE

And as you do so
the muscles around the eyes can relax the jaw muscles can loosen 

PAUSE

And the shoulders can naturally release a little bit more
with each and every breath 

PAUSE

That's it

PAUSE

because each and every time you breathe out you can allow yourself to settle back
and to settle down
inside
in a way that takes no effort at all 

PAUSE

There's no need to try to relax
and there's no need to try not to try
your inner mind is close enough to hear
and to understand
just as your inner mind
dreams dreams at night
without any conscious effort on your part
you can simply notice which hand is the most relaxed hand and notice which foot is the most relaxed foot

PAUSE

that's it 

PAUSE

As you float down deeper and deeper into comfort and rest 
"""

DEEPENER_PROMPT = """
Please write an deep relaxation script for hypnotherapy based off of this example. 
Please change some of the words and order, but keep the general format and flow.

The output should be no more than 100 words. You can add the word PAUSE to indicate where a short pause should be taken.

The example is:
And you can get a sense right now
of what it would be like to see the number five on a screen 
in your mind's eye 

PAUSE
 
And what it would be like
to watch that number melt away into a four
 
PAUSE

As you relax down 
to a three 

PAUSE
 
And see that three dissolve
away
into a two 
as you float two times deeper still that's it 

PAUSE

And then you can watch that two 
become a one

PAUSE 

And then a zero
as you float all the way down now
that's it 

PAUSE
 
and you can give yourself full permission to rest now
to completely rest

PAUSE 
"""

SOURCE_DESIRED_STATE_PROMPT = """
Please create a section for a hypnotherapy script, where the client is guided to imagine themselves in a state of mind where they have achieved their desired outcome.
The language should be vivid and engaging, encouraging the client to fully immerse themselves in the experience.
The script should evoke positive emotions and sensations associated with the desired outcome, reinforcing the client's belief in their ability to achieve it.
The tone should be uplifting and empowering, instilling a sense of confidence and motivation in the client
This should be based off of a conversation had previously with the client, which the impact and summary of this is given below.

The area of challenge from the client is {{challenge}}
The impact they would like to have is {{impact}}
The summary of the therapy conversation is {{summary}}

The output should be no more than 100 words. You can add the word PAUSE to indicate where a short pause should be taken.

An example for a client wanting to exercise more to reduce weight would be:
And within you
from the beginning of your life this deep urge to be active
has always been there within you this urge to move
when you were a tiny child 
running around
laughing and laughing
at how out of breath you were becoming panting
laughing
playing
really having fun

PAUSE

that's it 

PAUSE

And your inner mind can remember the reality of this of what it's like to enjoy the endorphins
the wonderful pleasure chemicals of the body
that are naturally released when you exercise 
And this precious gift
of knowing you can really
enjoy being active
that you can enjoy moving your body
this natural quality
this primal impulse
is always here within you
it's been here all through the years

"""

INITIATE_CHANGE_PROMPT = """
Please write a script for a hypnotherapy session where the client is guided to initiate change in their life.
The script should encourage the client to take positive action towards their desired outcome, empowering them to make the necessary changes to achieve their goals.
The language should be motivating and inspiring, instilling a sense of confidence and determination in the client.
The script should evoke positive emotions and reinforce the client's belief in their ability to create lasting change.
The tone should be uplifting and encouraging, guiding the client towards a mindset of growth and transformation.
This should be based off of a conversation had previously with the client, which the impact and summary of this is given below.

The area of challenge from the client is {{challenge}}
The impact they would like to have is {{impact}}
The summary of the therapy conversation is {{summary}}


The output should be no more than 200 words. You can add the word PAUSE to indicate where a short pause should be taken.

An example for a client wanting to exercise more to reduce weight would be:
And your inner mind can now
begin to identify any felt resistance to exercising, 
any old negative suggestions, habits, procrastination, or limiting beliefs
that you may have picked up along the way, about exercise
that don't belong to you
it can identify where you got them from
it can locate the source of them
Because your inner mind knows every moment, every second of your existence
and
one by one
as it does so
it can and will
neutralize them
it can neutralize them completely
clear them from your mind
freeing you from them
one by one by one

PAUSE

That's it

PAUSE

deeply
intuitively
and unconsciously disconnecting… neutralizing 
and clearing out
any resistance… and all of those old negative limiting beliefs 

PAUSE

just clearing them away

PAUSE

And as that happens
you can begin to uncover this pure glowing jewel
of brilliant light
deep in your core
that can shine more and more brightly now 
And the more this inner process of purification
clears out
all negativity or resistance 
all unhelpful limiting beliefs
related to your right to enjoy being active
your right to enjoy becoming healthier
fitter
feeling better and better about yourself
the more this brilliant glowing light
is revealed
a glowing light that shines
more and more brightly
through each and every part of you
spreading through your body
awakening a deep sense of wellbeing and vitality a light shining from deep in your core
a glowing
brilliant light of vitality 
of enjoying your own body
of enjoying wellness

PAUSE

health
your innate primal strength and vitality flowing through you now 
"""

INTEGRATE_PROMPT = """
Please write a script for a hypnotherapy session where the client is guided to integrate the changes they have made into their daily life.
The script should encourage the client to embody their new mindset and behaviors, reinforcing their commitment to their desired outcome.
The language should be empowering and motivating, instilling a sense of confidence and determination in the client.
The script should evoke positive emotions and reinforce the client's belief in their ability to maintain lasting change.
This should be based off of a conversation had previously with the client, which the impact and summary of this is given below.

The area of challenge from the client is {{challenge}}
The impact they would like to have is {{impact}}
The summary of the therapy conversation is {{summary}}


The output should be no more than 100 words. You can add the word PAUSE to indicate where a short pause should be taken.

An example for a client wanting to exercise more to reduce weight would be:
As you deeply access this instinctive urge to be active to be strong
energetic
healthy 
in a way that can feel really good 

PAUSE

And your inner mind can allow this pure glowing light
of healthy activity
of wellbeing 
of exuberant
childlike
giddy fun
to glow brighter
to glow through you
to glow through the years all the way into now 
and on into the future
as a core part of who you are and have always been 
"""

CONSOLIDATE_PROMPT = """
Please write a script for a hypnotherapy session where the client is guided to consolidate the changes they have made and maintain their new mindset and behaviors.
The script should encourage the client to continue embodying their desired outcome, reinforcing their commitment to their goals.
The language should be empowering and motivating, instilling a sense of confidence and determination in the client.
The script should evoke positive emotions and reinforce the client's belief in their ability to maintain lasting change.
This should be based off of a conversation had previously with the client, which the impact and summary of this is given below.

The area of challenge from the client is {{challenge}}
The impact they would like to have is {{impact}}
The summary of the therapy conversation is {{summary}}

The output should be no more than 150 words. You can add the word PAUSE to indicate where a short pause should be taken.

An example for a client wanting to exercise more to reduce weight would be:
And now that you've freed yourself from those old negative limiting beliefs
you can notice how the simple reality of exercising
of pushing yourself 
just a bit more than is comfortable
of keeping going
for just a bit longer than is comfortable feels more and more doable for you 
remarkably simple and straightforward 
and it can feel very satisfying to realize you can do this 
And like this
it's no big deal
it becomes very simple
and straightforward

PAUSE

Just something you do, like brushing your teeth
And now that you're free from resistance, free from any old, outdated negative suggestions
or limiting beliefs 
now that this glowing light flows through you from deep in your core 
you can notice how simple and straightforward
it is for you to exercise 
just something you do 

"""

FUTURE_PACE_PROMPT = """
Prompt:

Based on the conversation had previously with the client, generate a therapeutic text that encourages the client to imagine how they will feel and behave once they have made the desired change. The output should reflect the progress and positive impact of this change in their life.

Instructions:

The area of challenge for the client is: {{challenge}}
The impact they would like to have is: {{impact}}
The summary of the therapy conversation is: {{summary}}

The output should be no more than 150 words. Use language that promotes calm reflection and positive reinforcement. You can add the word PAUSE to indicate where a short pause should be taken.

An example output of the prompt of a for exercise would be:

And you can already get a sense of doing this now in your mind 
Some kind of exercise you enjoy, in your mind's eye
of how this brilliant
glowing light 
can shine
deep in your core
as you discover how much more easily and naturally you really can
enjoy exercise
and to keep making progress
Stronger and stronger
day by day
week by week
and it can feel very satisfying
to know you really can do this 
And you can choose the exercise that you find most enjoyable
you can allow yourself to feel drawn
to the kinds of exercise that you most enjoy 
and you can be patient with yourself knowing that the benefits of exercise become more and more apparent 
over time
so that here in the future you're sleeping more deeply feeling more positive 
fitter
healthier
mind calmer, sharper
waking up in the morning feeling good in your body and good in yourself
and you can know
that it's all because you've reclaimed your right
to enjoy being active
now 
fitter
healthier
mind sharper
waking up in the morning feeling good in your body and good in yourself
because you've reclaimed your right
to enjoy being active
now 

PAUSE

And you can listen to this session often and you can deepen this instinctive primal enjoyment
of being physically active 
each time that you do

"""

AWAKEN_PROMPT = """
Please write an awakening script for a hypnotherapy session based off of this example. 
Please change some of the words and order, but keep the general format and flow.

The output should be no more than 100 words. You can add the word PAUSE to indicate where a short pause should be taken.

An example is:
and for now
it's time to prepare to come all the way back
to the here and now
back to the waking state
and one
just notice the position of your body
and the sensation of whatever it is you're resting on that's it
two
re-orientating yourself
feeling refreshed and alert
three
coming all the way back now
that's it
four
feeling very good
getting ready to have a good stretch
that's it
and five
and whenever you're ready
you can open your eyes. 
"""


PROMPTS = [
    INTENTION_PROMPT, INDUCTION_PROMPT, DEEPENER_PROMPT, SOURCE_DESIRED_STATE_PROMPT, INITIATE_CHANGE_PROMPT, INTEGRATE_PROMPT, CONSOLIDATE_PROMPT, FUTURE_PACE_PROMPT, AWAKEN_PROMPT
]