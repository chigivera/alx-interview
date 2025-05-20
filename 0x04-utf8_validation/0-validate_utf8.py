#!/usr/bin/python3
"""
UTF-8 Validation Module
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    
    Args:
        data (list): List of integers representing bytes
        
    Returns:
        bool: True if data is valid UTF-8 encoding, False otherwise
    """
    # Number of bytes in the current UTF-8 character
    num_bytes = 0
    
    # Masks for checking the most significant bits
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000
    
    for num in data:
        # Get the 8 least significant bits
        byte = num & 0xFF
        
        # If this is the start of a new character
        if num_bytes == 0:
            # Count the number of leading 1s
            mask = 1 << 7
            while mask & byte:
                num_bytes += 1
                mask >>= 1
            
            # If no leading 1s, it's a single byte character
            if num_bytes == 0:
                continue
            
            # UTF-8 characters can only be 1-4 bytes long
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Check if this is a continuation byte (starts with 10)
            if not (byte & mask1 and not (byte & mask2)):
                return False
        
        # Decrease the number of bytes remaining
        num_bytes -= 1
    
    # If we have remaining bytes, the sequence is incomplete
    return num_bytes == 0 