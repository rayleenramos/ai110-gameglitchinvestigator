# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
When I first ran the game, I immediately noticed that the hint logic was reversed. For example, when I entered a number that was higher than the "secret" number, the game instructed me to guess a higher number, when it should have prompted me to guess a lower number instead.
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

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
For this project I used Claude.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
The AI noticed that the high/low hints in check_guess were swapped, it told players to "Go HIGHER!" when their guess was too high. It suggested flipping them, and I verified the fix by writing a test that checks a too-high guess says "LOWER" and a too-low guess says "HIGHER," which passed.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
The AI changed my tests to match its code instead of keeping the simpler design where check_guess returns just "Win". I caught this by noticing the original test assert result == "Win" would have failed against the tuple, showing the AI fixed the tests the easy way rather than the right way.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I decided a bug was really fixed when I had a test that failed against the old buggy code but passed against the new code. For the high/low bug, just seeing the game "look right" wasn't enough, I made sure a pytest case specifically checked the corrected behavior and passed.

- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
I ran test_hint_direction_matches_guess using pytest. It checked that a guess of 80 against a secret of 50 returns "Too High" with a message saying LOWER, and that a guess of 20 returns "Too Low" saying HIGHER. It passed, which showed me the hint messages now point the player in the correct direction instead of the swapped one.

- Did AI help you design or understand any tests? How?
Yes. The AI suggested adding negative assertions, not just positive ones. This helped me understand that a good regression test should fail on the old bug, checking only that the message says "LOWER" wasn't enough, because I also needed to confirm it doesn't also say "HIGHER." That made the test a real safeguard against the bug coming back.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Every time a user clicks a button or interacts with the app, Streamlit re-runs the entire Python script from top to bottom, like refreshing the page, but faster. Session state is like a small notebook Streamlit keeps on the side; it saves specific values so they survive each rerun instead of resetting to zero every time.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
One habit I want to reuse is testing state changes explicitly after every interactive action, since UI bugs in stateful apps rarely show up in normal linear testing.

- What is one thing you would do differently next time you work with AI on a coding task?
Next time I work with AI on a coding task, I would give it more context upfront, like the full file and what the expected behavior is, instead of asking about isolated snippets, which leads to fixes that don't account for how the pieces connect.

This project made me realize that AI-generated code can look correct without actually being correct, it passes a surface-level read but breaks under real usage, so treating it like code from any other source that needs testing is the right mindset.
