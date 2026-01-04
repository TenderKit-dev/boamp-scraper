"""
Test script to verify boamp-scraper installation
Run after: pip install boamp-scraper
"""

import sys


def test_imports():
    """Test all imports"""
    print("🧪 Testing imports...")
    
    try:
        from boamp import TenderScraper
        print("  ✅ TenderScraper imported")
    except ImportError as e:
        print(f"  ❌ Failed to import TenderScraper: {e}")
        return False
    
    try:
        from boamp import Tender, TenderCategory
        print("  ✅ Models imported")
    except ImportError as e:
        print(f"  ❌ Failed to import models: {e}")
        return False
    
    try:
        from boamp import __version__
        print(f"  ✅ Version: {__version__}")
    except ImportError as e:
        print(f"  ❌ Failed to import version: {e}")
        return False
    
    return True


def test_initialization():
    """Test scraper initialization"""
    print("\n🧪 Testing scraper initialization...")
    
    try:
        from boamp import TenderScraper
        scraper = TenderScraper(headless=True)
        print("  ✅ Scraper initialized")
        return True
    except Exception as e:
        print(f"  ❌ Failed to initialize scraper: {e}")
        return False


def test_models():
    """Test Pydantic models"""
    print("\n🧪 Testing models...")
    
    try:
        from boamp import Tender, TenderCategory
        from datetime import datetime
        
        tender = Tender(
            id="TEST123",
            title="Test Tender",
            organization="Test Org",
            budget=100000,
            category=TenderCategory.IT_DEVELOPMENT,
            url="https://example.com",
            published_date=datetime.now(),
        )
        print("  ✅ Tender model works")
        return True
    except Exception as e:
        print(f"  ❌ Failed to create Tender: {e}")
        return False


def test_cli():
    """Test CLI is available"""
    print("\n🧪 Testing CLI...")
    
    import subprocess
    
    try:
        result = subprocess.run(
            [sys.executable, "-m", "boamp", "--version"],
            capture_output=True,
            text=True,
            timeout=5
        )
        
        if result.returncode == 0:
            print(f"  ✅ CLI works: {result.stdout.strip()}")
            return True
        else:
            print(f"  ❌ CLI failed: {result.stderr}")
            return False
    except Exception as e:
        print(f"  ❌ CLI error: {e}")
        return False


def main():
    """Run all tests"""
    print("=" * 60)
    print("🚀 BOAMP SCRAPER INSTALLATION TEST")
    print("=" * 60)
    
    results = []
    
    # Run tests
    results.append(("Imports", test_imports()))
    results.append(("Initialization", test_initialization()))
    results.append(("Models", test_models()))
    results.append(("CLI", test_cli()))
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 TEST SUMMARY")
    print("=" * 60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status:10} {name}")
    
    print("-" * 60)
    print(f"TOTAL: {passed}/{total} tests passed ({passed/total*100:.0f}%)")
    print("=" * 60)
    
    if passed == total:
        print("\n🎉 ALL TESTS PASSED! Installation is working correctly! 🎉")
        return 0
    else:
        print(f"\n⚠️  {total - passed} test(s) failed. Please check the errors above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())

