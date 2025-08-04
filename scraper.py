#!/usr/bin/env python3
"""
Instagram Competitor Analytics Tracker - Scraper Module
Improved Instagram scraper with robust error handling, data validation,
CSV support, and mechanisms for handling rate limiting.
"""

import snscrape.modules.instagram as sninstagram
import pandas as pd
import time
import random
import csv
import os
from datetime import datetime, timedelta
import logging
from typing import List, Dict, Optional
import json

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('scraper.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class InstagramScraper:
    """Enhanced Instagram scraper with robust error handling and data validation."""
    
    def __init__(self, delay_range=(1, 3), max_retries=3):
        """
        Initialize the Instagram scraper.
        
        Args:
            delay_range (tuple): Range for random delays between requests
            max_retries (int): Maximum number of retries for failed requests
        """
        self.delay_range = delay_range
        self.max_retries = max_retries
        self.scraped_data = []
        
    def add_delay(self):
        """Add random delay to avoid rate limiting."""
        delay = random.uniform(*self.delay_range)
        logger.info(f"Adding delay of {delay:.2f} seconds")
        time.sleep(delay)
        
    def validate_post_data(self, post) -> bool:
        """Validate scraped post data."""
        required_fields = ['date', 'content', 'likeCount', 'commentCount']
        
        for field in required_fields:
            if not hasattr(post, field) or getattr(post, field) is None:
                logger.warning(f"Missing or invalid field: {field}")
                return False
        return True
        
    def extract_hashtags(self, content: str) -> List[str]:
        """Extract hashtags from post content."""
        if not content:
            return []
        
        hashtags = []
        words = content.split()
        for word in words:
            if word.startswith('#') and len(word) > 1:
                hashtags.append(word.lower())
        return hashtags
        
    def scrape_profile(self, username: str, max_posts: int = 50) -> List[Dict]:
        """
        Scrape Instagram profile with enhanced error handling.
        
        Args:
            username (str): Instagram username (without @)
            max_posts (int): Maximum number of posts to scrape
            
        Returns:
            List[Dict]: List of post data dictionaries
        """
        logger.info(f"Starting to scrape profile: {username}")
        posts_data = []
        retry_count = 0
        
        while retry_count < self.max_retries:
            try:
                # Initialize the scraper
                profile_scraper = sninstagram.InstagramUserScraper(username)
                posts_scraped = 0
                
                for post in profile_scraper.get_items():
                    if posts_scraped >= max_posts:
                        break
                        
                    # Validate post data
                    if not self.validate_post_data(post):
                        logger.warning(f"Skipping invalid post from {username}")
                        continue
                    
                    # Extract post information
                    post_data = {
                        'username': username,
                        'date': post.date.isoformat() if post.date else None,
                        'content': post.content or '',
                        'likes': post.likeCount or 0,
                        'comments': post.commentCount or 0,
                        'hashtags': self.extract_hashtags(post.content or ''),
                        'url': post.url or '',
                        'scraped_at': datetime.now().isoformat()
                    }
                    
                    # Calculate engagement rate
                    total_engagement = post_data['likes'] + post_data['comments']
                    post_data['engagement'] = total_engagement
                    
                    posts_data.append(post_data)
                    posts_scraped += 1
                    
                    logger.info(f"Scraped post {posts_scraped}/{max_posts} from {username}")
                    
                    # Add delay between posts
                    self.add_delay()
                    
                logger.info(f"Successfully scraped {len(posts_data)} posts from {username}")
                return posts_data
                
            except Exception as e:
                retry_count += 1
                logger.error(f"Error scraping {username} (attempt {retry_count}/{self.max_retries}): {str(e)}")
                
                if retry_count < self.max_retries:
                    wait_time = retry_count * 30  # Exponential backoff
                    logger.info(f"Retrying in {wait_time} seconds...")
                    time.sleep(wait_time)
                else:
                    logger.error(f"Failed to scrape {username} after {self.max_retries} attempts")
                    
        return posts_data
        
    def scrape_multiple_profiles(self, usernames: List[str], max_posts_per_profile: int = 50) -> pd.DataFrame:
        """
        Scrape multiple Instagram profiles.
        
        Args:
            usernames (List[str]): List of Instagram usernames
            max_posts_per_profile (int): Maximum posts per profile
            
        Returns:
            pd.DataFrame: Combined data from all profiles
        """
        all_posts = []
        
        for i, username in enumerate(usernames, 1):
            logger.info(f"Processing profile {i}/{len(usernames)}: {username}")
            
            try:
                posts = self.scrape_profile(username, max_posts_per_profile)
                all_posts.extend(posts)
                
                # Add longer delay between profiles
                if i < len(usernames):
                    profile_delay = random.uniform(5, 10)
                    logger.info(f"Waiting {profile_delay:.2f} seconds before next profile...")
                    time.sleep(profile_delay)
                    
            except Exception as e:
                logger.error(f"Failed to scrape profile {username}: {str(e)}")
                continue
                
        if all_posts:
            df = pd.DataFrame(all_posts)
            logger.info(f"Total posts scraped: {len(df)}")
            return df
        else:
            logger.warning("No posts were scraped successfully")
            return pd.DataFrame()
            
    def save_to_csv(self, data: pd.DataFrame, filename: str = None) -> str:
        """
        Save scraped data to CSV file.
        
        Args:
            data (pd.DataFrame): Data to save
            filename (str): Custom filename (optional)
            
        Returns:
            str: Path to saved file
        """
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"instagram_data_{timestamp}.csv"
            
        try:
            data.to_csv(filename, index=False, encoding='utf-8')
            logger.info(f"Data saved to {filename}")
            return filename
        except Exception as e:
            logger.error(f"Failed to save data to CSV: {str(e)}")
            raise
            
    def load_from_csv(self, filename: str) -> pd.DataFrame:
        """
        Load previously scraped data from CSV file.
        
        Args:
            filename (str): Path to CSV file
            
        Returns:
            pd.DataFrame: Loaded data
        """
        try:
            if not os.path.exists(filename):
                logger.warning(f"File {filename} does not exist")
                return pd.DataFrame()
                
            data = pd.read_csv(filename)
            logger.info(f"Loaded {len(data)} records from {filename}")
            return data
        except Exception as e:
            logger.error(f"Failed to load data from CSV: {str(e)}")
            raise
            
    def save_to_json(self, data: pd.DataFrame, filename: str = None) -> str:
        """
        Save scraped data to JSON file.
        
        Args:
            data (pd.DataFrame): Data to save
            filename (str): Custom filename (optional)
            
        Returns:
            str: Path to saved file
        """
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"instagram_data_{timestamp}.json"
            
        try:
            # Convert DataFrame to JSON
            data_dict = data.to_dict(orient='records')
            
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data_dict, f, indent=2, ensure_ascii=False)
                
            logger.info(f"Data saved to {filename}")
            return filename
        except Exception as e:
            logger.error(f"Failed to save data to JSON: {str(e)}")
            raise

def main():
    """Example usage of the Instagram scraper."""
    # Example competitor usernames (replace with actual usernames)
    competitors = [
        'example_user1',
        'example_user2', 
        'example_user3'
    ]
    
    # Initialize scraper
    scraper = InstagramScraper(delay_range=(2, 5), max_retries=3)
    
    try:
        # Scrape data from multiple profiles
        logger.info("Starting competitor analysis scraping...")
        data = scraper.scrape_multiple_profiles(competitors, max_posts_per_profile=30)
        
        if not data.empty:
            # Save data to files
            csv_file = scraper.save_to_csv(data)
            json_file = scraper.save_to_json(data)
            
            # Display basic statistics
            print(f"\nScraping completed!")
            print(f"Total posts scraped: {len(data)}")
            print(f"Profiles scraped: {data['username'].nunique()}")
            print(f"Data saved to: {csv_file}")
            print(f"JSON backup saved to: {json_file}")
            
            # Show top posts by engagement
            if len(data) > 0:
                top_posts = data.nlargest(5, 'engagement')[['username', 'likes', 'comments', 'engagement']]
                print("\nTop 5 posts by engagement:")
                print(top_posts.to_string(index=False))
                
        else:
            logger.warning("No data was scraped successfully")
            
    except Exception as e:
        logger.error(f"Scraping failed: {str(e)}")
        raise

if __name__ == "__main__":
    main()
