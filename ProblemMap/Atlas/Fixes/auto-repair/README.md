# Auto Repair v1

🛠️ **Auto Repair v1** is the first structured extension layer built on top of the Atlas fix system.

This folder does **not** claim that fully autonomous repair is already solved.

What it does claim is simpler and more useful:

> the Atlas now has a clear path from  
> **route → first repair direction → repair planning architecture**

This folder exists to define that path clearly, safely, and in a way that can grow without breaking the current system.

---

## What Auto Repair means here

In this project, **auto repair** does **not** mean:

- an AI blindly changing prompts
- an AI guessing random fixes
- an AI claiming full root-cause closure by itself
- a magic one-shot repair engine

Instead, auto repair means:

> a structured repair layer that starts **after Atlas routing**
> and turns diagnosis into a controlled repair workflow

In practical terms, the intended flow is:

1. route the case with the Atlas  
2. identify the likely failure family and broken invariant  
3. choose the most appropriate first repair family  
4. generate a constrained repair plan  
5. validate whether the repair improved the case  
6. escalate, revise, or rollback if needed

So this folder is not a replacement for the Atlas.

It is a **next layer** that depends on the Atlas being correct first.

---

## Where this sits in the full system

The current system can be understood like this:

```text
Problem Map 3.0
→ Troubleshooting Atlas
→ Canonical Casebook
→ Atlas-to-AI Adapter
→ Fix Surface
→ Auto Repair
→ WFGY Deep Repair
