import re

def parse_micr(micr_line: str):
    match = re.match(r"\|:(\d+)\|\s*(\d+)\s*\|\s*(\d+)", micr_line)
    if match:
        return {
            "routing": match.group(1),
            "account": match.group(2),
            "check_number": match.group(3)
        }
    return None