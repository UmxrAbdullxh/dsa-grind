# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview
LeetCode solution collection with 160 distinct problems solved in Python (160 solutions) and TypeScript (21 solutions). Each problem is a standalone file named `<number>.<slug>.<ext>`.

## Running Solutions
- **Python**: `python <filename>.py`
- **TypeScript**: `npx ts-node <filename>.ts`

No build system or test framework is configured; solutions are self‑contained scripts.

## Key Patterns
- Solutions often include a class (e.g., `MyHashSet`) or a function.
- File names follow the pattern `<problem‑number>.<kebab‑case‑slug>.<ext>`.
- When optimizing a solution, preserve the required class/function signature and add a brief comment describing the approach.

## Memory
User prefers succinct responses without trailing summaries. See memory files in `/home/umar/.claude/projects/-home-umar-code-sandbox-dsa-grind/memory/`.
