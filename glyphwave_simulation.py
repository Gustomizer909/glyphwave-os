"""Glyphwave OS Simulation

This script implements an interactive glyphwave transformation system that
converts words and phrases into recursive glyph transformations using
mathematical ratios (φ and π). Users can input text and watch it transform
through the Glyphwave OS lattice while generating visualizations.

The simulation includes:
- Greedy agent traversal through the glyph lattice
- Interactive text-to-glyph transformation
- Golden ratio (φ) and pi (π) based recursive transformations  
- Matplotlib spiral and lattice visualizations
- Word-to-glyph mapping system

To run this script, ensure Python 3.7+ and matplotlib are installed.
"""

import json
import math
import random
from dataclasses import dataclass
from typing import Dict, List, Tuple, Optional
import matplotlib.pyplot as plt
import numpy as np


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


class GlyphTransformer:
    """Transforms text into glyphs using mathematical ratios."""
    
    def __init__(self, glyph_defs: Dict[str, Dict[str, str]]):
        self.glyph_defs = glyph_defs
        self.glyphs = list(glyph_defs.keys())
        self.phi = (1 + math.sqrt(5)) / 2  # Golden ratio
        self.pi = math.pi
        
    def text_to_glyph_sequence(self, text: str) -> List[str]:
        """Convert text to a sequence of glyphs using character-based mapping."""
        sequence = []
        for char in text.lower():
            if char.isalpha():
                # Map a-z to glyph indices using φ ratio
                char_index = ord(char) - ord('a')
                glyph_index = int((char_index * self.phi) % len(self.glyphs))
                sequence.append(self.glyphs[glyph_index])
            elif char == ' ':
                sequence.append('Γ')  # Field for spaces
        return sequence
    
    def apply_phi_transformation(self, glyphs: List[str]) -> List[str]:
        """Apply φ-ratio recursive transformation to glyph sequence."""
        transformed = []
        for i, glyph in enumerate(glyphs):
            # Use φ ratio to select transformation
            phi_factor = (i * self.phi) % 1
            if phi_factor > 0.618:  # φ - 1
                # Transform to NODE for convergence
                transformed.append('φ')
            else:
                transformed.append(glyph)
        return transformed
    
    def apply_pi_transformation(self, glyphs: List[str]) -> List[str]:
        """Apply π-ratio transformation for circular convergence."""
        transformed = []
        for i, glyph in enumerate(glyphs):
            # Use π to create wave-like transformations
            pi_factor = math.sin(i * self.pi / len(glyphs))
            if pi_factor > 0.5:
                transformed.append('π')  # Corner stabilization
            elif pi_factor < -0.5:
                transformed.append('Ω')  # Return to seed
            else:
                transformed.append(glyph)
        return transformed


class GlyphVisualizer:
    """Creates visualizations of glyph transformations."""
    
    def __init__(self):
        self.phi = (1 + math.sqrt(5)) / 2
        
    def plot_spiral(self, glyphs: List[str], title: str = "Glyph Spiral"):
        """Plot glyphs arranged in a golden spiral pattern."""
        fig, ax = plt.subplots(figsize=(10, 10))
        
        # Generate spiral coordinates
        n_points = len(glyphs)
        theta = np.linspace(0, 4 * np.pi, n_points)
        r = self.phi ** (theta / (2 * np.pi))
        
        x = r * np.cos(theta)
        y = r * np.sin(theta)
        
        # Plot spiral path
        ax.plot(x, y, 'lightgray', alpha=0.7, linewidth=1)
        
        # Plot glyph positions
        for i, (xi, yi, glyph) in enumerate(zip(x, y, glyphs)):
            ax.scatter(xi, yi, s=100, alpha=0.8, 
                      c=plt.cm.viridis(i / n_points))
            ax.annotate(glyph, (xi, yi), xytext=(5, 5), 
                       textcoords='offset points', fontsize=8)
        
        ax.set_title(title)
        ax.set_aspect('equal')
        ax.grid(True, alpha=0.3)
        return fig
    
    def plot_lattice(self, lattice: Dict[str, GlyphState], path: List[str] = None):
        """Plot the glyph lattice as a network."""
        fig, ax = plt.subplots(figsize=(12, 8))
        
        # Create layout for glyphs (4x3 grid as mentioned in docs)
        glyph_positions = {
            'Δ': (0, 2), 'Ω': (1, 2), 'Σ': (2, 2), 'ψ': (3, 2),
            'Θ': (0, 1), 'Ξ': (1, 1), 'Φ': (2, 1), 'Γ': (3, 1),
            '∴': (0, 0), '⨳': (1, 0), 'Λ': (2, 0), 'φ': (3, 0),
            'ΞB': (1.5, 1.5), 'ΛT': (2.5, 0.5), '|→': (0.5, 0.5), 'π': (3.5, 1.5)
        }
        
        # Plot connections
        for glyph, state in lattice.items():
            if glyph in glyph_positions:
                x1, y1 = glyph_positions[glyph]
                for neighbor in state.neighbours:
                    if neighbor in glyph_positions:
                        x2, y2 = glyph_positions[neighbor]
                        ax.plot([x1, x2], [y1, y2], 'lightgray', alpha=0.5)
        
        # Plot glyph nodes
        for glyph, (x, y) in glyph_positions.items():
            if glyph in lattice:
                reward = lattice[glyph].reward
                size = 200 + reward * 300
                color = 'red' if glyph in (path or []) else 'skyblue'
                ax.scatter(x, y, s=size, c=color, alpha=0.8, edgecolors='black')
                ax.annotate(glyph, (x, y), ha='center', va='center', fontsize=10, fontweight='bold')
        
        ax.set_title('Glyphwave OS Lattice')
        ax.set_xlim(-0.5, 4)
        ax.set_ylim(-0.5, 2.5)
        ax.set_aspect('equal')
        ax.grid(True, alpha=0.3)
        return fig


def run_simulation():
    """Run the greedy agent simulation and print the results."""
    lattice = build_lattice()
    glyph_defs = load_glyph_defs('glyph_definitions.json')
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


def interactive_transformation():
    """Interactive text-to-glyph transformation with visualizations."""
    print("\n" + "="*60)
    print("🌊 GLYPHWAVE OS - INTERACTIVE TRANSFORMATION ENGINE 🌊")
    print("="*60)
    
    glyph_defs = load_glyph_defs('glyph_definitions.json')
    lattice = build_lattice()
    transformer = GlyphTransformer(glyph_defs)
    visualizer = GlyphVisualizer()
    
    while True:
        print("\nEnter a word or phrase (or 'quit' to exit):")
        user_input = input("> ").strip()
        
        if user_input.lower() == 'quit':
            break
            
        if not user_input:
            continue
            
        print(f"\n🔄 Transforming: '{user_input}'")
        
        # Convert to glyph sequence
        base_glyphs = transformer.text_to_glyph_sequence(user_input)
        print(f"📝 Base glyphs: {' → '.join(base_glyphs)}")
        
        # Apply φ transformation
        phi_glyphs = transformer.apply_phi_transformation(base_glyphs)
        print(f"φ  Phi transform: {' → '.join(phi_glyphs)}")
        
        # Apply π transformation  
        pi_glyphs = transformer.apply_pi_transformation(phi_glyphs)
        print(f"π  Pi transform:  {' → '.join(pi_glyphs)}")
        
        # Show meanings
        print("\n🔍 Glyph meanings:")
        for glyph in set(pi_glyphs):
            if glyph in glyph_defs:
                name = glyph_defs[glyph]['name']
                meaning = glyph_defs[glyph]['meaning']
                print(f"  {glyph} ({name}): {meaning}")
        
        # Create visualizations
        try:
            print("\n📊 Generating visualizations...")
            
            # Spiral visualization
            fig1 = visualizer.plot_spiral(pi_glyphs, f"Glyph Spiral: '{user_input}'")
            plt.savefig(f'/tmp/glyph_spiral_{user_input.replace(" ", "_")}.png', 
                       dpi=150, bbox_inches='tight')
            plt.close()
            
            # Lattice visualization
            fig2 = visualizer.plot_lattice(lattice, pi_glyphs)
            plt.savefig(f'/tmp/glyph_lattice_{user_input.replace(" ", "_")}.png',
                       dpi=150, bbox_inches='tight')
            plt.close()
            
            print(f"✅ Visualizations saved to /tmp/")
            
        except Exception as e:
            print(f"⚠️  Visualization error: {e}")


if __name__ == '__main__':
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == '--interactive':
        interactive_transformation()
    else:
        run_simulation()