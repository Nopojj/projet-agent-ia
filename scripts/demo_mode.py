"""
Demo mode script for JIRA integration
"""
import json
from pathlib import Path
from scripts.utils import get_mock_data

def run_demo():
    """Run demo mode with mock data"""
    print("🚀 Running in DEMO mode...")
    
    # Get mock data
    mock_data = get_mock_data()
    
    # Display summary
    print(f"\n📊 Total issues: {len(mock_data)}")
    
    # Count by status
    status_count = {}
    for item in mock_data:
        status = item['status']
        status_count[status] = status_count.get(status, 0) + 1
    
    print("\n📈 Status breakdown:")
    for status, count in status_count.items():
        print(f"  - {status}: {count}")
    
    return mock_data

if __name__ == "__main__":
    data = run_demo()
    print("\n✅ Demo completed successfully!")