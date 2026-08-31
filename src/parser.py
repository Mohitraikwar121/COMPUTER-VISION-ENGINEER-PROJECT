import re

def parse_scoreboard(text):
    # Extract TARUN and numbers
    match = re.search(r'TARUN.*?(\d+)\s*[|/]\s*(\d+)\s*[|/]\s*(\d+)', text)
    if match:
        return {
            'player': 'TARUN',
            'runs': match.group(1),
            'balls': match.group(2),
            'fours': match.group(3)
        }
    
    # Extract overs
    overs = re.search(r'(\d+)\.\s*(\d+)', text)
    if overs:
        return {'overs': f"{overs.group(1)}.{overs.group(2)}"}
    
    return None