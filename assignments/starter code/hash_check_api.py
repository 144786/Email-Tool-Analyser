def  file_is_malicious(file_path: str) -> bool:
    """
    Take the file at the path provided, hash it (SHA256), sent the hash to VirusTotal, and report whether comes
    back flagged as malware. 

    ***NOTE: to interact with VT's API, you will need an API key. Here it is:
    '3b6f919f8590692ff02fd1bd7136e2dc02ef1b2ccfe5392745ab5770d6c573a2'

    Args:
        file_path (string): 
        a string containing the path to the file to be hashed and checked by VirusTotal.

    Returns:
        bool: 
        True if VirusTotal flags the file as malicious, False otherwise.
    """
    # TODO
    pass
