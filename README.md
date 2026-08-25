# Russian Roulette Simulator

A two-player Russian roulette game built with Pygame, where a single random integer decides the outcome — the first project in a personal exploration of how randomness and probability can be modeled and exploited in code.

## How It Works

Each "pull of the trigger" generates a random integer between 0 and 5 using NumPy, simulating the 1-in-6 odds of a single loaded chamber in a six-round revolver. The game state (alive/dead) updates based on whether the generated value matches the "loaded" outcome, with Pygame handling the UI, sprite rendering, and mouse-click input for firing.

## Why I Built This

This started as a simple UI/game-logic exercise, but it became the starting point for a broader interest: how do you take something that looks purely random on the surface and reason about it mathematically? A six-chamber revolver has fixed, calculable odds — every "shot" is really just a single random draw from a known probability space.

That question — how likely outcomes can be modeled, exploited, or restructured — is what led directly into two follow-up projects:
- **[Huffman Coding Compressor](link)** — using the *probability* of symbol frequency to build optimal, lossless compression
- **[Markov Chain Text Generator](link)** — using probability distributions over sequences to generate text

## Tech Stack

- Python
- Pygame (UI, rendering, input handling)
- NumPy (random number generation)

## What I'd Improve

With more time, I'd extend this to let the player choose the number of chambers and loaded rounds, then compare the theoretical probability against the actual simulated outcome frequency over many runs — turning the game itself into a small probability experiment rather than just a fixed 1-in-6 mechanic.

<img width="1275" alt="Screenshot 2025-01-25 at 9 29 34 PM" src="https://github.com/user-attachments/assets/3e022e3f-ddf0-4bac-a263-35ea61e797cb" />
<img width="1270" alt="Screenshot 2025-01-25 at 9 30 01 PM" src="https://github.com/user-attachments/assets/840aa7e5-0f0c-4f31-afea-29f19c71dece" />
