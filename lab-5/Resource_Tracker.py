
resources = [
    [101, "Laptop", "Electronics", 8],
    [102, "Projector", "Electronics", 0],
    [103, "Whiteboard", "Classroom", 5],
    [104, "Microphone", "Audio", 3],
    [105, "Camera", "Electronics", 2]
]


def display_resources(resources):
    for r in resources:
        print(r)


def search_by_category(resources, category):
    for r in resources:
        if r[2] == category:
            print(r)


def find_unavailable(resources):
    for r in resources:
        if r[3] == 0:
            print(r)



print("All Resources:")
display_resources(resources)

print("Electronics Resources:")
search_by_category(resources, "Electronics")

print("Unavailable Resources:")
find_unavailable(resources)
