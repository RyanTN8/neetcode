class TimeMap:

    def __init__(self):
        self.hashMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        #if key in hashMap, add (timestamp, value) to hashMap list
        #if key not in hashMap, make list with (timestamp, value)
        if key in self.hashMap:
            self.hashMap[key].append((value, timestamp))
        else:
            self.hashMap[key] = [(value, timestamp)]
        print(value)

    def get(self, key: str, timestamp: int) -> str:
        if key in self.hashMap:
            arr = self.hashMap[key]
        else:
            return ""
        l = 0
        r = len(arr) - 1
        if arr[0][1] <= timestamp:
            result = arr[0][0]
        else:
            return ""

        while l <= r:
            mid = (l + r) // 2
            if timestamp == arr[mid][1]:
                return arr[mid][0]

            if timestamp < arr[mid][1]:
                r = mid - 1
            elif timestamp > arr[mid][1]:
                l = mid + 1
                result = arr[mid][0]
        
        return result
