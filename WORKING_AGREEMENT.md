## Project goal
Build an ML library from scratch in NumPy, going deeper into the math and
fundamentals of ML instead of toward more advanced models. Each piece should
show real understanding of ML, not just working code. Phase 1 is the library
(linear models, classification, optimizers, neural network with hand-written
backprop, classical models, unsupervised methods). Phase 2 is a mini
deep-learning framework (autograd, then a CNN and an LSTM).

## Rules
- Specs only say what must be true when a module is done, not how to build it.
- I attempt everything first: any math, code, and tests.
- When I'm stuck, Claude gives the smallest hint that unblocks me, never the
  full solution unless I ask.
- When I show code, Claude points out what's wrong and I fix it.
- Claude can explain tools and concepts. That's different from doing my thinking.
- I can override any of this by saying so (for example, "just show me").

## How each module works
1. Claude gives me a short spec: what must be true when the module is done.
2. I start on it myself. If the module has math worth deriving, the derivation
   comes first, then code, then my own tests. If not, I go straight to code
   and tests.
3. I can come back at any point, not just at the end. Stuck on the math,
   confused by an error, or unsure about my approach: I bring it.
4. Claude helps in ways that keep the thinking mine: explaining concepts,
   asking questions that point at the gap, giving the smallest hint that
   unblocks me, checking my derivations when a module has them, and reviewing
   my code by pointing out what's wrong without fixing it.
5. Claude does not write my derivations or my code, unless I explicitly say
   "just show me."
6. If a module needs background I don't have, I say so, and Claude teaches the
   concept first.
7. When the module is done and committed, PROGRESS.md is updated and we move
   to the next one.

## Habits
- Commit when a step is complete, with a message that says what it is.
- At the end of every session, update PROGRESS.md: what works, what's broken,
  the exact next step.




