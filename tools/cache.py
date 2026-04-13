import os
import functools
import json
import hashlib
from diskcache import Cache
from config.logger import logger
from dotenv import load_dotenv

load_dotenv()

# Global default TTL from environment
DEFAULT_EXPIRE = int(os.getenv("TOOL_CACHE_EXPIRE", 86400))

# Initialize a persistent cache in the .cache directory of the project root
CACHE_DIR = os.path.join(os.getcwd(), ".cache", "tool_results")
cache = Cache(CACHE_DIR)

def tool_cache(expire=None):
    """
    A decorator to cache tool results based on their arguments.
    Works with functions that return strings (standard for CrewAI tools).
    """
    effective_expire = expire if expire is not None else DEFAULT_EXPIRE
    
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Create a unique key based on function name and arguments
            # We hash the key to keep it manageable and safe for diskcache
            arg_str = json.dumps({"args": args, "kwargs": kwargs}, sort_keys=True)
            key_raw = f"{func.__name__}:{arg_str}"
            key = hashlib.md5(key_raw.encode()).hexdigest()
            
            # Check cache
            cached_result = cache.get(key)
            if cached_result is not None:
                logger.info(f"💾 Cache hit for {func.__name__}")
                return cached_result
            
            # Call the actual function
            logger.debug(f"🔍 Cache miss for {func.__name__}. Executing...")
            result = func(*args, **kwargs)
            
            # Store in cache
            cache.set(key, result, expire=effective_expire)
            return result
        return wrapper
    return decorator
