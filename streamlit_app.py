#!/usr/bin/env python3
"""
Instagram Competitor Analytics Tracker - Streamlit Web App
Interactive web application for Instagram competitor analysis and visualization.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import numpy as np
import time
import json
import logging
from typing import List, Dict, Optional

# Configure page
st.set_page_config(
    page_title="Instagram Competitor Analytics Tracker",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MockInstagramAnalytics:
    """Mock Instagram analytics for demonstration purposes."""
    
    def __init__(self):
        """Initialize mock analytics."""
        self.sample_usernames = [
            "example_brand", "competitor_one", "competitor_two", 
            "market_leader", "startup_rival"
        ]
        
    def generate_mock_profile_data(self, username: str) -> Dict:
        """Generate mock profile data for demonstration."""
        np.random.seed(hash(username) % 2**32)  # Consistent data per username
        
        followers = np.random.randint(10000, 1000000)
        following = np.random.randint(100, 5000)
        posts_count = np.random.randint(50, 2000)
        
        return {
            'username': username,
            'followers': followers,
            'following': following,
            'posts_count': posts_count,
            'engagement_rate': np.random.uniform(1.5, 8.5),
            'avg_likes': np.random.randint(100, 50000),
            'avg_comments': np.random.randint(10, 2000),
            'verified': np.random.choice([True, False], p=[0.2, 0.8])
        }
    
    def generate_mock_posts_data(self, username: str, num_posts: int = 20) -> pd.DataFrame:
        """Generate mock posts data for demonstration."""
        np.random.seed(hash(username) % 2**32)
        
        posts = []
        base_date = datetime.now()
        
        for i in range(num_posts):
            post_date = base_date - timedelta(days=np.random.randint(1, 90))
            likes = np.random.randint(50, 100000)
            comments = np.random.randint(5, 5000)
            
            posts.append({
                'username': username,
                'date': post_date.strftime('%Y-%m-%d'),
                'likes': likes,
                'comments': comments,
                'engagement': likes + comments,
                'content_type': np.random.choice(['photo', 'video', 'carousel', 'reel'], 
                                               p=[0.4, 0.2, 0.3, 0.1]),
                'hashtags_count': np.random.randint(0, 30),
                'posted_time': np.random.choice(['morning', 'afternoon', 'evening', 'night'])
            })
        
        return pd.DataFrame(posts)
    
    def get_trending_hashtags(self, username: str) -> List[str]:
        """Generate mock trending hashtags."""
        np.random.seed(hash(username) % 2**32)
        
        base_hashtags = [
            '#instagram', '#photography', '#love', '#instagood', '#photooftheday',
            '#fashion', '#beautiful', '#happy', '#cute', '#followme', '#like4like',
            '#nature', '#art', '#food', '#style', '#amazing', '#beauty', '#fitness',
            '#travel', '#lifestyle', '#motivation', '#inspiration', '#business'
        ]
        
        return np.random.choice(base_hashtags, size=10, replace=False).tolist()

def main():
    """Main Streamlit application."""
    
    # Initialize session state
    if 'analytics' not in st.session_state:
        st.session_state.analytics = MockInstagramAnalytics()
    if 'analyzed_profiles' not in st.session_state:
        st.session_state.analyzed_profiles = {}
    
    # Header
    st.title("📊 Instagram Competitor Analytics Tracker")
    st.markdown("---")
    
    # Sidebar
    with st.sidebar:
        st.header("🔧 Analysis Settings")
        
        # Input form for Instagram handles
        st.subheader("📱 Instagram Handles")
        
        # Option to use sample data or enter custom handles
        use_sample = st.checkbox("Use sample competitor data", value=True)
        
        if use_sample:
            selected_competitors = st.multiselect(
                "Select sample competitors:",
                options=st.session_state.analytics.sample_usernames,
                default=st.session_state.analytics.sample_usernames[:3]
            )
        else:
            custom_handles = st.text_area(
                "Enter Instagram handles (one per line, without @):",
                placeholder="example_brand\ncompetitor_one\ncompetitor_two"
            )
            selected_competitors = [handle.strip() for handle in custom_handles.split('\n') if handle.strip()]
        
        # Analysis options
        st.subheader("📊 Analysis Options")
        num_posts = st.slider("Posts to analyze per profile", 10, 50, 20)
        
        # Analyze button
        analyze_btn = st.button("🚀 Start Analysis", type="primary", use_container_width=True)
        
        if analyze_btn and selected_competitors:
            with st.spinner("Analyzing Instagram profiles..."):
                # Simulate analysis time
                progress_bar = st.progress(0)
                for i, username in enumerate(selected_competitors):
                    time.sleep(0.5)  # Simulate processing time
                    
                    # Generate mock data
                    profile_data = st.session_state.analytics.generate_mock_profile_data(username)
                    posts_data = st.session_state.analytics.generate_mock_posts_data(username, num_posts)
                    hashtags = st.session_state.analytics.get_trending_hashtags(username)
                    
                    st.session_state.analyzed_profiles[username] = {
                        'profile': profile_data,
                        'posts': posts_data,
                        'hashtags': hashtags,
                        'analyzed_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    }
                    
                    progress_bar.progress((i + 1) / len(selected_competitors))
                
                st.success(f"✅ Analysis completed for {len(selected_competitors)} profiles!")
    
    # Main content area
    if st.session_state.analyzed_profiles:
        display_analytics_dashboard()
    else:
        display_welcome_screen()

def display_welcome_screen():
    """Display welcome screen when no analysis has been run."""
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.image("https://via.placeholder.com/400x200/1DA1F2/ffffff?text=Instagram+Analytics", 
                caption="Instagram Competitor Analytics")
        
        st.markdown("""
        ### Welcome to Instagram Competitor Analytics Tracker! 👋
        
        This interactive web application helps you analyze Instagram competitor performance 
        and gain valuable insights for your social media strategy.
        
        **Features:**
        - 📈 Profile performance metrics
        - 📊 Engagement analysis and trends
        - 🔍 Content type performance comparison
        - #️⃣ Popular hashtags discovery
        - 📅 Posting pattern analysis
        
        **Getting Started:**
        1. Use the sidebar to select sample competitors or enter custom handles
        2. Configure analysis settings
        3. Click "Start Analysis" to begin
        
        **Note:** This demo uses mock data for demonstration purposes. 
        In a production environment, this would connect to Instagram's API or web scraping services.
        """)

def display_analytics_dashboard():
    """Display the main analytics dashboard."""
    
    profiles = st.session_state.analyzed_profiles
    
    # Tabs for different views
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📊 Overview", "📈 Engagement Analysis", "📱 Content Analysis", 
        "#️⃣ Hashtag Analysis", "📅 Posting Patterns"
    ])
    
    with tab1:
        display_overview_tab(profiles)
    
    with tab2:
        display_engagement_tab(profiles)
    
    with tab3:
        display_content_tab(profiles)
    
    with tab4:
        display_hashtag_tab(profiles)
    
    with tab5:
        display_posting_patterns_tab(profiles)

def display_overview_tab(profiles: Dict):
    """Display overview metrics and comparisons."""
    
    st.header("📊 Competitor Overview")
    
    # Create summary dataframe
    summary_data = []
    for username, data in profiles.items():
        profile = data['profile']
        posts_df = data['posts']
        
        summary_data.append({
            'Username': f"@{username}",
            'Followers': f"{profile['followers']:,}",
            'Following': f"{profile['following']:,}",
            'Posts': f"{profile['posts_count']:,}",
            'Avg Engagement': f"{posts_df['engagement'].mean():.0f}",
            'Engagement Rate': f"{profile['engagement_rate']:.1f}%",
            'Verified': '✅' if profile['verified'] else '❌'
        })
    
    summary_df = pd.DataFrame(summary_data)
    
    # Display metrics cards
    cols = st.columns(len(profiles))
    for i, (username, data) in enumerate(profiles.items()):
        with cols[i]:
            profile = data['profile']
            st.metric(
                label=f"@{username}",
                value=f"{profile['followers']:,}",
                delta=f"{profile['engagement_rate']:.1f}% engagement"
            )
    
    st.markdown("### 📋 Detailed Comparison")
    st.dataframe(summary_df, use_container_width=True)
    
    # Visualization: Followers vs Engagement Rate
    st.markdown("### 📈 Followers vs Engagement Rate")
    
    plot_data = []
    for username, data in profiles.items():
        profile = data['profile']
        plot_data.append({
            'Username': username,
            'Followers': profile['followers'],
            'Engagement Rate': profile['engagement_rate'],
            'Posts Count': profile['posts_count']
        })
    
    plot_df = pd.DataFrame(plot_data)
    
    fig = px.scatter(
        plot_df, 
        x='Followers', 
        y='Engagement Rate',
        size='Posts Count',
        color='Username',
        hover_name='Username',
        title="Followers vs Engagement Rate",
        labels={'Followers': 'Number of Followers', 'Engagement Rate': 'Engagement Rate (%)'}
    )
    fig.update_layout(height=500)
    st.plotly_chart(fig, use_container_width=True)

def display_engagement_tab(profiles: Dict):
    """Display engagement analysis."""
    
    st.header("📈 Engagement Analysis")
    
    # Combine all posts data
    all_posts = []
    for username, data in profiles.items():
        posts_df = data['posts'].copy()
        all_posts.append(posts_df)
    
    combined_df = pd.concat(all_posts, ignore_index=True)
    combined_df['date'] = pd.to_datetime(combined_df['date'])
    
    # Engagement over time
    st.subheader("📅 Engagement Trends Over Time")
    
    fig = px.line(
        combined_df.groupby(['username', 'date'])['engagement'].mean().reset_index(),
        x='date',
        y='engagement',
        color='username',
        title="Average Engagement Over Time"
    )
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)
    
    # Engagement distribution
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("💬 Likes vs Comments")
        fig = px.scatter(
            combined_df,
            x='likes',
            y='comments',
            color='username',
            title="Likes vs Comments Correlation"
        )
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("📊 Engagement Distribution")
        fig = px.box(
            combined_df,
            x='username',
            y='engagement',
            title="Engagement Distribution by Profile"
        )
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)

def display_content_tab(profiles: Dict):
    """Display content type analysis."""
    
    st.header("📱 Content Type Analysis")
    
    # Combine all posts data
    all_posts = []
    for username, data in profiles.items():
        posts_df = data['posts'].copy()
        all_posts.append(posts_df)
    
    combined_df = pd.concat(all_posts, ignore_index=True)
    
    # Content type performance
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Content Type Distribution")
        content_dist = combined_df['content_type'].value_counts()
        fig = px.pie(
            values=content_dist.values,
            names=content_dist.index,
            title="Content Type Distribution"
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("🎯 Content Type Performance")
        content_perf = combined_df.groupby('content_type')['engagement'].mean().sort_values(ascending=True)
        fig = px.bar(
            x=content_perf.values,
            y=content_perf.index,
            orientation='h',
            title="Average Engagement by Content Type"
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Content type by username
    st.subheader("👥 Content Strategy by Competitor")
    
    content_by_user = combined_df.groupby(['username', 'content_type']).size().unstack(fill_value=0)
    content_by_user_pct = content_by_user.div(content_by_user.sum(axis=1), axis=0) * 100
    
    fig = px.bar(
        content_by_user_pct,
        title="Content Type Distribution by Competitor (%)",
        labels={'value': 'Percentage', 'index': 'Username'}
    )
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)

def display_hashtag_tab(profiles: Dict):
    """Display hashtag analysis."""
    
    st.header("#️⃣ Hashtag Analysis")
    
    # Collect all hashtags
    all_hashtags = {}
    for username, data in profiles.items():
        hashtags = data['hashtags']
        for hashtag in hashtags:
            if hashtag not in all_hashtags:
                all_hashtags[hashtag] = []
            all_hashtags[hashtag].append(username)
    
    # Popular hashtags
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🔥 Most Popular Hashtags")
        hashtag_counts = {tag: len(users) for tag, users in all_hashtags.items()}
        sorted_hashtags = sorted(hashtag_counts.items(), key=lambda x: x[1], reverse=True)[:10]
        
        hashtag_df = pd.DataFrame(sorted_hashtags, columns=['Hashtag', 'Used by # Competitors'])
        st.dataframe(hashtag_df, use_container_width=True)
    
    with col2:
        st.subheader("📊 Hashtag Usage Distribution")
        if sorted_hashtags:
            tags, counts = zip(*sorted_hashtags[:8])
            fig = px.bar(
                x=list(counts),
                y=list(tags),
                orientation='h',
                title="Top Hashtags by Usage"
            )
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)
    
    # Hashtags by competitor
    st.subheader("👥 Hashtag Usage by Competitor")
    
    for username, data in profiles.items():
        with st.expander(f"@{username} - Top Hashtags"):
            hashtags = data['hashtags']
            hashtag_text = " ".join(hashtags)
            st.write(hashtag_text)

def display_posting_patterns_tab(profiles: Dict):
    """Display posting pattern analysis."""
    
    st.header("📅 Posting Pattern Analysis")
    
    # Combine all posts data
    all_posts = []
    for username, data in profiles.items():
        posts_df = data['posts'].copy()
        all_posts.append(posts_df)
    
    combined_df = pd.concat(all_posts, ignore_index=True)
    
    # Posting time analysis
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🕐 Best Posting Times")
        time_engagement = combined_df.groupby('posted_time')['engagement'].mean().sort_values(ascending=False)
        
        fig = px.bar(
            x=time_engagement.index,
            y=time_engagement.values,
            title="Average Engagement by Posting Time"
        )
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("📊 Posting Time Distribution")
        time_dist = combined_df['posted_time'].value_counts()
        
        fig = px.pie(
            values=time_dist.values,
            names=time_dist.index,
            title="When Competitors Post Most"
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Weekly posting frequency
    st.subheader("📈 Posting Frequency by Competitor")
    
    # Add some mock frequency data
    frequency_data = []
    for username in profiles.keys():
        np.random.seed(hash(username) % 2**32)
        for day in ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']:
            frequency_data.append({
                'Username': username,
                'Day': day,
                'Posts': np.random.randint(0, 5)
            })
    
    freq_df = pd.DataFrame(frequency_data)
    
    fig = px.bar(
        freq_df,
        x='Day',
        y='Posts',
        color='Username',
        title="Weekly Posting Frequency",
        barmode='group'
    )
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()