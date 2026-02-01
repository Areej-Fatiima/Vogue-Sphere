# VogueSphere 🎓

**AI-Powered Digital Fashion Consultant** – Final Year Project

VogueSphere is a web-based platform designed to bridge the gap between personal style and the latest fashion trends. Users receive personalized outfit recommendations based on their preferences, uploaded images, and real-time fashion trends from multiple brands.

---

## 🌟 Key Features

- **User Preference Quiz**: Input style, color preferences, body type, climate, and culture to get personalized suggestions.
- **Image-Based Feedback**: Users can upload photos; AI (YOLO + CLIP) detects outfit elements and provides recommendations.
- **Recommendations**: Personalized outfit suggestions using AI-powered matching with real-time fashion data.
- **Community Engagement**: Users can interact, post, and get feedback from the community.
- **Admin Insights**: Admins can analyze trends and regional preferences to improve offerings.
- **Social Media Integration**: Stay updated with trending outfits from Instagram brands.

---

## 🛠️ Technology Stack

- **Frontend**: React.js, Tailwind CSS  
- **Backend**: Flask (Python)  
- **AI & Image Processing**: YOLO, CLIP  
- **Web Scraping**: Selenium, BeautifulSoup  
- **Database**: PostgreSQL / Supabase  
- **Version Control**: Git & GitHub

---

## 🗂 Project Structure




VOUGESPHERE/
├── project-voguesphere/
│ ├── src/
│ │ ├── pages/ # React pages (Quiz, Recommendations, Profile, etc.)
│ │ ├── supabase/ # Supabase client setup
│ │ ├── setupTests.js
│ │ └── reportWebVitals.js
│ ├── tailwind.config.js
│ └── ...other frontend files
├── backend/ # Flask backend (API endpoints, AI processing)
└── README.md



---

## 🚀 How to Run the Project

### Frontend
```bash
cd VOUGESPHERE/project-voguesphere
npm install
npm start
cd VOUGESPHERE/Backend
python -m venv venv
source venv/Scripts/activate  # Windows
 python outfit_scraper/run_both.py


 
