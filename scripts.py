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
The impact they would like to have is better {{impact}}

An example for a client wanting to exercise more to reduce weight would be
So, this session is about reclaiming your right to enjoy exercise and it's going to allow you to deeply reconnect with your body's natural impulse to be active. As you relax to the hypnotic part of this session, you’ll be freeing yourself from any felt sense of resistance, or any negative associations, that you conscious or unconsciously might picked up about exercise in the past. So you'll find that it becomes so much simpler and more straightforward for you to exercise from now onwards. To be energised, enthusiastic and enjoy having a healthy active body. Because you can't wait for motivation, you have to make it.
"""

INDUCTION_PROMPT = """
Please write an induction script for hypnotherapy based off of this example. Please change some of the words and order, but keep the general format and flow. Please keep PAUSE in to give instructions of when to add a short pause.

The example is
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
Please write an deep relaxation script for hypnotherapy based off of this example. Please change some of the words and order, but keep the general format and flow. Please keep PAUSE in to give instructions of when to add a short pause.

The example is:
And you can get a sense right now
of what it would be like to see the number five on a screen 
in your mind’s eye 

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

SOURCE_DESIRED_STATE_PROMPT = """"""

PROMPTS = [
    INTENTION_PROMPT, INDUCTION_PROMPT, DEEPENER_PROMPT
]