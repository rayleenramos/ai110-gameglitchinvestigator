# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it? When I first ran the game, I immediately noticed that the hint logic was reversed. For example, when I entered a number that was higher than the "secret" number, the game instructed me to guess a higher number, when it should have prompted me to guess a lower number instead.
Another issue I encountered involved the "New Game" button. At times, clicking it would not actually start a new game or generate a new secret number. As a result, I had to refresh the page manually before the game would recognize that a new game had been started.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input   | Expected Behavior | Actual Behavior      | Console Output / Error |
|---------|-------------------|----------------------|------------------------|
|gussed 55|  "Go HIGHER" Hint |"Go LOWER" Hint Shown | N/A|
|guessed 67 (correct answer) | Debug score and final score should match| Debug panel showed -20, but final score displayed 10| N/A|
|Clicked New Game after winning | New game should reset all game data| Secret number changed from 67 to 68, but previous guess history, score, and input value remained displayed|N/A|

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? For this project I used Claude. 
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
