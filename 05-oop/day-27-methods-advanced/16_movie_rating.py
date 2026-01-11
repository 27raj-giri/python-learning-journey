# Create a Movie class with rating. Add method to check if movie is "Good" (rating > 7) or "Average".

class Movie:
    def __init__ (self, title, rating):
        self.title = title
        self.rating = rating

    def check_quality(self):
        if self.rating > 7:
            return "Good Movie"
        
        else:
            return "Average Movie"
        
m1 = Movie("Bahubali", 9)
m2 = Movie("BaliBahu", 4)

print(f"{m1.title} is a {m1.check_quality()}")
print(f"{m2.title} is a {m2.check_quality()}")