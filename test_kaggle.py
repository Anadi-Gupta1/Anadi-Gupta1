import os
import json

# Set environment variables for Kaggle
os.environ['KAGGLE_USERNAME'] = 'anadiskt'
os.environ['KAGGLE_KEY'] = 'b485f80ad71307a1d0e2447573005104'

try:
    import kaggle
    api = kaggle.api
    
    # Test basic API call
    print("🔍 Testing Kaggle API connection...")
    
    # Try to get some basic stats
    print(f"🎯 Attempting to fetch user data...")
    
    # Get datasets
    try:
        datasets = api.dataset_list(user='anadiskt')
        print(f"📦 Datasets: {len(datasets) if datasets else 0}")
        if datasets:
            print(f"   Example dataset: {datasets[0].ref if datasets else 'None'}")
    except Exception as e:
        print(f"⚠️ Datasets error: {e}")
    
    # Get competitions
    try:
        competitions = api.competitions_list(user='anadiskt')
        print(f"🏆 Competitions: {len(competitions) if competitions else 0}")
        if competitions:
            print(f"   Example competition: {competitions[0].ref if competitions else 'None'}")
    except Exception as e:
        print(f"⚠️ Competitions error: {e}")
    
    print("✅ Kaggle API test completed successfully!")
    
except Exception as e:
    print(f"❌ Error: {e}")
    print("🔧 This might be a credential or network issue")
