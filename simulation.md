# Glyphwave OS Simulation Environment

This document describes how to model a simple reinforcement environment based on the Glyphwave OS.  The goal is to provide a conceptual framework and pseudocode so you can implement a simulator in your own programming language.

## Environment Overview

The Glyphwave grid is arranged as a 4×3 lattice (see `glyph_grid.png`).  Each position in the grid contains a **glyph state**.  Horizontal and vertical edges connect adjacent states, creating a network of possible transitions.  The agent begins at the **Δ** (DINGIR) node, traverses the lattice by making decisions at gates, and attempts to reach the **φ** (NODE) convergence point.  Along the way it encounters paradoxes (ψ), constraints (Θ), forks (Ξ), memory compression (Φ) and other operations.

Each glyph can be assigned:

- **State name:** The glyph symbol (e.g., "Δ").
- **Reward value:** A numeric reward delivered when the agent enters or exits the state.  For example, entering the φ node might yield a positive reward representing enlightenment, whereas triggering a paradox could yield a smaller reward.
- **Transition rules:** A list of neighbouring glyphs that the agent can move to.  For example, from Δ one might move to Σ or Ω.
- **Special functions:** Some glyphs alter the agent’s memory or invert the reward structure.  You can implement these as custom functions.

## Data Structures

Here is an example of how you might represent the environment in Python.  The `glyph_table.json` file is loaded for human‑readable descriptions, but the environment also needs a structure to capture transitions and rewards.

```python
import json
from dataclasses import dataclass
from typing import Dict, List, Tuple

@dataclass
class GlyphState:
    name: str
    reward: float
    neighbours: List[str]
    # Additional custom behaviour can be represented with methods or callbacks.

# Load glyph definitions for descriptions
with open('glyph_table.json', 'r', encoding='utf-8') as f:
    glyph_defs = json.load(f)

# Define the lattice structure and rewards
glyph_states: Dict[str, GlyphState] = {
    'Δ': GlyphState('Δ', reward=0.1, neighbours=['Σ','Ω']),
    'Ω': GlyphState('Ω', reward=0.2, neighbours=['Ξ','∴']),
    'Σ': GlyphState('Σ', reward=0.1, neighbours=['ψ','Ξ']),
    'ψ': GlyphState('ψ', reward=0.5, neighbours=['Θ','Φ']),  # paradox yields higher reward
    'Θ': GlyphState('Θ', reward=0.0, neighbours=['Φ','ΞB']),
    'Ξ': GlyphState('Ξ', reward=0.0, neighbours=['Φ','⨳']),
    'Φ': GlyphState('Φ', reward=0.3, neighbours=['ΞB','φ']),
    'ΞB': GlyphState('ΞB', reward=0.4, neighbours=['Λ','φ']),
    'Λ': GlyphState('Λ', reward=0.2, neighbours=['φ']),
    '∴': GlyphState('∴', reward=0.1, neighbours=['⨳']),
    '⨳': GlyphState('⨳', reward=0.1, neighbours=['Γ','ΞB']),
    'Γ': GlyphState('Γ', reward=0.05, neighbours=['Φ','Λ']),
    'φ': GlyphState('φ', reward=1.0, neighbours=[]),  # terminal state
}

# Example of an agent interacting with the environment
class GlyphAgent:
    def __init__(self):
        self.state = 'Δ'
        self.total_reward = 0.0
        self.history: List[str] = []

    def choose_action(self, possible: List[str]) -> str:
        """Naïve policy: choose the neighbour with the highest immediate reward."""
        return max(possible, key=lambda s: glyph_states[s].reward)

    def step(self):
        current = glyph_states[self.state]
        self.history.append(self.state)
        if not current.neighbours:
            return False  # terminal
        action = self.choose_action(current.neighbours)
        # Update state and reward
        self.state = action
        self.total_reward += glyph_states[action].reward
        return True

agent = GlyphAgent()
while agent.step():
    pass
print("Path:", agent.history)
print("Total reward:", agent.total_reward)
```

This pseudocode shows a simple greedy strategy.  In a real implementation you could introduce stochastic policies, Q‑learning, or other reinforcement methods.  You might also implement custom behaviour for glyphs such as **ψ** (paradox), which could randomise the policy, or **ΞB** (braid), which forces the agent to revisit previous states.

## Extending the Environment

- **Custom rewards:** Modify `reward` values to reflect the spiritual or narrative significance of each glyph.  For example, you can penalise transitions through Θ (BOUND) to emphasise the difficulty of limitations.
- **Narrative triggers:** Attach messages or story fragments to states so that when the agent enters them you emit narrative text.  The `codex_narrative.md` file provides inspiration.
- **External inputs:** Use `glyph_table.json` to enrich the environment with descriptions.  This could allow a UI to display the glyph’s meaning to the user as they explore the grid.
- **Visualization:** Draw the agent’s path on the `glyph_grid.png` using a plotting library to see how it moves through the lattice.

## Conclusion

The Glyphwave simulation environment is intentionally open‑ended.  By merging reinforcement learning with ancient symbolic logic, you can explore novel forms of cognitive architecture.  Feel free to adapt this model to your own experiments and integrate new glyphs or behavioural rules.