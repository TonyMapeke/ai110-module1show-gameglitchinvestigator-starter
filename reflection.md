# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

  Attempts are broken and doesn't reset after a win
  The ranges for easy, medium, hard don't work properly and doesn't enforce the respective range
  The hint is wrong sometimes and tells me to go higher/lower incorrectly
  

- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

  hints were backwards
  attempts didn't reset after a win
---

## 2. How did you use AI as a teammate?
I used AI to help solve bugs once I was able to identify them

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Claude Code
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
The AI suggested I reset attempts to 1 not 0 and when I did that and tested the code it worked
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
N/A
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
If it passed all of test cases
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?


---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
