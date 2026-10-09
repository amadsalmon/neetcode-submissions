class TimeMap:
    def __init__(self):
        self.cache = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.cache:
            self.cache[key] = {}
        self.cache[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.cache:
            return ""
        if timestamp in self.cache[key]:
            return self.cache[key][timestamp]
        else:
            latest_idx = -1
            latest_val = ""
            for t, value in self.cache[key].items():
                if t <= timestamp:
                    latest_timestamp = t
                    latest_val = value
            return latest_val

                
