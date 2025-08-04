# 📊 Instagram Competitor Analytics Tracker

Interactive web application for Instagram competitor analysis with comprehensive insights and visualizations.

![Instagram Analytics Dashboard](https://github.com/user-attachments/assets/58b85437-596b-4b71-bedd-575e13a7285b)

## 🌟 Features

- **🌐 Interactive Web Interface**: User-friendly Streamlit dashboard
- **📈 Comprehensive Analytics**: Profile metrics, engagement trends, and performance insights
- **📊 Interactive Visualizations**: Dynamic charts and graphs using Plotly
- **🔍 Multi-Competitor Analysis**: Compare multiple Instagram profiles simultaneously
- **#️⃣ Hashtag Discovery**: Identify popular and trending hashtags
- **📅 Posting Pattern Analysis**: Optimal timing and frequency insights
- **📱 Content Type Analysis**: Performance comparison across different content types
- **💾 Data Export**: Download results in CSV format

## 🚀 Live Demo

**🌐 Access the Live App**: [Instagram Analytics Tracker](https://your-app-name.streamlit.app) *(Deploy to get your URL)*

## 📸 Screenshots

### Welcome Screen
![Welcome Screen](https://github.com/user-attachments/assets/f0a16ca3-60c1-4153-8a4d-ac54df9831d8)

### Analytics Dashboard
![Dashboard Overview](https://github.com/user-attachments/assets/58b85437-596b-4b71-bedd-575e13a7285b)

## 🏃‍♂️ Quick Start

### Option 1: Use the Live Web App (Recommended)
1. Visit the [live application](https://your-app-name.streamlit.app)
2. Select sample competitors or enter custom Instagram handles
3. Configure analysis settings
4. Click "Start Analysis" and explore the interactive dashboard

### Option 2: Run Locally
```bash
# Clone the repository
git clone https://github.com/vaibhavkumarsingh12/instagram-competitor-analytics-tracker.git
cd instagram-competitor-analytics-tracker

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run streamlit_app.py
```

Then open your browser and go to `http://localhost:8501`

## 📱 How to Use

1. **🔧 Configure Settings**: Use the sidebar to select competitors and analysis options
2. **🚀 Start Analysis**: Click the "Start Analysis" button to process the data
3. **📊 Explore Results**: Navigate through different tabs:
   - **Overview**: Competitor comparison and key metrics
   - **Engagement Analysis**: Trends and engagement patterns
   - **Content Analysis**: Content type performance insights
   - **Hashtag Analysis**: Popular hashtag discovery
   - **Posting Patterns**: Optimal posting times and frequency

## 🛠️ Technology Stack

- **Frontend**: [Streamlit](https://streamlit.io/) - Interactive web framework
- **Visualization**: [Plotly](https://plotly.com/) - Interactive charts and graphs
- **Data Processing**: [Pandas](https://pandas.pydata.org/) - Data manipulation and analysis
- **Backend**: Python 3.12+
- **Deployment**: [Streamlit Cloud](https://streamlit.io/cloud) - Free hosting platform

## 📦 Installation & Deployment

### Local Development
```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

### Streamlit Cloud Deployment
1. Fork this repository
2. Visit [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub account
4. Deploy this repository
5. Access your live app at the provided URL

For detailed deployment instructions, see [DEPLOYMENT.md](DEPLOYMENT.md)

## 📊 Current Implementation

**Note**: This version uses mock data for demonstration purposes. The application includes:

- Sample competitor profiles with realistic metrics
- Simulated engagement data and trends
- Mock hashtag analysis
- Artificial posting pattern data

For production use, integrate with:
- Instagram Basic Display API
- Third-party social media APIs
- Web scraping solutions (following Terms of Service)

## 🔧 Customization

### Adding Real Data Sources
Replace the `MockInstagramAnalytics` class in `streamlit_app.py` with real data integration:

```python
# Replace mock data with real API calls
class RealInstagramAnalytics:
    def scrape_profile(self, username):
        # Implement real Instagram data collection
        pass
```

### Extending Functionality
- Add user authentication
- Implement data persistence
- Create scheduled analysis reports
- Add more visualization types

## 📝 Files Structure

```
instagram-competitor-analytics-tracker/
├── streamlit_app.py          # Main Streamlit application
├── scraper.py               # Original Instagram scraper
├── requirements.txt         # Python dependencies
├── .streamlit/
│   └── config.toml         # Streamlit configuration
├── DEPLOYMENT.md           # Deployment guide
└── README.md               # This file
```

## 🚀 Deployment Options

### 1. Streamlit Cloud (Recommended)
- **Free hosting** for public repositories
- **Automatic deployments** from GitHub
- **Custom domains** available
- **Access URL**: `https://your-app-name.streamlit.app`

### 2. GitHub Pages Integration
Create a redirect page that points to your Streamlit Cloud app for easy access via GitHub Pages.

### 3. Alternative Platforms
- Heroku
- Railway
- PythonAnywhere
- DigitalOcean App Platform

## 🔐 Privacy & Compliance

- **No personal data collection** in the demo version
- **Mock data only** for demonstration
- **Instagram ToS compliance** required for production use
- **Rate limiting** implemented in scraper
- **Error handling** for robust operation

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This application is for educational and demonstration purposes. Always comply with Instagram's Terms of Service and API guidelines when collecting data. The current implementation uses mock data to showcase functionality.

---

**🌟 Star this repository if you found it helpful!**
