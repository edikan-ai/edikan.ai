#!/usr/bin/env python3
"""
Generate ALL remaining blog posts for edikan.ai
"""

import os

def create_post(num, filename, title, date, focus, languages=[]):
    """Create a complete blog post with industrial focus"""
    
    # Language-specific code examples
    code_examples = {
        'python': '# Python implementation\nimport numpy as np\nimport pandas as pd',
        'sql': '-- SQL query example\nSELECT * FROM sensor_readings\nWHERE temperature > 1500',
        'matlab': '% MATLAB code\nA = [1 2; 3 4];\nB = inv(A);',
        'r': '# R statistical analysis\ndata <- read.csv("sensors.csv")\nsummary(data)',
        'julia': '# Julia high-performance computing\nusing DataFrames\nusing Statistics',
        'cpp': '// C++ for real-time systems\n#include <vector>\n#include <algorithm>',
        'rust': '// Rust for safe systems programming\nfn main() {\n    let readings = vec![1500, 1502, 1498];\n}'
    }
    
    lang_section = ""
    if languages:
        lang_section = "<h3>Multi-Language Implementation</h3>\n"
        for lang in languages:
            if lang in code_examples:
                lang_section += f'<div class="code-block">{code_examples[lang]}\n// {lang.upper()} specific implementation</div>\n'
    
    template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - edikan.ai</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; line-height: 1.8; color: #333; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); min-height: 100vh; }}
        .container {{ width: 100%; max-width: 800px; margin: 0 auto; padding: 15px; }}
        article {{ background: white; border-radius: 10px; padding: 40px; margin: 20px 0; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }}
        .post-header {{ border-bottom: 2px solid #f0f0f0; padding-bottom: 20px; margin-bottom: 30px; }}
        h1 {{ color: #333; margin-bottom: 10px; font-size: 2.2rem; line-height: 1.3; }}
        h2 {{ color: #667eea; margin: 35px 0 20px; font-size: 1.6rem; }}
        h3 {{ color: #333; margin: 25px 0 15px; font-size: 1.3rem; }}
        .post-meta {{ color: #999; font-size: 0.9em; }}
        .code-block {{ background: #2d2d2d; color: #f8f8f2; padding: 20px; border-radius: 8px; overflow-x: auto; margin: 20px 0; font-family: 'Courier New', monospace; white-space: pre; }}
        .personal-story {{ background: #f8f9fa; border-left: 4px solid #667eea; padding: 20px; margin: 25px 0; font-style: italic; }}
        .exercise-box {{ background: #f0f8ff; border: 2px solid #667eea; border-radius: 8px; padding: 25px; margin: 30px 0; }}
        .truth-bomb {{ background: #fff3cd; border: 1px solid #ffc107; border-radius: 8px; padding: 20px; margin: 25px 0; }}
        .next-post {{ background: #667eea; color: white; padding: 20px; border-radius: 8px; margin-top: 40px; text-align: center; }}
        .next-post a {{ color: white; text-decoration: none; font-weight: bold; }}
    </style>
</head>
<body>
    <div class="container">
        <article>
            <div class="post-header">
                <h1>{title}</h1>
                <div class="post-meta">
                    {date} • 12 min read • Part {num} of Industrial AI Mastery
                </div>
            </div>
            
            <div class="post-content">
                <div class="personal-story">
                    <strong>[YOUR STORY - {focus.upper()} PLACEHOLDER]</strong>
                    <p>Add your personal experience with {focus}. What specific incident happened? What was the cost/impact? How did you feel?</p>
                </div>

                <h2>The Problem</h2>
                <p>Working in industrial systems, {focus} became a critical issue when...</p>
                
                <div class="personal-story">
                    <strong>[SPECIFIC INCIDENT PLACEHOLDER]</strong>
                    <p>Describe the exact moment things went wrong. Include details: time, place, system affected, people involved.</p>
                </div>

                <h2>What I Didn't Understand</h2>
                <p>The fundamental concepts I was missing...</p>
                
                <div class="code-block"># Example of what I was doing wrong
# [CODE PLACEHOLDER - Add your actual buggy code]
def my_broken_function():
    pass  # This caused problems because...</div>

                <h2>The Industrial Impact</h2>
                <p>In a steel mill or industrial setting, this translates to...</p>
                
                {lang_section}

                <h2>The Exercise</h2>
                <div class="exercise-box">
                    <h3>Hands-On Challenge: {focus.title()}</h3>
                    <p>Build a solution for this industrial scenario:</p>
                    <div class="code-block"># Your challenge:
# 1. Read sensor data from multiple sources
# 2. Process using correct {focus} concepts
# 3. Output actionable insights
# NO AI HELP - work through it yourself!</div>
                </div>

                <h2>What Finally Clicked</h2>
                <div class="truth-bomb">
                    <strong>The Revelation:</strong> Understanding {focus} meant realizing that...
                    <br><br>
                    <strong>Key Takeaways:</strong>
                    <ul>
                        <li>Concept 1 that changed everything</li>
                        <li>Concept 2 that I wish I knew earlier</li>
                        <li>Concept 3 that prevents future disasters</li>
                    </ul>
                </div>

                <div class="personal-story">
                    <strong>[YOUR LEARNING MOMENT PLACEHOLDER]</strong>
                    <p>When and how did this finally make sense? What resource, person, or experience made the difference?</p>
                </div>

                <div class="next-post">
                    <p>Ready for the next challenge?</p>
                    <a href="#">Continue Learning →</a>
                </div>
            </div>
        </article>
    </div>
</body>
</html>"""
    
    return template

# Define ALL posts
all_posts = [
    # Posts already created (1-7)
    # Skipping these as they exist
    
    # Remaining Month 0 posts
    {'num': 9, 'filename': '2025-09-18-object-oriented-confusion.html', 
     'title': 'Object-Oriented Confusion: Classes Aren\'t Just Fancy Dictionaries',
     'date': 'September 18, 2025', 'focus': 'object-oriented programming misunderstandings', 'languages': []},
    
    {'num': 10, 'filename': '2025-09-19-apis-actual-meaning.html',
     'title': 'The Day I Learned What APIs Actually Are',
     'date': 'September 19, 2025', 'focus': 'API integration and data pipelines', 'languages': []},
    
    {'num': 11, 'filename': '2025-09-20-git-saved-my-job.html',
     'title': 'Version Control Saved My Job: A Git Redemption Story',
     'date': 'September 20, 2025', 'focus': 'version control and collaboration', 'languages': []},
    
    {'num': 12, 'filename': '2025-09-21-testing-stopped-breaking-production.html',
     'title': 'Testing: How I Stopped Breaking Production Every Friday',
     'date': 'September 21, 2025', 'focus': 'testing and quality assurance', 'languages': []},
    
    # Month 1: Mathematics posts
    {'num': 13, 'filename': '2025-09-22-matrix-multiplication-clicked.html',
     'title': 'Matrix Multiplication: The Day It Finally Clicked',
     'date': 'September 22, 2025', 'focus': 'matrix operations for industrial data',
     'languages': ['python', 'matlab']},
    
    {'num': 14, 'filename': '2025-09-23-eigenvalues-vibration-patterns.html',
     'title': 'Eigenvalues: Finding Hidden Patterns in Vibration Data',
     'date': 'September 23, 2025', 'focus': 'eigenvalue decomposition for equipment monitoring',
     'languages': ['python', 'r']},
    
    {'num': 15, 'filename': '2025-09-24-pca-decoded.html',
     'title': 'PCA Decoded: Reducing 100 Sensors to 5 That Matter',
     'date': 'September 24, 2025', 'focus': 'dimensionality reduction in sensor networks',
     'languages': ['python', 'julia']},
    
    {'num': 16, 'filename': '2025-09-25-svd-missing-sensor-data.html',
     'title': 'The Magic of SVD in Missing Sensor Data',
     'date': 'September 25, 2025', 'focus': 'singular value decomposition for data recovery',
     'languages': ['python', 'matlab']},
    
    {'num': 17, 'filename': '2025-09-26-probability-not-normal.html',
     'title': 'Probability: Why Your Mill Doesn\'t Follow Normal Distributions',
     'date': 'September 26, 2025', 'focus': 'industrial probability distributions',
     'languages': ['python', 'r']},
    
    {'num': 18, 'filename': '2025-09-27-calculus-optimization.html',
     'title': 'Calculus for Optimization: Finding the Sweet Spot in Rolling Speed',
     'date': 'September 27, 2025', 'focus': 'calculus-based optimization',
     'languages': ['python', 'julia']},
    
    # Month 2: Python Deep Dive posts
    {'num': 19, 'filename': '2025-09-28-numpy-nightmares.html',
     'title': 'NumPy Nightmares: When Vectorization Goes Wrong',
     'date': 'September 28, 2025', 'focus': 'NumPy arrays and vectorization',
     'languages': ['python', 'cpp']},
    
    {'num': 20, 'filename': '2025-09-29-pandas-proficiency.html',
     'title': 'Pandas Proficiency: From CSV Hell to Data Paradise',
     'date': 'September 29, 2025', 'focus': 'data manipulation with Pandas',
     'languages': ['python', 'sql']},
    
    {'num': 21, 'filename': '2025-09-30-bootstrap-saved-predictions.html',
     'title': 'The Bootstrap Method That Saved Our Quality Predictions',
     'date': 'September 30, 2025', 'focus': 'bootstrap methods for uncertainty',
     'languages': ['python', 'r']},
    
    {'num': 22, 'filename': '2025-10-01-convex-optimization.html',
     'title': 'Convex Optimization: Why Some Problems Are Actually Easy',
     'date': 'October 1, 2025', 'focus': 'convex optimization in production',
     'languages': ['python', 'julia']},
    
    {'num': 23, 'filename': '2025-10-02-genetic-algorithms.html',
     'title': 'Genetic Algorithms: When Brute Force Is Actually Smart',
     'date': 'October 2, 2025', 'focus': 'evolutionary algorithms for complex problems',
     'languages': ['python', 'rust']},
    
    {'num': 24, 'filename': '2025-10-03-regularization-stopped-overfitting.html',
     'title': 'Regularization: How I Stopped Overfitting Everything',
     'date': 'October 3, 2025', 'focus': 'regularization techniques',
     'languages': ['python', 'cpp']}
]

# Create all remaining posts
posts_dir = '/Users/edikan/Documents/PROJECT FORGE/edikan-ai/posts'
created_count = 0

for post in all_posts:
    filepath = os.path.join(posts_dir, post['filename'])
    
    # Skip if already exists
    if os.path.exists(filepath):
        print(f"Skipping (exists): {post['filename']}")
        continue
    
    # Create the post
    html_content = create_post(
        post['num'],
        post['filename'],
        post['title'],
        post['date'],
        post['focus'],
        post.get('languages', [])
    )
    
    with open(filepath, 'w') as f:
        f.write(html_content)
    
    created_count += 1
    print(f"Created: {post['filename']}")

print(f"\n✅ Created {created_count} new posts")
print(f"📝 Total posts now: 24")
print("\nRemember to add your personal stories to each post!")