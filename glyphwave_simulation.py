"""Glyphwave OS Simulation

This script implements a simple greedy agent that traverses the
Glyphwave OS lattice defined in ``simulation.md``.  It loads
glyph definitions from ``glyph_table.json`` to enrich the output.

The agent starts at the Δ (DINGIR) state and repeatedly chooses
the neighbouring state with the highest immediate reward.  It
accumulates rewards until it reaches the terminal φ state.  At
the end of the run it prints the path taken, showing for each
glyph the symbol, its descriptive name, and meaning from the
glyph table.  This provides a quick demonstration of how a
reinforcement agent might navigate the symbolic lattice.

To run this script, execute it in the directory containing
``glyph_table.json`` and ensure Python 3.7+ is installed.
"""

import json
from dataclasses import dataclass
from typing import Dict, List


@dataclass
class GlyphState:
    """Represents a state (glyph) in the lattice."""
    name: str
    reward: float
    neighbours: List[str]


def load_glyph_defs(path: str) -> Dict[str, Dict[str, str]]:
    """Load glyph definitions from a JSON file.

    Args:
        path: Path to the JSON file containing glyph definitions.

    Returns:
        A mapping from glyph symbol to a dictionary with fields like
        ``name``, ``meaning`` and ``origin``.
    """
    # Resolve the path relative to this script so it works when run from any directory
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(script_dir, path)
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def build_lattice() -> Dict[str, GlyphState]:
    """Define the lattice structure and reward values.

    This mirrors the example provided in ``simulation.md``.

    Returns:
        A mapping from glyph symbol to a ``GlyphState`` instance.
    """
    return {
        'Δ': GlyphState('Δ', reward=0.1, neighbours=['Σ', 'Ω']),
        'Ω': GlyphState('Ω', reward=0.2, neighbours=['Ξ', '∴']),
        'Σ': GlyphState('Σ', reward=0.1, neighbours=['ψ', 'Ξ']),
        'ψ': GlyphState('ψ', reward=0.5, neighbours=['Θ', 'Φ']),
        'Θ': GlyphState('Θ', reward=0.0, neighbours=['Φ', 'ΞB']),
        'Ξ': GlyphState('Ξ', reward=0.0, neighbours=['Φ', '⨳']),
        'Φ': GlyphState('Φ', reward=0.3, neighbours=['ΞB', 'φ']),
        'ΞB': GlyphState('ΞB', reward=0.4, neighbours=['Λ', 'φ']),
        'Λ': GlyphState('Λ', reward=0.2, neighbours=['φ']),
        '∴': GlyphState('∴', reward=0.1, neighbours=['⨳']),
        '⨳': GlyphState('⨳', reward=0.1, neighbours=['Γ', 'ΞB']),
        'Γ': GlyphState('Γ', reward=0.05, neighbours=['Φ', 'Λ']),
        'φ': GlyphState('φ', reward=1.0, neighbours=[]),
    }


class GlyphAgent:
    """A simple greedy agent for the Glyphwave lattice."""

    def __init__(self, lattice: Dict[str, GlyphState]):
        self.lattice = lattice
        self.state = 'Δ'
        self.total_reward: float = 0.0
        self.history: List[str] = []

    def choose_action(self, possible: List[str]) -> str:
        """Choose the neighbour with the highest immediate reward.

        Args:
            possible: A list of neighbouring glyph symbols.

        Returns:
            The symbol of the chosen neighbour.
        """
        return max(possible, key=lambda s: self.lattice[s].reward)

    def step(self) -> bool:
        """Perform one step: move to a neighbour and accumulate reward.

        Returns:
            False if the current state is terminal (no neighbours), True otherwise.
        """
        current = self.lattice[self.state]
        self.history.append(self.state)
        if not current.neighbours:
            return False  # terminal state
        action = self.choose_action(current.neighbours)
        self.state = action
        self.total_reward += self.lattice[action].reward
        return True


def run_simulation():
    """Run the greedy agent simulation and print the results."""
    lattice = build_lattice()
    glyph_defs = load_glyph_defs('glyph_table.json')
    agent = GlyphAgent(lattice)
    # Traverse until terminal state
    while agent.step():
        pass
    # Print the path with descriptive information
    print("Glyphwave OS Simulation Result")
    print("Path:")
    for symbol in agent.history:
        defs = glyph_defs.get(symbol, {})
        name = defs.get('name', 'Unknown')
        meaning = defs.get('meaning', 'No description')
        reward = lattice[symbol].reward
        print(f"  {symbol}: {name} - {meaning} (reward={reward})")
    print(f"Total reward accumulated: {agent.total_reward}")


if __name__ == '__main__':
    run_simulation()