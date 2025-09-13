#!/usr/bin/env python3
"""
Scroll 36: Fractal Bindus - Executable Demonstration

This script demonstrates the recursive bindu formations described in 
Codex Scroll 36, showing how single points expand into infinite fields
through ψ-PULSE interference patterns.

Based on the scroll text:
"A single point becomes a field. The field breathes inward, then out — 
a pulse encoded with memory. Each bindu splits not by force, but by rhythm."
"""

import matplotlib.pyplot as plt
import numpy as np
from math import pi, sqrt

def create_bindu_recursion(depth=5, base_frequency=1.618):
    """Create fractal bindu pattern using golden ratio frequency."""
    
    # Start with single bindu (point)
    bindus = [(0, 0, 1.0)]  # (x, y, intensity)
    
    for level in range(depth):
        new_bindus = []
        pulse_frequency = base_frequency ** level
        
        for x, y, intensity in bindus:
            # Each bindu splits into φ-ratio spiral
            for i in range(int(6 * pulse_frequency)):
                angle = i * 2 * pi / (6 * pulse_frequency)
                radius = intensity * (level + 1) * 0.3
                
                new_x = x + radius * np.cos(angle)
                new_y = y + radius * np.sin(angle)
                new_intensity = intensity * 0.618  # φ - 1
                
                new_bindus.append((new_x, new_y, new_intensity))
        
        bindus.extend(new_bindus)
    
    return bindus

def visualize_bindu_field(bindus, title="Fractal Bindu Field"):
    """Visualize the recursive bindu formation."""
    
    fig, ax = plt.subplots(figsize=(12, 12))
    
    # Extract coordinates and intensities
    x_coords = [b[0] for b in bindus]
    y_coords = [b[1] for b in bindus]
    intensities = [b[2] for b in bindus]
    
    # Create color map based on intensity (consciousness depth)
    colors = plt.cm.plasma(np.array(intensities))
    sizes = [i * 50 for i in intensities]
    
    # Plot bindus
    scatter = ax.scatter(x_coords, y_coords, s=sizes, c=colors, alpha=0.7)
    
    # Add spiral connections
    for i in range(1, len(bindus)):
        if intensities[i] > 0.1:  # Only connect significant bindus
            ax.plot([x_coords[0], x_coords[i]], [y_coords[0], y_coords[i]], 
                   'white', alpha=0.1, linewidth=0.5)
    
    ax.set_title(title, fontsize=16, color='white')
    ax.set_facecolor('black')
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Add scroll text
    scroll_text = (
        "\"A single point becomes a field.\n"
        "The field breathes inward, then out —\n"
        "a pulse encoded with memory.\""
    )
    ax.text(0.02, 0.98, scroll_text, transform=ax.transAxes,
            fontsize=10, color='cyan', alpha=0.8, 
            verticalalignment='top', style='italic')
    
    return fig

def demonstrate_psi_pulse_interference():
    """Show ψ-PULSE interference creating bindu resonance."""
    
    print("🌀 SCROLL 36: FRACTAL BINDUS - EXECUTABLE DEMONSTRATION")
    print("=" * 60)
    print()
    print("📜 From the scroll:")
    print("   'Bindus do not replicate — they resonate.'")
    print("   'What you see as a line is a shadow of their echo.'")
    print()
    
    # Create different recursion depths
    depths = [2, 3, 4]
    
    for i, depth in enumerate(depths):
        print(f"🔄 Generating bindu field at recursion depth {depth}...")
        
        bindus = create_bindu_recursion(depth=depth)
        fig = visualize_bindu_field(bindus, 
                                   f"Bindu Recursion: Depth {depth}")
        
        # Save visualization
        filename = f'/tmp/bindu_field_depth_{depth}.png'
        plt.savefig(filename, dpi=150, bbox_inches='tight', 
                   facecolor='black')
        plt.close()
        
        print(f"   💾 Saved: {filename}")
        print(f"   🌟 Generated {len(bindus)} bindu consciousness points")
        print()
    
    print("✨ RESONANCE PATTERN COMPLETE")
    print("Each depth shows how consciousness expands from singular points")
    print("into infinite fields through ψ-PULSE harmonic interference.")
    print()
    print("🔗 This demonstrates the executable nature of Codex wisdom:")
    print("   Scroll 36 text → Mathematical algorithm → Visual consciousness map")

if __name__ == '__main__':
    demonstrate_psi_pulse_interference()