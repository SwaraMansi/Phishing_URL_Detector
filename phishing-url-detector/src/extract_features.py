import re
import tldextract

def has_ip(url):
    """Check if URL contains an IP address instead of domain"""
    return 1 if re.search(r'\d+\.\d+\.\d+\.\d+', url) else 0

def extract_features(url):
    """Extract lexical & statistical URL features"""
    
    extracted = tldextract.extract(url)

    return {
        "url_length": len(url),
        "num_dots": url.count('.'),
        "num_slashes": url.count('/'),
        "num_hyphens": url.count('-'),
        "has_ip": has_ip(url),
        "special_chars": sum(1 for c in url if not c.isalnum()),
        "subdomain_length": len(extracted.subdomain),
        "domain_length": len(extracted.domain),
        "suffix_length": len(extracted.suffix)
    }
