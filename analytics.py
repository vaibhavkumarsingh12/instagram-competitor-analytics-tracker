#!/usr/bin/env python3
"""
Instagram Analytics Module
Enhanced analytics functions for Instagram competitor analysis.
This module can be extended to work with real Instagram data.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Tuple
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class InstagramAnalytics:
    """
    Instagram Analytics Engine
    
    This class provides comprehensive analytics for Instagram data.
    Currently uses mock data for demonstration, but can be extended
    to work with real Instagram APIs or scraped data.
    """
    
    def __init__(self):
        """Initialize the analytics engine."""
        self.data_cache = {}
        
    def calculate_engagement_rate(self, likes: int, comments: int, followers: int) -> float:
        """
        Calculate engagement rate for a post.
        
        Args:
            likes (int): Number of likes
            comments (int): Number of comments
            followers (int): Number of followers
            
        Returns:
            float: Engagement rate as percentage
        """
        if followers == 0:
            return 0.0
        
        total_engagement = likes + comments
        engagement_rate = (total_engagement / followers) * 100
        return round(engagement_rate, 2)
    
    def analyze_posting_patterns(self, posts_df: pd.DataFrame) -> Dict:
        """
        Analyze posting patterns and optimal timing.
        
        Args:
            posts_df (pd.DataFrame): DataFrame with posts data
            
        Returns:
            Dict: Analysis results with optimal posting insights
        """
        if posts_df.empty:
            return {}
        
        # Convert date column if needed
        if 'date' in posts_df.columns:
            posts_df['date'] = pd.to_datetime(posts_df['date'])
            posts_df['day_of_week'] = posts_df['date'].dt.day_name()
            posts_df['hour'] = posts_df['date'].dt.hour
        
        # Analyze posting frequency by day
        daily_posts = posts_df.groupby('day_of_week').size().to_dict()
        
        # Analyze engagement by posting time
        if 'posted_time' in posts_df.columns:
            time_engagement = posts_df.groupby('posted_time')['engagement'].mean().to_dict()
        else:
            time_engagement = {}
        
        # Find optimal posting times
        best_day = max(daily_posts.items(), key=lambda x: x[1])[0] if daily_posts else None
        best_time = max(time_engagement.items(), key=lambda x: x[1])[0] if time_engagement else None
        
        return {
            'daily_distribution': daily_posts,
            'time_engagement': time_engagement,
            'optimal_day': best_day,
            'optimal_time': best_time,
            'total_posts': len(posts_df),
            'avg_posts_per_day': len(posts_df) / 7 if len(posts_df) > 0 else 0
        }
    
    def analyze_content_performance(self, posts_df: pd.DataFrame) -> Dict:
        """
        Analyze content type performance.
        
        Args:
            posts_df (pd.DataFrame): DataFrame with posts data
            
        Returns:
            Dict: Content performance analysis
        """
        if posts_df.empty or 'content_type' not in posts_df.columns:
            return {}
        
        # Content type distribution
        content_dist = posts_df['content_type'].value_counts().to_dict()
        
        # Average engagement by content type
        content_engagement = posts_df.groupby('content_type')['engagement'].agg([
            'mean', 'median', 'std'
        ]).round(2).to_dict()
        
        # Best performing content type
        best_content = posts_df.groupby('content_type')['engagement'].mean().idxmax()
        
        return {
            'distribution': content_dist,
            'engagement_stats': content_engagement,
            'best_performing': best_content,
            'total_content_types': len(content_dist)
        }
    
    def analyze_hashtag_performance(self, posts_df: pd.DataFrame) -> Dict:
        """
        Analyze hashtag usage and performance.
        
        Args:
            posts_df (pd.DataFrame): DataFrame with posts data
            
        Returns:
            Dict: Hashtag analysis results
        """
        if posts_df.empty:
            return {}
        
        hashtag_data = []
        
        # Extract hashtags from posts if available
        if 'hashtags' in posts_df.columns:
            for _, row in posts_df.iterrows():
                if isinstance(row['hashtags'], list):
                    for hashtag in row['hashtags']:
                        hashtag_data.append({
                            'hashtag': hashtag,
                            'engagement': row.get('engagement', 0),
                            'likes': row.get('likes', 0),
                            'comments': row.get('comments', 0)
                        })
        
        if not hashtag_data:
            return {}
        
        hashtag_df = pd.DataFrame(hashtag_data)
        
        # Top hashtags by usage frequency
        top_hashtags = hashtag_df['hashtag'].value_counts().head(20).to_dict()
        
        # Average engagement per hashtag
        hashtag_engagement = hashtag_df.groupby('hashtag')['engagement'].mean().sort_values(ascending=False).head(20).to_dict()
        
        return {
            'top_by_frequency': top_hashtags,
            'top_by_engagement': hashtag_engagement,
            'total_unique_hashtags': len(hashtag_df['hashtag'].unique()),
            'avg_hashtags_per_post': len(hashtag_df) / len(posts_df) if len(posts_df) > 0 else 0
        }
    
    def calculate_competitor_metrics(self, profiles_data: Dict) -> pd.DataFrame:
        """
        Calculate comprehensive competitor metrics.
        
        Args:
            profiles_data (Dict): Dictionary with profile data for each competitor
            
        Returns:
            pd.DataFrame: Comprehensive metrics comparison
        """
        metrics = []
        
        for username, data in profiles_data.items():
            profile = data.get('profile', {})
            posts_df = data.get('posts', pd.DataFrame())
            
            if posts_df.empty:
                continue
            
            # Basic metrics
            followers = profile.get('followers', 0)
            following = profile.get('following', 0)
            posts_count = profile.get('posts_count', 0)
            
            # Engagement metrics
            avg_likes = posts_df['likes'].mean() if 'likes' in posts_df.columns else 0
            avg_comments = posts_df['comments'].mean() if 'comments' in posts_df.columns else 0
            avg_engagement = posts_df['engagement'].mean() if 'engagement' in posts_df.columns else 0
            
            # Engagement rate
            engagement_rate = self.calculate_engagement_rate(
                int(avg_likes), int(avg_comments), followers
            )
            
            # Growth indicators (mock calculation)
            follower_to_following_ratio = followers / following if following > 0 else 0
            posts_to_followers_ratio = posts_count / followers if followers > 0 else 0
            
            # Content frequency
            posting_patterns = self.analyze_posting_patterns(posts_df)
            
            metrics.append({
                'username': username,
                'followers': followers,
                'following': following,
                'posts_count': posts_count,
                'avg_likes': round(avg_likes, 2),
                'avg_comments': round(avg_comments, 2),
                'avg_engagement': round(avg_engagement, 2),
                'engagement_rate': engagement_rate,
                'follower_following_ratio': round(follower_to_following_ratio, 2),
                'posts_followers_ratio': round(posts_to_followers_ratio * 1000, 2),  # per 1000 followers
                'posts_per_week': round(posting_patterns.get('avg_posts_per_day', 0) * 7, 2),
                'verified': profile.get('verified', False)
            })
        
        return pd.DataFrame(metrics)
    
    def generate_insights(self, profiles_data: Dict) -> Dict:
        """
        Generate actionable insights from competitor analysis.
        
        Args:
            profiles_data (Dict): Dictionary with profile data for each competitor
            
        Returns:
            Dict: Key insights and recommendations
        """
        if not profiles_data:
            return {}
        
        metrics_df = self.calculate_competitor_metrics(profiles_data)
        
        if metrics_df.empty:
            return {}
        
        # Top performers
        top_engagement = metrics_df.loc[metrics_df['engagement_rate'].idxmax()]
        top_followers = metrics_df.loc[metrics_df['followers'].idxmax()]
        most_active = metrics_df.loc[metrics_df['posts_per_week'].idxmax()]
        
        # Industry benchmarks (calculated from the dataset)
        avg_engagement_rate = metrics_df['engagement_rate'].mean()
        avg_followers = metrics_df['followers'].mean()
        avg_posting_frequency = metrics_df['posts_per_week'].mean()
        
        # Content analysis across all competitors
        all_posts = []
        for data in profiles_data.values():
            if not data.get('posts', pd.DataFrame()).empty:
                all_posts.append(data['posts'])
        
        if all_posts:
            combined_posts = pd.concat(all_posts, ignore_index=True)
            content_analysis = self.analyze_content_performance(combined_posts)
            best_content_type = content_analysis.get('best_performing', 'Unknown')
        else:
            best_content_type = 'Unknown'
        
        insights = {
            'top_performers': {
                'highest_engagement': top_engagement['username'],
                'most_followers': top_followers['username'],
                'most_active': most_active['username']
            },
            'benchmarks': {
                'avg_engagement_rate': round(avg_engagement_rate, 2),
                'avg_followers': int(avg_followers),
                'avg_posting_frequency': round(avg_posting_frequency, 2)
            },
            'recommendations': {
                'optimal_content_type': best_content_type,
                'target_engagement_rate': round(avg_engagement_rate * 1.2, 2),  # 20% above average
                'recommended_posting_frequency': f"{round(avg_posting_frequency * 1.1, 1)} posts per week"
            },
            'competitive_gaps': {
                'engagement_leader_advantage': round(top_engagement['engagement_rate'] - avg_engagement_rate, 2),
                'follower_leader_advantage': int(top_followers['followers'] - avg_followers),
                'activity_leader_advantage': round(most_active['posts_per_week'] - avg_posting_frequency, 2)
            }
        }
        
        return insights
    
    def export_analysis_report(self, profiles_data: Dict, filename: str = None) -> str:
        """
        Export comprehensive analysis report.
        
        Args:
            profiles_data (Dict): Dictionary with profile data for each competitor
            filename (str): Optional custom filename
            
        Returns:
            str: Path to exported file
        """
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"instagram_competitor_analysis_{timestamp}.xlsx"
        
        try:
            with pd.ExcelWriter(filename, engine='openpyxl') as writer:
                # Metrics comparison
                metrics_df = self.calculate_competitor_metrics(profiles_data)
                metrics_df.to_excel(writer, sheet_name='Competitor_Metrics', index=False)
                
                # Individual profile data
                for username, data in profiles_data.items():
                    if not data.get('posts', pd.DataFrame()).empty:
                        posts_df = data['posts']
                        sheet_name = f"{username}_Posts"[:31]  # Excel sheet name limit
                        posts_df.to_excel(writer, sheet_name=sheet_name, index=False)
                
                # Insights summary
                insights = self.generate_insights(profiles_data)
                insights_df = pd.DataFrame([insights])
                insights_df.to_excel(writer, sheet_name='Insights', index=False)
            
            logger.info(f"Analysis report exported to {filename}")
            return filename
            
        except Exception as e:
            logger.error(f"Failed to export analysis report: {str(e)}")
            raise