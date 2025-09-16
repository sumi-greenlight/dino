#!/usr/bin/env python3
"""
Animated ASCII Block-Style Walking Dinosaur
"""

import time
import os
import sys

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_terminal_width():
    """Get the width of the terminal."""
    try:
        return os.get_terminal_size().columns
    except:
        return 80  # fallback width

class WalkingDino:
    def __init__(self):
        self.position = 0
        self.frame = 0
        self.terminal_width = get_terminal_width()
        
        # Two frames for walking animation - block style ASCII art
        self.frames = [
            # Frame 1 - left foot forward
            [
                "                ████████████    ",
                "              ██            ██  ",
                "            ██                ██",
                "          ██      ████      ██  ",
                "        ██      ██    ██    ██  ",
                "      ██        ██    ██    ██  ",
                "    ██            ████      ██  ",
                "  ██                        ██  ",
                "██                          ██  ",
                "██    ████████████████████████  ",
                "██  ██                      ██  ",
                "██████                      ██  ",
                "██  ██                      ██  ",
                "██  ██                      ██  ",
                "██  ██                    ██    ",
                "██  ██████████████████████      ",
                "██                              ",
                "██                              ",
                "██      ██                      ",
                "██      ██                      ",
                "██    ████          ██          ",
                "██    ████          ██          ",
                "      ████          ████        ",
                "      ████          ████        "
            ],
            # Frame 2 - right foot forward  
            [
                "                ████████████    ",
                "              ██            ██  ",
                "            ██                ██",
                "          ██      ████      ██  ",
                "        ██      ██    ██    ██  ",
                "      ██        ██    ██    ██  ",
                "    ██            ████      ██  ",
                "  ██                        ██  ",
                "██                          ██  ",
                "██    ████████████████████████  ",
                "██  ██                      ██  ",
                "██████                      ██  ",
                "██  ██                      ██  ",
                "██  ██                      ██  ",
                "██  ██                    ██    ",
                "██  ██████████████████████      ",
                "██                              ",
                "██                              ",
                "██                ██            ",
                "██                ██            ",
                "██          ██    ████          ",
                "██          ██    ████          ",
                "            ████  ████          ",
                "            ████  ████          "
            ]
        ]
    
    def get_current_frame(self):
        """Get the current animation frame."""
        return self.frames[self.frame]
    
    def next_frame(self):
        """Advance to the next animation frame."""
        self.frame = (self.frame + 1) % len(self.frames)
    
    def move_forward(self):
        """Move the dinosaur forward."""
        self.position += 2
        # Reset position when dino walks off screen
        if self.position > self.terminal_width:
            self.position = -40  # Start from left side (dino width ~32 chars)
    
    def render(self):
        """Render the dinosaur at current position."""
        clear_screen()
        current_frame = self.get_current_frame()
        
        # Print some empty lines at top for better positioning
        print("\n" * 5)
        
        # Render each line of the dinosaur with proper spacing
        for line in current_frame:
            spaces = " " * max(0, self.position)
            print(spaces + line)
        
        # Print some info at bottom
        print(f"\n\nPress Ctrl+C to stop the animation")
        print(f"Position: {self.position}, Frame: {self.frame + 1}")

def main():
    """Main animation loop."""
    dino = WalkingDino()
    
    print("🦕 ASCII Block-Style Walking Dinosaur Animation! 🦕")
    print("Starting in 3 seconds...")
    time.sleep(3)
    
    try:
        while True:
            dino.render()
            dino.next_frame()
            dino.move_forward()
            time.sleep(0.3)  # Animation speed
            
    except KeyboardInterrupt:
        clear_screen()
        print("\n🦕 Thanks for watching the dinosaur walk! 🦕")
        print("Animation stopped.")

if __name__ == "__main__":
    main()