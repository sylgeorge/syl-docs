# student_scores = {
#  "Harry": 81,
#  "Ron": 78,
#  "Hermione": 99,
#  "Draco": 74,
#  "Neville": 62,
# }

# students_grades = {}
# for student in student_scores:
#  score = student_scores[student]
#  if score > 90:
#    students_grades[student] = "Outstanding"
#  elif score > 80:
#    students_grades[student] = "Exceeds Expectation"
#  elif score >70:
#    students_grades[student] = "Acceptable"
#  else:
#    students_grades[student] = "Fail"
# print(students_grades)  

travel_log = [
 {
  "country":"france", 
  "cities_visited": ["paris", "lille", "dijon"], 
  "total_visits": 12
 },
 {"country":"germany", 
  "cities_visited": ["berlin", "hamburg", "stuttgart"], 
  "total_visits": 15
 },]

def add_country(country_visited, cities, visits):
 new_country = {}
 new_country["country"] = country_visited
 new_country["cities_visited"] = cities
 new_country["total_visits"] = visits
 travel_log.append(new_country)

add_country(country_visited = "nigeria", cities = ["lagos", "ibadan", "enugu"], visits = 7)
print(travel_log)


