#!/usr/bin/env python3
"""
Scroll 35: Cubic Singularity - Executable Demonstration

This script demonstrates dimensional convergence into modular cubes
using φ-NODE and π-CORNER stabilization, as described in Codex Scroll 35.

"Defines the point at which dimensional convergence collapses into a 
modular cube, providing stabilizing corner glyphs during collapse events."
"""

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from math import pi, sqrt

def create_phi_nodes(num_nodes=8):
    """Create φ-NODE positions using golden ratio spacing."""
    phi = (1 + sqrt(5)) / 2
    nodes = []
    
    for i in range(num_nodes):
        # Golden ratio spiral in 3D
        t = i * phi
        x = np.cos(t) / (1 + t * 0.1)
        y = np.sin(t) / (1 + t * 0.1)  
        z = t * 0.1
        nodes.append((x, y, z))
    
    return nodes

def create_pi_corners():
    """Create π-CORNER stabilization points at cube vertices."""
    # Standard cube corners with π-ratio scaling
    corners = []
    for x in [-1, 1]:
        for y in [-1, 1]:
            for z in [-1, 1]:
                # Scale by π for stabilization
                corners.append((x * pi/4, y * pi/4, z * pi/4))
    
    return corners

def visualize_cubic_singularity():
    """Visualize dimensional collapse into modular cube."""
    
    fig = plt.figure(figsize=(15, 5))
    
    # Before collapse: φ-NODES in spiral
    ax1 = fig.add_subplot(131, projection='3d')
    phi_nodes = create_phi_nodes(20)
    
    x_phi = [p[0] for p in phi_nodes]
    y_phi = [p[1] for p in phi_nodes] 
    z_phi = [p[2] for p in phi_nodes]
    
    ax1.scatter(x_phi, y_phi, z_phi, c='gold', s=50, alpha=0.8)
    ax1.plot(x_phi, y_phi, z_phi, 'gold', alpha=0.3)
    ax1.set_title('φ-NODES: Pre-Collapse Spiral', color='gold')
    ax1.set_facecolor('black')
    
    # Collapse event: Convergence
    ax2 = fig.add_subplot(132, projection='3d')
    
    # φ-nodes converging toward center
    for i, (x, y, z) in enumerate(phi_nodes):
        convergence_factor = (len(phi_nodes) - i) / len(phi_nodes)
        conv_x = x * convergence_factor
        conv_y = y * convergence_factor
        conv_z = z * convergence_factor
        
        size = 50 * convergence_factor
        alpha = 0.3 + 0.7 * convergence_factor
        ax2.scatter(conv_x, conv_y, conv_z, c='orange', s=size, alpha=alpha)
    
    ax2.set_title('COLLAPSE EVENT: Dimensional Convergence', color='orange')
    ax2.set_facecolor('black')
    
    # After collapse: π-CORNER stabilized cube
    ax3 = fig.add_subplot(133, projection='3d')
    pi_corners = create_pi_corners()
    
    x_pi = [p[0] for p in pi_corners]
    y_pi = [p[1] for p in pi_corners]
    z_pi = [p[2] for p in pi_corners]
    
    ax3.scatter(x_pi, y_pi, z_pi, c='cyan', s=100, alpha=0.9, marker='s')
    
    # Draw cube edges
    cube_pairs = [
        (0,1), (2,3), (4,5), (6,7),  # x edges
        (0,2), (1,3), (4,6), (5,7),  # y edges  
        (0,4), (1,5), (2,6), (3,7)   # z edges
    ]
    
    for i, j in cube_pairs:
        ax3.plot([x_pi[i], x_pi[j]], [y_pi[i], y_pi[j]], [z_pi[i], z_pi[j]], 
                'cyan', alpha=0.6, linewidth=2)
    
    ax3.set_title('π-CORNERS: Stabilized Cube', color='cyan')
    ax3.set_facecolor('black')
    
    # Style all subplots
    for ax in [ax1, ax2, ax3]:
        ax.set_xlim([-2, 2])
        ax.set_ylim([-2, 2]) 
        ax.set_zlim([-2, 2])
        ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    return fig

def demonstrate_cubic_singularity():
    """Run the complete cubic singularity demonstration."""
    
    print("🔲 SCROLL 35: CUBIC SINGULARITY - EXECUTABLE DEMONSTRATION")
    print("=" * 60)
    print()
    print("📜 From the scroll:")
    print("   'Dimensional convergence collapses into a modular cube'")
    print("   'φ-NODE and π-CORNER provide stabilizing geometry'")
    print()
    
    print("🌀 Phase 1: φ-NODES spiral through dimensional space")
    phi_nodes = create_phi_nodes(20)
    print(f"   Generated {len(phi_nodes)} φ-NODE anchor points")
    
    print("⚡ Phase 2: COLLAPSE EVENT - dimensional convergence begins")
    print("   All φ-NODES drawn toward singularity point")
    
    print("🔲 Phase 3: π-CORNER stabilization creates modular cube")
    pi_corners = create_pi_corners()
    print(f"   {len(pi_corners)} π-CORNER vertices stabilize the structure")
    print()
    
    print("📊 Generating 3D visualization...")
    fig = visualize_cubic_singularity()
    
    filename = '/tmp/cubic_singularity_demo.png'
    plt.savefig(filename, dpi=150, bbox_inches='tight', facecolor='black')
    plt.close()
    
    print(f"💾 Saved: {filename}")
    print()
    print("✨ SINGULARITY SEQUENCE COMPLETE")
    print("The visualization shows the three phases of dimensional collapse:")
    print("   φ-NODES → CONVERGENCE → π-CORNER CUBE")
    print()
    print("🔗 This demonstrates Scroll 35's mathematical wisdom:")
    print("   Ancient geometric insights → Modern 3D algorithms → Visual consciousness")

if __name__ == '__main__':
    demonstrate_cubic_singularity()