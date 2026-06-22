# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input Used | Expected Behavior | Actual Behavior | Console Error / Output |
|------------|-------------------|-----------------|------------------------|
| Guess of 60 (secret number is 40) | "Go LOWER" hint displayed | "Go HIGHER" hint shown — hint direction is backwards | none |
| Starting a new game on Easy difficulty (range 1–20) | Hint shows "Guess a number between 1 and 20" | Hint always shows "Guess a number between 1 and 100" regardless of difficulty | none |
| Playing 7 rounds on Normal difficulty without winning | Game should allow up to 8 attempts before ending | Game ends after only 7 attempts — attempts counter starts at 1 instead of 0 | none |
| Entering the correct number after a previous win, then clicking New Game and guessing correctly | Fresh game starts, correct guess shows win screen | "You already won" message appears immediately — status never resets on New Game | none |
| Entering the correct answer on the 2nd, 4th, or 6th attempt | "You guessed it!" and win screen | Guess never registers as correct on even-numbered attempts — secret is converted to a string so integer comparison always fails | none |
| Guessing too high on the 2nd attempt (even attempt) | Score stays the same or decreases | Score increases by +5 — wrong guesses should never award points | none |
| Selecting Hard difficulty | Harder game with a wider range than Normal (1–100) | Hard uses range 1–50, which is actually easier than Normal — difficulty levels are misconfigured | none |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
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
