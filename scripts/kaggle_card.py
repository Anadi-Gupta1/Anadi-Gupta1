import os
import kaggle
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
import requests
from datetime import datetime
import json

# Set up Kaggle credentials
kaggle_username = os.getenv("KAGGLE_USERNAME") or "anadiskt"
kaggle_key = os.getenv("KAGGLE_KEY") or "b485f80ad71307a1d0e2447573005104"

# Ensure kaggle directory exists and set up credentials
kaggle_dir = os.path.expanduser("~/.kaggle")
if not os.path.exists(kaggle_dir):
    os.makedirs(kaggle_dir)

# Create kaggle.json with credentials
kaggle_config = {
    "username": kaggle_username,
    "key": kaggle_key
}

kaggle_json_path = os.path.join(kaggle_dir, "kaggle.json")
with open(kaggle_json_path, "w") as f:
    json.dump(kaggle_config, f)

# Set proper permissions (on Unix-like systems)
try:
    os.chmod(kaggle_json_path, 0o600)
except:
    pass  # Windows doesn't need this

# Get Kaggle username
username = kaggle_username

try:
    # Fetch user data
    api = kaggle.api
    user = api.get_user(username)
    
    # Get competitions and datasets
    competitions = api.competitions_list(user=username)
    datasets = api.dataset_list(user=username)
    
    # Prepare data
    stats = {
        "Datasets": len(datasets) if datasets else 0,
        "Competitions": len(competitions) if competitions else 0,
        "Followers": getattr(user, 'followers', 0),
        "Following": getattr(user, 'following', 0)
    }
    
    # Create a more attractive visualization
    fig, ax = plt.subplots(figsize=(12, 8))
    fig.patch.set_facecolor('#f8f9fa')
    
    # Colors for bars
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']
    
    bars = ax.bar(stats.keys(), stats.values(), color=colors, alpha=0.8, edgecolor='white', linewidth=2)
    
    # Add value labels on bars
    for bar, value in zip(bars, stats.values()):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + max(stats.values()) * 0.01,
                f'{value}', ha='center', va='bottom', fontsize=14, fontweight='bold')
    
    # Styling
    ax.set_title(f'🏆 Kaggle Stats for @{username}', fontsize=20, fontweight='bold', pad=20)
    ax.set_ylabel('Count', fontsize=14, fontweight='bold')
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    ax.set_facecolor('#ffffff')
    
    # Remove top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#cccccc')
    ax.spines['bottom'].set_color('#cccccc')
    
    # Add timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M UTC")
    plt.figtext(0.99, 0.01, f'Last updated: {timestamp}', ha='right', fontsize=10, style='italic', alpha=0.7)
    
    plt.tight_layout()
    plt.savefig("kaggle.png", dpi=300, bbox_inches='tight', facecolor='#f8f9fa')
    plt.close()
    
    print(f"✅ Generated Kaggle stats for {username}")
    print(f"📊 Stats: {stats}")
    
except Exception as e:
    print(f"❌ Error fetching Kaggle data: {e}")
    # Create a fallback image
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.text(0.5, 0.5, f'Kaggle Stats\n@{username}\nData temporarily unavailable', 
            ha='center', va='center', fontsize=16, transform=ax.transAxes)
    ax.set_title('🏆 Kaggle Profile Stats', fontsize=20, fontweight='bold')
    plt.savefig("kaggle.png", dpi=300, bbox_inches='tight')
    plt.close()

# Update README
readme_path = "README.md"
kaggle_section = """
## 📊 Kaggle Stats

![Kaggle Stats](kaggle.png)

*Stats are automatically updated daily via GitHub Actions*
"""

try:
    with open(readme_path, "r", encoding='utf-8') as f:
        readme = f.read()
except FileNotFoundError:
    readme = f"# {username}'s GitHub Profile\n\nWelcome to my GitHub profile!"

# Check if Kaggle stats section already exists
if "## 📊 Kaggle Stats" not in readme and "![Kaggle Stats]" not in readme:
    readme += kaggle_section
    with open(readme_path, "w", encoding='utf-8') as f:
        f.write(readme)
    print("✅ Updated README.md with Kaggle stats section")
else:
    print("✅ Kaggle stats section already exists in README.md")
