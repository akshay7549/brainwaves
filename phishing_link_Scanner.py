import re
import requests

# Function to check URL structure for suspicious patterns
def check_url_pattern(url):
    phishing_patterns = [
        r"http:\/\/\d+\.\d+\.\d+\.\d+",  # URLs with IP addresses
        r"http[s]?:\/\/(\w+\.)*free.*",      # URLs with 'free'
        r"http[s]?:\/\/(\w+\.)*bonus.*",     # URLs with 'bonus'
        r"http[s]?:\/\/(\w+\.)*login.*"      # URLs with 'login'
    ]

    for pattern in phishing_patterns:
        if re.search(pattern, url):
            return True
    return False

# Function to check URL against Google Safe Browsing API (requires API key)
def check_with_google_safebrowsing(url):
    api_key = "YOUR_GOOGLE_SAFE_BROWSING_API_KEY"  # Replace with your API key
    endpoint = f"https://safebrowsing.googleapis.com/v4/threatMatches:find?key={api_key}"

    payload = {
        "client": {
            "clientId": "phishing-scanner",
            "clientVersion": "1.0"
        },
        "threatInfo": {
            "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING"],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [
                {"url": url}
            ]
        }
    }

    try:
        response = requests.post(endpoint, json=payload)
        if response.status_code == 200:
            result = response.json()
            if "matches" in result:
                return True  # Malicious URL detected
    except requests.exceptions.RequestException as e:
        print(f"Error while contacting API: {e}")

    return False

# Main function to classify the URL
def classify_url(url):
    if check_url_pattern(url):
        return "Suspicious: Matches phishing patterns"

    if check_with_google_safebrowsing(url):
        return "Malicious: Detected by Google Safe Browsing"

    return "Safe: No issues detected"

# Entry point for testing URLs
def test_urls():
    test_data = [
        "http://192.168.1.1",              # Suspicious: IP-based URL
        "https://example.com/free-offer",  # Suspicious: Contains 'free'
        "https://safe-site.com",           # Safe: Normal URL
        "https://login.fakebank.com",      # Suspicious: Contains 'login'
        "http://bonus-example.com"         # Suspicious: Contains 'bonus'
    ]

    print("Phishing Link Scanner Test Results")
    for url in test_data:
        print(f"URL: {url}")
        result = classify_url(url)
        print(f"Result: {result}\n")

if __name__ == "__main__":
    test_urls()
