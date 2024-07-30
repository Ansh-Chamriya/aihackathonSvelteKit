import re

def retrieve_symbol(query):
    pattern=re.compile('"trading_symbol":\s*"([^"]*)"')
    matches = pattern.findall(query)
    return matches
