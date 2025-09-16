# 🦕 ASCII Walking Dinosaur

An animated block-style ASCII art dinosaur that walks across your screen! Perfect for embedding in websites, GitHub READMEs, or just enjoying some retro terminal vibes.

## 🚀 Live Demo

**GitHub Pages:** `https://yourusername.github.io/walking-dino`

## ✨ Features

- 🎬 **Smooth Animation** - Two-frame walking cycle with realistic gait
- 🎮 **Interactive Controls** - Play/pause, speed control, reset, fullscreen
- 📱 **Responsive Design** - Works on desktop, tablet, and mobile
- 🖼️ **Iframe Ready** - Easy to embed in any website
- ⌨️ **Keyboard Controls** - Space, S, R, F keys for control
- 🎨 **Retro Aesthetic** - Classic green-on-black terminal look
- 📋 **Copy Embed Code** - One-click embed code generation

## 🎮 Controls

| Action | Button | Keyboard |
|--------|--------|----------|
| Play/Pause | ⏯️ | `Space` |
| Speed Control | ⚡ | `S` |
| Reset Position | 🔄 | `R` |
| Fullscreen | 🔳 | `F` |
| Copy Embed | 📋 | - |

## 🛠️ Setup for GitHub Pages

### Quick Setup (Recommended)

1. **Fork this repository** or **create a new repository**
2. **Upload the `index.html` file** to your repository root
3. **Enable GitHub Pages**:
   - Go to repository Settings
   - Scroll to "Pages" section
   - Select "Deploy from a branch"
   - Choose "main" branch and "/ (root)"
   - Click "Save"
4. **Visit your site** at `https://yourusername.github.io/repositoryname`

### Manual Setup

```bash
# Clone or create your repository
git clone https://github.com/yourusername/walking-dino.git
cd walking-dino

# Add the index.html file (copy the content from this repo)
# Commit and push
git add index.html
git commit -m "Add walking dinosaur animation"
git push origin main
```

## 🔗 Embedding

### Basic Iframe
```html
<iframe src="https://yourusername.github.io/walking-dino" 
        width="800" 
        height="400" 
        style="border: none; background: #000;">
</iframe>
```

### Responsive Iframe
```html
<div style="width: 100%; height: 400px; background: #000;">
    <iframe src="https://yourusername.github.io/walking-dino" 
            width="100%" 
            height="100%" 
            style="border: none;">
    </iframe>
</div>
```

### With External Controls
```html
<iframe id="dinoFrame" src="https://yourusername.github.io/walking-dino" 
        width="800" height="400">
</iframe>
<button onclick="document.getElementById('dinoFrame').contentWindow.postMessage({action: 'toggle'}, '*')">
    Toggle Animation
</button>

<script>
function controlDino(action) {
    document.getElementById('dinoFrame').contentWindow.postMessage({action: action}, '*');
}
</script>
```

## 📱 Mobile Support

The animation automatically adapts to mobile devices with:
- Smaller font sizes for better fit
- Touch-friendly controls
- Responsive layout
- Optimized performance

## 🎨 Customization

You can easily customize the dinosaur by editing the `frames` array in the JavaScript:

```javascript
this.frames = [
    // Frame 1 - your custom ASCII art here
    `your custom dinosaur frame 1`,
    
    // Frame 2 - your custom ASCII art here  
    `your custom dinosaur frame 2`
];
```

## 🐍 Python Version

Want to run this in your terminal? Check out `walking_dino.py`:

```bash
python3 walking_dino.py
```

## 📋 File Structure

```
walking-dino/
├── index.html          # Main GitHub Pages file
├── walking_dino.html   # Standalone version
├── walking_dino.py     # Python terminal version
├── iframe_demo.html    # Embedding examples
└── README.md          # This file
```

## 🤝 Contributing

Feel free to:
- 🐛 Report bugs
- 💡 Suggest features  
- 🎨 Submit custom dinosaur designs
- 📖 Improve documentation

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🦕 Fun Facts

- The dinosaur uses Unicode block characters (█) for that authentic ASCII feel
- Two-frame animation creates the illusion of walking
- Originally inspired by the Chrome offline dinosaur game
- Works great in GitHub README files when hosted on GitHub Pages!

---

**⭐ Star this repo if you enjoyed the walking dinosaur!**

Made with 💚 and lots of █ blocks
