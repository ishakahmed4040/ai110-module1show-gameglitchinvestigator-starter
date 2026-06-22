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

I used Claude Code (Claude Sonnet) as my main AI collaborator throughout this project. I used it directly inside VS Code to read the code, identify bugs, and help me fix them one at a time rather than all at once.

One example where the AI suggestion was correct was when I told it the game was ending too early on Normal difficulty. The AI pointed out that `st.session_state.attempts` was initialized to `1` instead of `0`, which meant one attempt was silently consumed before the player even guessed. I verified this by checking the Developer Debug Info panel in the running app — the attempt count started at 1 right away, which confirmed the AI's explanation was accurate.

One example where I had to push back was around the "You already won" bug. My first instinct was that the issue was with the `st.stop()` call blocking the game, but the AI traced the real cause to the `new_game` button not resetting `status`, `score`, or `history`. Once I tested it by clicking New Game after a win, the issue reproduced exactly as the AI described, so I accepted that explanation and we fixed all three missing resets together.

---

## 3. Debugging and testing your fixes

I decided a bug was really fixed when I could reproduce the exact broken behavior first, then confirm it was gone after the change. For example, with the hints bug I deliberately guessed higher than the secret and watched the wrong hint appear — then after fixing the swap in `check_guess`, I repeated the same guess and saw the correct hint. Seeing the broken state before and the correct state after gave me confidence the fix actually worked.

The most useful test I ran was the full pytest suite in `tests/test_game_logic.py`. I ran `pytest tests/test_game_logic.py -v` from the terminal and it collected 12 tests covering the hints direction, the score deduction logic, the difficulty ranges, and the correct-guess win detection. All 12 passed, which confirmed that the core logic functions were working correctly as pure Python — separate from any Streamlit UI behavior.

Yes, AI helped me design the tests. I described the bugs to Claude and it suggested what each test case should assert — for example, it pointed out that for the hints bug I should not just check the outcome string but also check that the message contains "LOWER" or "HIGHER", which is a more precise check than just checking "Too High". It also explained why the existing starter tests were failing (they compared the full tuple return value to a plain string) and showed me how to unpack the tuple first before asserting.

---

## 4. What did you learn about Streamlit and state?

The biggest thing I learned is that Streamlit reruns the entire Python script from top to bottom every single time the user clicks a button or types something. This caught me off guard at first because I expected it to behave more like a normal program that runs once and waits. If you store a variable normally inside the script, it gets reset to its default value on every rerun, which is why the game kept losing track of the secret number and attempts.

Session state (`st.session_state`) is how Streamlit remembers things across those reruns. I would explain it to a friend like this: imagine every time you click a button, the whole app restarts from scratch — but `st.session_state` is like a sticky note that survives each restart. You write values onto it once (using the `if "key" not in st.session_state` pattern) and they stay there until you explicitly change or delete them.

This is also what caused the "You already won" bug. When I clicked New Game, the script reset the secret and attempts, but `st.session_state.status` still said `"won"` from the previous game because nobody cleared it. Streamlit hit the status check at the top of the submit block, saw `"won"`, and stopped the game immediately. Once I understood how reruns and session state work together, that bug made complete sense.

---

## 5. Looking ahead: your developer habits

One habit I want to carry forward is fixing and documenting bugs one at a time instead of trying to fix everything at once. On this project I went through each bug individually, confirmed it was broken, applied the fix, and then moved on. That made it much easier to know exactly what changed and why each fix worked. I plan to use this same approach in future labs — isolate one problem, fix it, verify it, repeat.

One thing I would do differently next time is ask the AI to explain its reasoning before I accept a fix. A few times during this project I applied a change the AI suggested without fully understanding why it worked, and I only understood it after going back and reading the code again. Next time I will ask "why does this fix the bug?" before applying it, so I actually learn from each step rather than just copying the solution.

This project changed the way I think about AI-generated code because I used to assume that if the code ran without crashing, it was probably correct. Working through these bugs showed me that AI-generated code can run fine on the surface while having subtle logic errors hiding underneath — like the secret being cast to a string on even attempts, which looked harmless but silently broke wins half the time. Now I treat AI-generated code as a starting point that needs the same careful review I would give any other code..
