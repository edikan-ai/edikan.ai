"""
Blog post generation script for edikan.ai
Generates all 24 posts with proper structure
"""

import os
from datetime import datetime, timedelta

# Blog post metadata
POSTS = [
    # Month 00: The Confession (6 posts)
    {
        'filename': '2025-09-10-transpose-button-confession.html',
        'title': 'The Transpose Button Confession: How I Faked My Way Through AI',
        'date': 'September 10, 2025',
        'part': 1,
        'status': 'created'
    },
    {
        'filename': '2025-09-11-variable-amnesia.html', 
        'title': 'Variable Amnesia: When I Couldn\'t Explain What x = 5 Actually Means',
        'date': 'September 11, 2025',
        'part': 2,
        'status': 'created'
    },
    {
        'filename': '2025-09-12-loop-that-almost-got-me-fired.html',
        'title': 'The Loop That Almost Got Me Fired',
        'date': 'September 12, 2025',
        'part': 3,
        'status': 'created'
    },
    {
        'filename': '2025-09-13-functions-more-than-copy-paste.html',
        'title': 'Functions: More Than Copy-Paste Blocks I Don\'t Understand',
        'date': 'September 13, 2025',
        'part': 4,
        'status': 'pending'
    },
    {
        'filename': '2025-09-14-data-structure-disaster.html',
        'title': 'My Data Structure Disaster at the Steel Mill',
        'date': 'September 14, 2025',
        'part': 5,
        'status': 'pending'
    },
    {
        'filename': '2025-09-15-debugging-diary.html',
        'title': 'The Debugging Diary: Learning to Fix What I Don\'t Understand',
        'date': 'September 15, 2025',
        'part': 6,
        'status': 'pending'
    },
    
    # Month 0: Building Competence (6 posts)
    {
        'filename': '2025-09-16-excel-to-python.html',
        'title': 'From Excel to Python: A Metallurgist\'s Painful Journey',
        'date': 'September 16, 2025',
        'part': 7,
        'status': 'pending'
    },
    {
        'filename': '2025-09-17-sql-nightmares.html',
        'title': 'SQL Nightmares: When SELECT * Crashed Production',
        'date': 'September 17, 2025',
        'part': 8,
        'status': 'pending'
    },
    {
        'filename': '2025-09-18-object-oriented-confusion.html',
        'title': 'Object-Oriented Confusion: Classes Aren\'t Just Fancy Dictionaries',
        'date': 'September 18, 2025',
        'part': 9,
        'status': 'pending'
    },
    {
        'filename': '2025-09-19-apis-actual-meaning.html',
        'title': 'The Day I Learned What APIs Actually Are',
        'date': 'September 19, 2025',
        'part': 10,
        'status': 'pending'
    },
    {
        'filename': '2025-09-20-git-saved-my-job.html',
        'title': 'Version Control Saved My Job: A Git Redemption Story',
        'date': 'September 20, 2025',
        'part': 11,
        'status': 'pending'
    },
    {
        'filename': '2025-09-21-testing-stopped-breaking-production.html',
        'title': 'Testing: How I Stopped Breaking Production Every Friday',
        'date': 'September 21, 2025',
        'part': 12,
        'status': 'pending'
    },
    
    # Month 1: Mathematics (6 posts)
    {
        'filename': '2025-09-22-matrix-multiplication-clicked.html',
        'title': 'Matrix Multiplication: The Day It Finally Clicked',
        'date': 'September 22, 2025',
        'part': 13,
        'status': 'pending'
    },
    {
        'filename': '2025-09-23-eigenvalues-vibration-patterns.html',
        'title': 'Eigenvalues: Finding Hidden Patterns in Vibration Data',
        'date': 'September 23, 2025',
        'part': 14,
        'status': 'pending'
    },
    {
        'filename': '2025-09-24-pca-decoded.html',
        'title': 'PCA Decoded: Reducing 100 Sensors to 5 That Matter',
        'date': 'September 24, 2025',
        'part': 15,
        'status': 'pending'
    },
    {
        'filename': '2025-09-25-svd-missing-sensor-data.html',
        'title': 'The Magic of SVD in Missing Sensor Data',
        'date': 'September 25, 2025',
        'part': 16,
        'status': 'pending'
    },
    {
        'filename': '2025-09-26-probability-not-normal.html',
        'title': 'Probability: Why Your Mill Doesn\'t Follow Normal Distributions',
        'date': 'September 26, 2025',
        'part': 17,
        'status': 'pending'
    },
    {
        'filename': '2025-09-27-calculus-optimization.html',
        'title': 'Calculus for Optimization: Finding the Sweet Spot in Rolling Speed',
        'date': 'September 27, 2025',
        'part': 18,
        'status': 'pending'
    },
    
    # Month 2: Python Deep Dive (6 posts)
    {
        'filename': '2025-09-28-numpy-nightmares.html',
        'title': 'NumPy Nightmares: When Vectorization Goes Wrong',
        'date': 'September 28, 2025',
        'part': 19,
        'status': 'pending'
    },
    {
        'filename': '2025-09-29-pandas-proficiency.html',
        'title': 'Pandas Proficiency: From CSV Hell to Data Paradise',
        'date': 'September 29, 2025',
        'part': 20,
        'status': 'pending'
    },
    {
        'filename': '2025-09-30-bootstrap-saved-predictions.html',
        'title': 'The Bootstrap Method That Saved Our Quality Predictions',
        'date': 'September 30, 2025',
        'part': 21,
        'status': 'pending'
    },
    {
        'filename': '2025-10-01-convex-optimization.html',
        'title': 'Convex Optimization: Why Some Problems Are Actually Easy',
        'date': 'October 1, 2025',
        'part': 22,
        'status': 'pending'
    },
    {
        'filename': '2025-10-02-genetic-algorithms.html',
        'title': 'Genetic Algorithms: When Brute Force Is Actually Smart',
        'date': 'October 2, 2025',
        'part': 23,
        'status': 'pending'
    },
    {
        'filename': '2025-10-03-regularization-stopped-overfitting.html',
        'title': 'Regularization: How I Stopped Overfitting Everything',
        'date': 'October 3, 2025',
        'part': 24,
        'status': 'pending'
    }
]

def create_blog_index():
    """Create the main blog index page"""
    html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blog - edikan.ai | Industrial AI Mastery Journey</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }
        
        .container {
            width: 100%;
            max-width: 1000px;
            margin: 0 auto;
            padding: 20px;
        }
        
        header {
            background: white;
            border-radius: 10px;
            padding: 30px;
            margin-bottom: 30px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            text-align: center;
        }
        
        h1 {
            color: #667eea;
            margin-bottom: 10px;
            font-size: 2.5rem;
        }
        
        .tagline {
            color: #666;
            font-size: 1.2rem;
            font-style: italic;
        }
        
        .posts-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 20px;
            margin-top: 30px;
        }
        
        .post-card {
            background: white;
            border-radius: 10px;
            padding: 25px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            transition: transform 0.3s, box-shadow 0.3s;
            cursor: pointer;
            text-decoration: none;
            color: inherit;
            display: block;
        }
        
        .post-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }
        
        .post-number {
            background: #667eea;
            color: white;
            width: 30px;
            height: 30px;
            border-radius: 50%;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            font-size: 0.9rem;
            margin-bottom: 10px;
        }
        
        .post-title {
            color: #333;
            font-size: 1.1rem;
            font-weight: 600;
            margin-bottom: 8px;
            line-height: 1.4;
        }
        
        .post-date {
            color: #999;
            font-size: 0.9rem;
        }
        
        .section-header {
            background: rgba(255,255,255,0.95);
            border-radius: 10px;
            padding: 20px;
            margin: 30px 0 20px;
            text-align: center;
        }
        
        .section-header h2 {
            color: #667eea;
            font-size: 1.8rem;
        }
        
        .coming-soon {
            opacity: 0.6;
            cursor: not-allowed;
        }
        
        .nav-links {
            background: white;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 20px;
            text-align: center;
        }
        
        .nav-links a {
            color: #667eea;
            text-decoration: none;
            margin: 0 15px;
            font-weight: 600;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="nav-links">
            <a href="/">← Back to edikan.ai</a>
            <a href="https://github.com/edikan-ai/edikan-ai-docs" target="_blank">View Exercises</a>
        </div>
        
        <header>
            <h1>The Industrial AI Journey</h1>
            <p class="tagline">From confession to competence - A brutally honest path to mastery</p>
        </header>
        
        <div class="section-header">
            <h2>Month 00: The Confession</h2>
            <p>Admitting what I don't know</p>
        </div>
        
        <div class="posts-grid">
'''
    
    # Add all posts
    current_section = "00"
    for post in POSTS:
        # Add section headers
        if post['part'] == 7:
            html += '''
        </div>
        
        <div class="section-header">
            <h2>Month 0: Building Competence</h2>
            <p>Learning the fundamentals properly</p>
        </div>
        
        <div class="posts-grid">
'''
        elif post['part'] == 13:
            html += '''
        </div>
        
        <div class="section-header">
            <h2>Month 1: Mathematical Foundations</h2>
            <p>The language of industrial AI</p>
        </div>
        
        <div class="posts-grid">
'''
        elif post['part'] == 19:
            html += '''
        </div>
        
        <div class="section-header">
            <h2>Month 2: Python Deep Dive</h2>
            <p>From basics to industrial applications</p>
        </div>
        
        <div class="posts-grid">
'''
        
        # Add post card
        status_class = '' if post['status'] == 'created' else ' coming-soon'
        html += f'''
            <a href="posts/{post['filename']}" class="post-card{status_class}">
                <div class="post-number">{post['part']}</div>
                <h3 class="post-title">{post['title']}</h3>
                <p class="post-date">{post['date']}</p>
            </a>
'''
    
    html += '''
        </div>
    </div>
</body>
</html>'''
    
    return html

# Generate blog index
blog_index = create_blog_index()
print("Blog index generated")
print(f"Total posts to create: {len(POSTS)}")
print(f"Posts already created: {sum(1 for p in POSTS if p['status'] == 'created')}")
print(f"Posts pending: {sum(1 for p in POSTS if p['status'] == 'pending')}")