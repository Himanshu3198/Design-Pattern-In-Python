import time
import threading

"""A simple key-value store with expiration."""


class KeyValue:
    def __init__(self):
        self.key_store = {}
        self.ttl_tracker = {}
        self.lock = threading.Lock()
        self.cleanup_thread = threading.Thread(target=self.clean_expire, daemon=True)
        self.cleanup_thread.start()

    def add(self, key, value, ttl):
        with self.lock:
            self.key_store[key] = value
            print("Key has been set: ", key)
            self.ttl_tracker[key] = time.time() + ttl

    def get(self, key):
        with self.lock:
            if key not in self.key_store:
                return "No key Found"
            return f"returning the key: {self.key_store[key]}"

    def remove_key(self, key):
        with self.lock:
            if key not in self.key_store:
                return "No key Found to remove"
            del self.key_store[key]
            del self.ttl_tracker[key]

    def clean_expire(self):
        while True:
          time.sleep(1)
          deleted_key = []
          current_time = time.time()
          with self.lock:

            for key in self.ttl_tracker.keys():
                if current_time > self.ttl_tracker[key]:
                    deleted_key.append(key)
            for key in deleted_key:
                del self.key_store[key]
                print("expired key: ", key)
                del self.ttl_tracker[key]

    def display_key(self):
        with self.lock:
            if len(self.key_store) == 0:
                print("No key Found")
                return None
            for key in self.key_store:
                print(key, self.key_store[key])


my_key = KeyValue()

my_key.add(5, 25, 5)
my_key.add(10, 21, 5)
my_key.add(20, 25, 5)
my_key.add(6,18,10)
print(my_key.remove_key(5))
print(my_key.get(20))

my_key.display_key()
time.sleep(12)
my_key.display_key()
