"""
Script to inspect BOAMP.fr structure and find correct selectors

Usage:
    python tools/inspect_boamp.py
"""

import asyncio
from playwright.async_api import async_playwright


async def inspect_boamp():
    """Inspect BOAMP.fr to find correct selectors"""
    
    async with async_playwright() as p:
        # Launch browser
        browser = await p.chromium.launch(headless=False)  # Show browser
        context = await browser.new_context(
            viewport={"width": 1920, "height": 1080},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        )
        page = await context.new_page()
        
        # Navigate to BOAMP search
        url = "https://www.boamp.fr/pages/recherche/?disposition=chronologique&nature=marché&famille=F17&texte=cloud"
        print(f"🌐 Navigating to: {url}")
        
        try:
            await page.goto(url, timeout=30000, wait_until="networkidle")
            print("✅ Page loaded")
            
            # Wait a bit for JS to render
            await asyncio.sleep(3)
            
            # Get page title
            title = await page.title()
            print(f"📄 Page title: {title}")
            
            # Try to find tender containers
            print("\n🔍 Looking for tender containers...")
            
            # Common selectors to try
            selectors_to_try = [
                ".resultat-recherche",
                ".liste-resultats",
                ".avis-item",
                ".annonce",
                "article",
                ".card",
                "[data-testid*='tender']",
                "[data-testid*='avis']",
                ".search-result",
                ".result-item",
            ]
            
            for selector in selectors_to_try:
                try:
                    elements = await page.query_selector_all(selector)
                    if elements:
                        print(f"✅ Found {len(elements)} elements with selector: {selector}")
                        
                        # Get HTML of first element
                        if elements:
                            html = await elements[0].inner_html()
                            print(f"📝 First element HTML (truncated):")
                            print(html[:500])
                            print("...")
                            break
                except Exception as e:
                    pass
            
            # Get page content
            print("\n📄 Getting page content...")
            content = await page.content()
            
            # Save to file
            with open("boamp_page_source.html", "w", encoding="utf-8") as f:
                f.write(content)
            print("✅ Page source saved to boamp_page_source.html")
            
            # Take screenshot
            await page.screenshot(path="boamp_screenshot.png")
            print("✅ Screenshot saved to boamp_screenshot.png")
            
            # Wait for user to inspect
            print("\n⏸️  Browser will stay open for 30 seconds for manual inspection...")
            print("   Inspect the page in the browser window")
            print("   Use F12 to open DevTools")
            print("   Check the HTML structure")
            await asyncio.sleep(30)
            
        except Exception as e:
            print(f"❌ Error: {e}")
        
        finally:
            await browser.close()
            print("\n✅ Done! Check boamp_page_source.html for the full HTML")


if __name__ == "__main__":
    print("🔍 BOAMP Inspector")
    print("=" * 50)
    asyncio.run(inspect_boamp())

