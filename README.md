# **KRAM — Keyword Recognition And Matching AI**  
*A tiny, retro-style rule-based chatbot built for maximum expandability and peak old-terminal aesthetics.*


##  What is KRAM?
KRAM is a **lightweight, rule-based AI** that responds to users by detecting keywords and matching them to categories.  
It's designed to feel like an **old-school 90s terminal chatbot**, complete with ASCII art and simple logic that you can easily expand.

Think of it as:
- A **barebones AI for beginners**
- A sandbox for experimenting with keyword-based logic
- A nostalgia trip for anyone who loves old CLI aesthetics  
- A perfect base to learn AI interaction *without* touching machine learning

##  Features
- **Retro ASCII banner** straight out of the hacker basement era  
- **Keyword-based emotion and intent detection**  
- **Priority system** so serious inputs override memes  
- **Easily expandable categories** — add keywords in seconds  
- **Zero dependencies** except `random`  
- **MIT Licensed** (modify, fork, steal—your choice)  
- **Runs on any Python install** (even on a potato)

##  Why KRAM?
KRAM is perfect for:
- People who want an AI but don’t want to dive into LLMs yet  
- Students learning input handling and basic NLP logic  
- Developers who love retro or minimalist designs  
- Anyone who wants a chatbot they can fully understand and modify  
- Pixel-punk terminal enthusiasts  

KRAM is the opposite of modern bloated models — it’s **simple, readable, expandable**, and fully yours.

##  How It Works
KRAM scans your input, splits it into words, and matches them against keyword lists like:

keywords_negative
keywords_positive
keywords_aggressive
keywords_memes
keywords_greetings
...


The first category that matches (based on a priority list) determines the response.

This means **you can add a new personality, emotion, mood, or meme category in seconds.**

### Example of extending KRAM:
```python
keywords_angry = ["rage", "furious", "mad"]
responses["angry"] = ["Chill dude...", "Woah relax"]
priority_order.insert(1, "angry")
```

Done.
You just expanded KRAM.

Current Version

KRAM Barebones v1.0

*GUI version currently in development.*

Run It
```python
python KRAM.py
```
License

MIT License — do whatever you want, just give credits to the creator.


