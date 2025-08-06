import streamlit as st
from urllib.parse import urlparse

st.title("🔐 PhishGuard - Phishing URL Detector")

url = st.text_input("Enter the URL to check:")

def is_phishing(url):
    phishing_signs = []
    if urlparse(url).hostname and urlparse(url).hostname.replace(".", "").isdigit():
        phishing_signs.append("❌ Uses IP address instead of domain name.")

    domain_parts = urlparse(url).hostname.split('.') if urlparse(url).hostname else []
    if len(domain_parts) > 3:
        phishing_signs.append("❌ Contains too many subdomains.")

    suspicious_keywords = ["login", "verify", "update", "bank", "secure", "account", "signin"]
    for keyword in suspicious_keywords:
        if keyword in url.lower():
            phishing_signs.append(f"⚠️ Suspicious keyword found: '{keyword}'")

    if phishing_signs:
        return False, phishing_signs
    else:
        return True, ["✅ No obvious phishing signs found. Still, be cautious!"]

if url:
    st.subheader("🔍 Analysis Result")
    is_safe, messages = is_phishing(url)
    for msg in messages:
        st.write(msg)
    if is_safe:
        st.success("✅ This URL appears to be safe.")
    else:
        st.error("🚨 This URL may be phishing!")
