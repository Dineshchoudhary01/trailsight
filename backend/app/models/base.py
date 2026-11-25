from datetime import datetime, timezone


def utcnow() -> datetime:
    """Hamesha UTC mein time. DB mein timestamps UTC hi store hote hain."""
    return datetime.now(timezone.utc)