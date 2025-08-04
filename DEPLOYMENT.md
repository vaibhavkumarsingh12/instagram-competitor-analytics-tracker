# Instagram Competitor Analytics Tracker - Deployment Guide

## 🚀 Live Web Application

This Instagram Competitor Analytics Tracker has been upgraded to a fully interactive web application using Streamlit. The app provides comprehensive competitor analysis with interactive charts and visualizations.

### 📱 Features

- **Interactive Dashboard**: User-friendly web interface for entering Instagram handles
- **Comprehensive Analytics**: 
  - Profile performance metrics
  - Engagement analysis and trends  
  - Content type performance comparison
  - Popular hashtags discovery
  - Posting pattern analysis
- **Interactive Visualizations**: Dynamic charts using Plotly
- **Real-time Analysis**: Process multiple competitors simultaneously
- **Export Capabilities**: Download data and charts

### 🌐 Accessing the Deployed App

#### Streamlit Cloud Deployment

1. **Live App URL**: Once deployed to Streamlit Cloud, the app will be available at:
   ```
   https://[your-app-name].streamlit.app
   ```

2. **Direct Repository Access**: The app can be deployed directly from this GitHub repository to Streamlit Cloud.

### 🔧 Local Development

To run the application locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/vaibhavkumarsingh12/instagram-competitor-analytics-tracker.git
   cd instagram-competitor-analytics-tracker
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app**:
   ```bash
   streamlit run streamlit_app.py
   ```

4. **Access the app**: Open your browser and go to `http://localhost:8501`

### 📊 How to Use

1. **Open the app** in your web browser
2. **Configure settings** in the sidebar:
   - Choose sample competitor data or enter custom Instagram handles
   - Set the number of posts to analyze per profile
3. **Click "Start Analysis"** to begin the analysis
4. **Explore the results** across different tabs:
   - Overview: Competitor comparison and metrics
   - Engagement Analysis: Trends and engagement patterns
   - Content Analysis: Content type performance
   - Hashtag Analysis: Popular hashtag discovery
   - Posting Patterns: Optimal posting times and frequency

### 🚀 Streamlit Cloud Deployment Instructions

#### Option 1: Deploy via Streamlit Cloud (Recommended)

1. **Visit Streamlit Cloud**: Go to [share.streamlit.io](https://share.streamlit.io)
2. **Connect GitHub**: Link your GitHub account
3. **Deploy this repository**: 
   - Repository: `vaibhavkumarsingh12/instagram-competitor-analytics-tracker`
   - Branch: `main`
   - Main file path: `streamlit_app.py`
4. **Deploy**: Click "Deploy" and wait for the app to build
5. **Access**: Your app will be live at `https://[auto-generated-name].streamlit.app`

#### Option 2: Deploy via GitHub Pages (Static Hosting)

While Streamlit apps require a Python backend, you can embed the Streamlit Cloud app in a GitHub Pages site:

1. **Create `index.html`** in your repository:
   ```html
   <!DOCTYPE html>
   <html>
   <head>
       <title>Instagram Competitor Analytics Tracker</title>
       <meta http-equiv="refresh" content="0; url=https://your-app-name.streamlit.app">
   </head>
   <body>
       <p>Redirecting to <a href="https://your-app-name.streamlit.app">Instagram Analytics Tracker</a></p>
   </body>
   </html>
   ```

2. **Enable GitHub Pages**: 
   - Go to repository Settings > Pages
   - Set source to "Deploy from a branch"
   - Select `main` branch
   - Your redirect page will be at `https://vaibhavkumarsingh12.github.io/instagram-competitor-analytics-tracker`

### 🔧 Configuration Files

The repository includes configuration files for easy deployment:

- `requirements.txt`: Python dependencies
- `.streamlit/config.toml`: Streamlit configuration
- `streamlit_app.py`: Main application file

### 📝 Technical Notes

- **Mock Data**: The current implementation uses mock data for demonstration purposes
- **Instagram API**: For production use, consider integrating with Instagram's official API or approved scraping solutions
- **Rate Limiting**: The original scraper includes rate limiting and error handling
- **Scalability**: The app can be extended with caching, database integration, and user authentication

### 🛠️ Customization

To customize the app:

1. **Modify data sources**: Update the `MockInstagramAnalytics` class in `streamlit_app.py`
2. **Add new visualizations**: Extend the dashboard tabs with additional charts
3. **Integrate real APIs**: Replace mock data with actual Instagram API calls
4. **Add authentication**: Implement user login and data persistence

### 📈 Production Considerations

- **API Integration**: Replace mock data with real Instagram data sources
- **Database**: Add data persistence with databases like PostgreSQL or MongoDB
- **Authentication**: Implement user management and secure access
- **Caching**: Add caching for improved performance
- **Error Handling**: Enhanced error handling for production use

---

**Note**: This application is for educational and demonstration purposes. Always comply with Instagram's Terms of Service and API guidelines when collecting data.