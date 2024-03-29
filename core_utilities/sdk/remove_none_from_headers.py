from typing import Dict, Optional


def remove_none_from_headers(headers: Dict[str, Optional[str]]) -> Dict[str, str]:
    new_headers: Dict[str, str] = {}
    for header_key, header_value in headers.items():
        if header_value is not None:
            new_headers[header_key] = header_value
    return new_headers
