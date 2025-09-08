// Kaggle Activity Graph API - Simple & Clean
const KAGGLE_USERNAME = 'anadiskt';
const KAGGLE_KEY = 'b485f80ad71307a1d0e2447573005104';

// Set environment variables for Kaggle API
process.env.KAGGLE_USERNAME = 'anadiskt';
process.env.KAGGLE_KEY = 'b485f80ad71307a1d0e2447573005104';

function generateKaggleActivityGraph(data) {
  const width = 800;
  const height = 200;
  
  return `<svg width="${width}" height="${height}" viewBox="0 0 ${width} ${height}" fill="none" xmlns="http://www.w3.org/2000/svg">
  <style>
    .title { font: 600 16px 'Segoe UI', Ubuntu, Sans-Serif; fill: #24292f; }
    .activity-day { fill: #ebedf0; }
    .activity-1 { fill: #9be9a8; }
    .activity-2 { fill: #40c463; }
    .activity-3 { fill: #30a14e; }
    .activity-4 { fill: #216e39; }
    .month-label { font: 400 10px 'Segoe UI', Ubuntu, Sans-Serif; fill: #656d76; }
    .day-label { font: 400 10px 'Segoe UI', Ubuntu, Sans-Serif; fill: #656d76; }
  </style>
  
  <!-- Title -->
  <text x="20" y="25" class="title">📊 ${KAGGLE_USERNAME}'s Kaggle Activity</text>
  
  <!-- Activity Grid (52 weeks × 7 days) -->
  ${generateActivityGrid()}
  
  <!-- Month labels -->
  <text x="20" y="180" class="month-label">Jan</text>
  <text x="120" y="180" class="month-label">Mar</text>
  <text x="220" y="180" class="month-label">May</text>
  <text x="320" y="180" class="month-label">Jul</text>
  <text x="420" y="180" class="month-label">Sep</text>
  <text x="520" y="180" class="month-label">Nov</text>
  
  <!-- Day labels -->
  <text x="5" y="55" class="day-label">Mon</text>
  <text x="5" y="75" class="day-label">Wed</text>
  <text x="5" y="95" class="day-label">Fri</text>
  
</svg>`;
}

function generateActivityGrid() {
  let grid = '';
  const squareSize = 11;
  const gap = 2;
  
  // Generate 52 weeks of activity
  for (let week = 0; week < 52; week++) {
    for (let day = 0; day < 7; day++) {
      const x = 20 + week * (squareSize + gap);
      const y = 45 + day * (squareSize + gap);
      
      // Random activity level (0-4) for demo
      const activityLevel = Math.floor(Math.random() * 5);
      const className = activityLevel === 0 ? 'activity-day' : `activity-${activityLevel}`;
      
      grid += `<rect x="${x}" y="${y}" width="${squareSize}" height="${squareSize}" class="${className}" rx="2"/>`;
    }
  }
  
  return grid;
}

// For Vercel API
module.exports = (req, res) => {
  res.setHeader('Content-Type', 'image/svg+xml');
  res.setHeader('Cache-Control', 'public, max-age=3600'); // 1 hour cache
  
  const activityGraph = generateKaggleActivityGraph();
  res.send(activityGraph);
};

// For local testing
if (require.main === module) {
  console.log('🚀 Kaggle Activity Graph API');
  console.log('📊 Generating activity graph...');
  console.log(generateKaggleActivityGraph());
}
