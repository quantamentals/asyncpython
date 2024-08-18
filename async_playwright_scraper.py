import asyncio
import aiohttp
from playwright.async_api import async_playwright

"""

It looks like you've provided three different main functions that utilize different libraries for web scraping and automation. Here's a breakdown of each:
1. Basic Playwright usage
This function launches a Chromium browser, navigates to https://example.com, prints the page title, and closes the browser.
2. Advanced Playwright usage
This function also uses Playwright to launch a Chromium browser and navigate to https://example.com. Additionally, it:

    Takes a screenshot of the page and saves it as "example.png"
    Retrieves the HTML content of the page and prints it
    Retrieves the title of the page and prints it

3. aiohttp usage
This function uses aiohttp to send a GET request to https://example.com and prints the HTML response.



Playwright and asyncio are a powerful combination for web scraping, automation, and testing. Here are some additional use cases:
1. Form submission
Use Playwright to fill out forms and submit them, then await the response.
Python

await page.fill('input[name="username"]', 'username')
await page.fill('input[name="password"]', 'password')
await page.click('button[type="submit"]')

2. Clicking buttons and links
Await clicks on buttons or links to trigger navigation or JavaScript events.
Python

await page.click('button[type="button"]')
await page.click('a[href="/about"]')

3. Scrolling and waiting
Await scrolling to specific elements or waiting for elements to appear.
Python

await page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
await page.wait_for_selector('div.loader', state='hidden')

4. Handling alerts and dialogs
Await and handle alerts, confirmations, or prompts.
Python

page.on('dialog', lambda dialog: dialog.accept())
await page.click('button[type="button"]')

5. Downloading files
Await downloads by clicking on links or buttons that trigger file downloads.
Python

await page.click('a[href="/download.pdf"]')

6. Uploading files
Await file uploads by filling input fields with file paths.
Python

await page.fill('input[type="file"]', '/path/to/file.txt')

7. Network requests
Await network requests and responses to inspect or mock API calls.
Python

page.on('request', lambda request: print(request.url))
page.on('response', lambda response: print(response.status))

8. Browser context and page management
Await creation and destruction of browser contexts and pages.
Python

browser_context = await playwright.chromium.launchPersistentContext()
page = await browser_context.newPage()
await page.goto('https://example.com')
await browser_context.close()

9. Emulation
Await emulation of different devices, screen sizes, or languages.
Python

await page.emulate(Playwright.devices['iPhone 12'])

10. Testing
Await and assert page content, titles, or URLs for end-to-end testing.
Python

assert await page.title() == 'Example Domain'

These use cases showcase the power of combining Playwright with asyncio for efficient and effective web automation and scraping.


##

Playwright and asyncio are a powerful combination for web scraping, automation, and testing. Here are some additional use cases:
1. Form submission
Use Playwright to fill out forms and submit them, then await the response.
Python

await page.fill('input[name="username"]', 'username')
await page.fill('input[name="password"]', 'password')
await page.click('button[type="submit"]')

2. Clicking buttons and links
Await clicks on buttons or links to trigger navigation or JavaScript events.
Python

await page.click('button[type="button"]')
await page.click('a[href="/about"]')

3. Scrolling and waiting
Await scrolling to specific elements or waiting for elements to appear.
Python

await page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
await page.wait_for_selector('div.loader', state='hidden')

4. Handling alerts and dialogs
Await and handle alerts, confirmations, or prompts.
Python

page.on('dialog', lambda dialog: dialog.accept())
await page.click('button[type="button"]')

5. Downloading files
Await downloads by clicking on links or buttons that trigger file downloads.
Python

await page.click('a[href="/download.pdf"]')

6. Uploading files
Await file uploads by filling input fields with file paths.
Python

await page.fill('input[type="file"]', '/path/to/file.txt')

7. Network requests
Await network requests and responses to inspect or mock API calls.
Python

page.on('request', lambda request: print(request.url))
page.on('response', lambda response: print(response.status))

8. Browser context and page management
Await creation and destruction of browser contexts and pages.
Python

browser_context = await playwright.chromium.launchPersistentContext()
page = await browser_context.newPage()
await page.goto('https://example.com')
await browser_context.close()

9. Emulation
Await emulation of different devices, screen sizes, or languages.
Python

await page.emulate(Playwright.devices['iPhone 12'])

10. Testing
Await and assert page content, titles, or URLs for end-to-end testing.
Python

assert await page.title() == 'Example Domain'

These use cases showcase the power of combining Playwright with asyncio for efficient and effective web automation and scraping.

Playwright is an excellent tool for scraping JavaScript-heavy websites, including Single-Page Applications (SPAs). Here are some tips to help you scrape JS clients or SPAs with Playwright:
1. Wait for the page to load
Use page.wait_for_load_state() to wait for the page to finish loading, including any asynchronous data fetching.
Python

await page.goto('https://example.com')
await page.wait_for_load_state('networkidle')

2. Wait for specific elements
Use page.wait_for_selector() to wait for specific elements to appear, indicating that the data has been loaded.
Python

await page.wait_for_selector('div[data-loaded="true"]')

3. Use page.query_selector()
Instead of page.content(), use page.query_selector() to retrieve specific elements or data.
Python

elements = await page.query_selector_all('div.product')
for element in elements:
    title = await element.query_selector('h2')
    print(await title.text_content())

4. Evaluate JavaScript
Use page.evaluate() to execute JavaScript code in the context of the page, allowing you to access data that's not readily available in the HTML.
Python

data = await page.evaluate('() => window.data')
print(data)

5. Handle pagination and infinite scrolling
Use page.wait_for_selector() and page.evaluate() to handle pagination and infinite scrolling.
Python

while True:
    await page.wait_for_selector('div.loading', state='hidden')
    await page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
    if not await page.query_selector('div.next-page'):
        break

6. Use page.context()
Create a new browser context to isolate sessions and avoid conflicts when scraping multiple pages.
Python

context = await playwright.chromium.launchPersistentContext()
page = await context.newPage()

7. Handle anti-scraping measures
Be respectful of websites and handle anti-scraping measures like rate limiting, CAPTCHAs, or JavaScript challenges.
By following these tips, you can effectively use Playwright to scrape JavaScript-heavy websites, including SPAs. Remember to always check the website's terms of service and robots.txt file to ensure you're not violating any scraping policies.


Here are some popular anti-scraping measures:
1. Rate Limiting

    Limiting the number of requests from a single IP address within a certain time frame.

2. CAPTCHAs

    Challenges that require human interaction, such as image recognition or text entry.

3. JavaScript Challenges

    Executing JavaScript code to verify the user is a human, rather than a bot.

4. IP Blocking

    Blocking requests from specific IP addresses or ranges.

5. User-Agent Blocking

    Blocking requests based on the User-Agent header, which identifies the browser or scraper.

6. Honeypot Traps

    Setting up decoy pages or links that, when accessed, reveal a scraper's presence.

7. Browser Fingerprinting

    Collecting information about a browser's characteristics, such as plugins, screen resolution, and language, to identify scrapers.

8. Cookie-Based Validation

    Requiring cookies to be set and validated to ensure a legitimate browser session.

9. Token-Based Validation

    Requiring tokens, such as CSRF tokens, to be present and valid in requests.

10. Machine Learning-Based Detection

    Using machine learning algorithms to identify patterns and anomalies indicative of scraping activity.

11. Web Application Firewalls (WAFs)

    Configuring WAFs to detect and block scraping traffic based on rules and patterns.

12. Content Protection Networks

    Using services like Cloudflare or Akamai to protect content and detect scraping activity.

13. Browser Rendering Analysis

    Analyzing how a browser renders content to detect scrapers, which often use headless browsers.

14. Behavioral Analysis

    Monitoring user behavior to detect anomalies indicative of scraping activity.

To bypass these measures, scrapers often employ techniques like:

    Rotating IP addresses and User-Agents
    Using headless browsers with rendering capabilities
    Solving CAPTCHAs and JavaScript challenges
    Mimicking human behavior
    Using proxy servers or VPNs

However, it's essential to note that scraping should be done responsibly and in accordance with website terms of service and applicable laws.

Playwright and aiohttp can help get around some anti-scraping measures, but it's essential to use these techniques responsibly and in accordance with website terms of service and applicable laws. Here are some ways to bypass certain measures:
1. Rate Limiting

    Use aiohttp's ClientSession with a reasonable timeout and conn_timeout to avoid overwhelming the server.
    Implement exponential backoff to retry requests after a delay.

2. CAPTCHAs

    Use playwright to render the CAPTCHA and extract the image.
    Utilize CAPTCHA-solving services or libraries like pytesseract.

3. JavaScript Challenges

    Use playwright to execute JavaScript code and complete challenges.
    Employ libraries like js2py to execute JavaScript code in Python.

4. IP Blocking

    Rotate IP addresses using aiohttp's Proxy support or external proxy services.
    Utilize VPNs or residential proxy networks.

5. User-Agent Blocking

    Rotate User-Agents using aiohttp's headers parameter or external libraries like fake-useragent.
    Mimic browser fingerprints using playwright's browser_context options.

6. Honeypot Traps

    Avoid triggering honeypot traps by not accessing decoy pages or links.
    Use playwright to inspect page content and detect honeypot traps.

7. Browser Fingerprinting

    Use playwright to mimic browser fingerprints by setting browser_context options.
    Employ libraries like browser-fingerprint to generate fake fingerprints.

8. Cookie-Based Validation

    Use aiohttp's CookieJar to store and reuse cookies.
    Employ playwright to set cookies using browser_context options.

9. Token-Based Validation

    Extract tokens from page content using playwright's page.query_selector.
    Reuse tokens in subsequent requests using aiohttp's headers parameter.

10. Machine Learning-Based Detection

    Avoid triggering machine learning-based detection by mimicking human behavior.
    Employ libraries like scrapy-splash to render pages and avoid detection.

Remember, these techniques should be used responsibly and in accordance with website terms of service and applicable laws. Always respect website owners' rights and avoid overwhelming their servers.


Here are some great scraping patterns using Playwright, aiohttp, and asyncio:
1. Concurrent Requests
Use asyncio.gather to send multiple requests concurrently with aiohttp.
Python

async def fetch_pages(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_page(session, url) for url in urls]
        pages = await asyncio.gather(*tasks)
        return pages

async def fetch_page(session, url):
    async with session.get(url) as response:
        return await response.text()

2. Playwright Browser Context
Use Playwright's browser context to manage multiple pages and avoid conflicts.
Python

async def scrape_pages(urls):
    async with async_playwright() as p:
        browser_context = await p.chromium.launchPersistentContext()
        pages = []
        for url in urls:
            page = await browser_context.newPage()
            await page.goto(url)
            pages.append(page)
        return pages

3. Rotate User-Agents
Rotate User-Agents using aiohttp's headers parameter.
Python

user_agents = ['UA1', 'UA2', 'UA3']

async def fetch_page(session, url):
    headers = {'User-Agent': random.choice(user_agents)}
    async with session.get(url, headers=headers) as response:
        return await response.text()

4. Handle Pagination
Handle pagination by extracting next page links and recursively scraping.
Python

async def scrape_pages(url):
    async with async_playwright() as p:
        browser_context = await p.chromium.launchPersistentContext()
        page = await browser_context.newPage()
        await page.goto(url)
        while True:
            next_page_link = await page.query_selector('a.next-page')
            if not next_page_link:
                break
            await page.click('a.next-page')
            await page.wait_for_load_state('networkidle')
        return page

5. Handle Anti-Scraping Measures
Handle anti-scraping measures like CAPTCHAs using Playwright.
Python

async def solve_captcha(page):
    await page.click('button[data-captcha]')
    await page.wait_for_selector('iframe[src*="captcha"]')
    captcha_iframe = await page.query_selector('iframe[src*="captcha"]')
    await captcha_iframe.click()
    # Solve CAPTCHA using OCR or other methods

6. Respect Website Terms
Respect website terms by adding delays between requests.
Python

async def fetch_pages(urls):
    async with aiohttp.ClientSession() as session:
        for url in urls:
            await session.get(url)
            await asyncio.sleep(1)  # Add 1-second delay

These patterns will help you build efficient and respectful scraping workflows using Playwright, aiohttp, and asyncio.

    
"""

# basic playwright use case:
async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://example.com")
        print(await page.title())
        await browser.close()

        

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://example.com")

        # Take a screenshot of the page
        await page.screenshot(path="example.png")

        # Get the HTML content of the page
        html = await page.content()
        print(html)

        # Get the title of the page
        title = await page.title()
        print(title)

        # Close the browser
        await browser.close()

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    url = "https://example.com"
    html = await fetch(url)
    print(html)

asyncio.run(main())