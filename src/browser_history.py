class BrowserHistory:
    def __init__(self, homepage: str):
        self.undo = []
        self.redo = []
        self.undo.append(homepage)  # Fix: Use self.undo instead of undo

    def visit(self, url: str) -> None:
        self.undo.append(url)  # Fix: Use self.undo
        self.redo.clear()  # Fix: Use self.redo

    def back(self, steps: int) -> str:
        while steps > 0 and len(self.undo) > 1:  # Fix: Use self.undo
            self.redo.append(self.undo.pop())  # Fix: Use self.redo
            steps -= 1  # Fix: Use steps instead of step
        return self.undo[-1] 

    def forward(self, steps: int) -> str:
        while steps > 0 and len(self.redo) != 0:  # Fix: Use self.redo
            self.undo.append(self.redo.pop())  # Fix: Use self.undo
            steps -= 1  # Fix: Use steps instead of step
        return self.undo[-1]


# Testing the implementation
if __name__ == "__main__":
    obj = BrowserHistory("google.com")
    obj.visit("youtube.com")
    obj.visit("facebook.com")
    obj.visit("twitter.com")

    print(obj.back(1))  # Should return "facebook.com"
    print(obj.back(1))  # Should return "youtube.com"
    print(obj.forward(1))  # Should return "facebook.com"
    
    obj.visit("linkedin.com")  # Clears forward history
    print(obj.forward(2))  # Should return "linkedin.com"
    print(obj.back(2))  # Should return "google.com"
