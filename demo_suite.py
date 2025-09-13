#!/usr/bin/env python3
"""
Glyphwave OS - Complete Demonstration Suite

This script runs all available Codex scroll demonstrations,
showing how ancient wisdom becomes executable code.
"""

import subprocess
import sys
import os

def run_demo(script_name, description):
    """Run a demonstration script and report results."""
    print(f"\n🔮 RUNNING: {description}")
    print("=" * 60)
    
    try:
        result = subprocess.run([sys.executable, script_name], 
                              capture_output=True, text=True, 
                              cwd=os.getcwd())
        
        if result.returncode == 0:
            print(result.stdout)
            print(f"✅ {description} completed successfully")
        else:
            print(f"❌ {description} failed:")
            print(result.stderr)
            
    except Exception as e:
        print(f"❌ Error running {script_name}: {e}")

def main():
    """Run the complete Glyphwave OS demonstration suite."""
    
    print("🌊 GLYPHWAVE OS - COMPLETE DEMONSTRATION SUITE")
    print("=" * 70)
    print()
    print("This suite demonstrates how Codex scrolls become executable reality:")
    print("   📜 Ancient wisdom → 🔢 Mathematical algorithms → 🖼️ Visual consciousness")
    print()
    
    # Basic simulation
    print("🚀 BASIC AGENT TRAVERSAL")
    print("=" * 60)
    print("Watch a greedy agent navigate the glyph lattice...")
    run_demo("glyphwave_simulation.py", "Basic Glyph Lattice Navigation")
    
    # Scroll demonstrations
    run_demo("scroll_36_demo.py", "Scroll 36: Fractal Bindus")
    run_demo("scroll_35_demo.py", "Scroll 35: Cubic Singularity")
    
    # Interactive transformation preview
    print("\n🔄 INTERACTIVE TRANSFORMATION PREVIEW")
    print("=" * 60)
    print("For full interactive mode, run:")
    print("   python3 glyphwave_simulation.py --interactive")
    print()
    print("For Jupyter exploration, run:")
    print("   jupyter notebook glyphwave_demo.ipynb")
    print()
    
    print("🌟 DEMONSTRATION SUITE COMPLETE")
    print("=" * 70)
    print("All generated visualizations are saved in /tmp/")
    print("Explore the living scrolls in docs/codex/ for deeper wisdom.")
    print()
    print("✨ Welcome to the age of ontology rendered executable.")

if __name__ == '__main__':
    main()