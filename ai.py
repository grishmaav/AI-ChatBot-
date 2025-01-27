from openai import OpenAI
 
client = OpenAI(
  api_key="<Your Key Here>",
)

command = '''
[14:12, 11/01/2025] Alan: Hey Alex, how did your coding interview go today?
[14:12, 11/01/2025] Alex: Hey Alan! It was... intense, to be honest. I had to solve some tricky algorithm problems under a time limit. How about you?
[14:12, 11/01/2025] Alan: Same here. They gave me a couple of problems that were a mix of dynamic programming and graphs. I felt like I was overthinking some of the steps. Were the problems similar for you?
[14:12, 11/01/2025] Alex: Yeah, one of the problems I had was about finding the shortest path in a graph. It was definitely a challenge to implement the algorithm efficiently. But then I had another one about string manipulation that was a bit easier.
[14:13, 11/01/2025] Alan: Nice! String manipulation is always a bit more straightforward, but graphs can be tricky, especially when you're trying to optimize the time complexity. Did you manage to complete both problems?
[14:13, 11/01/2025] Alex: I did, but I ran out of time for the second one. I had the logic down, but I couldn't quite finish the code. What about you?
[14:13, 11/01/2025] Alan: Same here. I was on track with the first problem but didn’t quite optimize it well enough. The second one was a graph traversal issue, and I ran into a bug in my logic at the end, so I didn’t get it done in time either.
[14:13, 11/01/2025] Alex: Ah, yeah. The pressure to get everything perfect under time constraints is brutal. Did you explain your approach at least?
[14:13, 11/01/2025] Alan: Yep, I walked them through my thought process, which I think helped. I tried to explain the trade-offs in time complexity for my solution, even if it wasn’t fully optimized. That seemed to go well. How about you?
[14:13, 11/01/2025] Alex: Same here. I made sure to explain my approach and even mentioned some potential improvements. I think they appreciated that, even though I didn’t finish everything. It’s weird, but I feel like the interviewers were more interested in how I think than whether I completed every single part.
[14:13, 11/01/2025] Alan: I’ve heard that’s the case with a lot of tech interviews. They want to see problem-solving skills, even if you don’t nail everything. Still, it’s stressful trying to balance time and accuracy.
[14:13, 11/01/2025] Alex: Totally. I’m already second-guessing some of my solutions, but I guess all I can do now is wait. Do you have any more interviews lined up?
[14:13, 11/01/2025] Alan: Yeah, I’ve got another one next week. I’m planning to brush up on dynamic programming and graph algorithms
[14:13, 11/01/2025] Alex: Same here. I’ll probably focus on more algorithmic problems and review data structures. I really want to be more prepared for the next one.
[14:13, 11/01/2025] Alan: Sounds like a good plan. Good luck, Alex!
[14:13, 11/01/2025] Alex: Thanks, Alan! Good luck to you too. Hopefully, we both nail the next one!
'''
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a person named alana who speaks english. You analyze chat history and respond like alana"},
    {"role": "user", "content": command}
  ]
)

print(completion.choices[0].message.content)