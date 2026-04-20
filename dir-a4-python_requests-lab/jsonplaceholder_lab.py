import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def separator(title):
    """pretty print: take title, print it, and also print 50 = for the visibility"""
    print("\n")
    print(f"{'='*50}")
    print(f"    {title}")
    print('='*50)


# ─────────────────────────────────────────────
# 1. GET ALL POSTS
# ─────────────────────────────────────────────
separator("1. GET ALL POSTS")

response = requests.get(f"{BASE_URL}/posts")
print(f"Status Code: {response.status_code}")
posts = response.json()
# why need .json():
# "response" holds the raw HTTP response (status code, headers, body as bytes/text). The body arrives as a plain string of text that happens to look like JSON.
# .json() parses that string into a Python dict/list so you can use posts[0], user['name'], etc.
# Without it:
# response.text   # → '[ {"userId": 1, "id": 1, "title": "..." }, ...]'  ← just a string
# response.json() # → [ {"userId": 1, "id": 1, "title": "..."}, ...]     ← actual Python list
print(f"Total posts: {len(posts)}")
print(f"First post: {posts[0]}")

# ─────────────────────────────────────────────
# 2. GET A SINGLE POST (by ID)
# ─────────────────────────────────────────────
separator("2. GET A SINGLE POST (id=1)")

response = requests.get(f"{BASE_URL}/posts/1")
print(f"Status Code: {response.status_code}")
print(f"Post: {response.json()}")

# ─────────────────────────────────────────────
# 3. GET POSTS WITH QUERY PARAMS (filter by userId)
# ─────────────────────────────────────────────
separator("3. GET POSTS BY USER ID (userId=1)")

params = {"userId": 1}
response = requests.get(f"{BASE_URL}/posts", params=params)
print(f"Status Code: {response.status_code}")
user_posts = response.json()
print(f"Posts by userId=1: {len(user_posts)}")
print(f"First post: {user_posts[0]}")
# params is a requests.get() keyword argument that appends a query string to the URL automatically.
# Instead of manually building ?userId=1, you pass a dict and requests handles the encoding — including proper URL-escaping for special characters or multiple values.
# ─────────────────────────────────────────────
# 4. GET COMMENTS FOR A POST
# ─────────────────────────────────────────────
separator("4. GET COMMENTS FOR POST (postId=1)")

response = requests.get(f"{BASE_URL}/posts/1/comments")
print(f"Status Code: {response.status_code}")
comments = response.json()
print(f"Total comments: {len(comments)}")
print(f"First comment: {comments[0]}")

# ─────────────────────────────────────────────
# 5. POST - CREATE A NEW POST
# ─────────────────────────────────────────────
separator("5. CREATE A NEW POST (POST)")

new_post = {
    "title": "My New Post",
    "body": "This is the body of my new post",
    "userId": 1
}
response = requests.post(f"{BASE_URL}/posts", json=new_post)
# if not use "json" word above should do:
# Manual equivalent — more verbose:
#    import json
#    requests.post(url, data=json.dumps(new_post), headers={"Content-Type": "application/json"})
#    instead: "requests" module give us those 2 functions: 1. serialize dict to JSON, 2. sets header on the request.
print(f"Status Code: {response.status_code}")  # 201 Created
print(f"Created Post: {response.json()}")

# ─────────────────────────────────────────────
# 6. PUT - UPDATE AN ENTIRE POST
# ─────────────────────────────────────────────
separator("6. UPDATE A POST (PUT id=1)")

updated_post = {
    "id": 1,
    "title": "Updated Title",
    "body": "Updated body content",
    "userId": 1
}
response = requests.put(f"{BASE_URL}/posts/1", json=updated_post)
print(f"Status Code: {response.status_code}")  # 200 OK
print(f"Updated Post: {response.json()}")

# ─────────────────────────────────────────────
# 7. PATCH - PARTIALLY UPDATE A POST
# ─────────────────────────────────────────────
separator("7. PATCH A POST (PATCH id=1)")

patch_data = {
    "title": "Only the Title Changed"
}
response = requests.patch(f"{BASE_URL}/posts/1", json=patch_data)
print(f"Status Code: {response.status_code}")  # 200 OK
print(f"Patched Post: {response.json()}")

# ─────────────────────────────────────────────
# 8. DELETE A POST
# ─────────────────────────────────────────────
separator("8. DELETE A POST (id=1)")

response = requests.delete(f"{BASE_URL}/posts/1")
print(f"Status Code: {response.status_code}")  # 200 OK
print(f"Response body (empty = success): {response.json()}")

# ─────────────────────────────────────────────
# 9. GET ALL USERS
# ─────────────────────────────────────────────
separator("9. GET ALL USERS")

response = requests.get(f"{BASE_URL}/users")
print(f"Status Code: {response.status_code}")
users = response.json()
print(f"Total users: {len(users)}")
print(f"First user name: {users[0]['name']}")

# ─────────────────────────────────────────────
# 10. GET A SINGLE USER
# ─────────────────────────────────────────────
separator("10. GET A SINGLE USER (id=1)")

response = requests.get(f"{BASE_URL}/users/1")
print(f"Status Code: {response.status_code}")
user = response.json()
print(f"Name: {user['name']}")
print(f"Email: {user['email']}")
print(f"City: {user['address']['city']}")

# ─────────────────────────────────────────────
# 11. GET ALL TODOS
# ─────────────────────────────────────────────
separator("11. GET ALL TODOS")

response = requests.get(f"{BASE_URL}/todos")
print(f"Status Code: {response.status_code}")
todos = response.json()
print(f"Total todos: {len(todos)}")

# ─────────────────────────────────────────────
# 12. GET COMPLETED TODOS (filter by completed)
# ─────────────────────────────────────────────
separator("12. GET COMPLETED TODOS")

params = {"completed": "true"}
response = requests.get(f"{BASE_URL}/todos", params=params)
print(f"Status Code: {response.status_code}")
completed = response.json()
print(f"Completed todos: {len(completed)}")
print(f"Example: {completed[0]}")

# ─────────────────────────────────────────────
# 13. CHECK RESPONSE HEADERS
# ─────────────────────────────────────────────
separator("13. INSPECT RESPONSE HEADERS")

response = requests.get(f"{BASE_URL}/posts/1")
print(f"Content-Type : {response.headers.get('Content-Type')}")
print(f"Server       : {response.headers.get('Server')}")
print(f"X-Powered-By : {response.headers.get('X-Powered-By')}")

# ─────────────────────────────────────────────
# 14. SEND CUSTOM HEADERS
# ─────────────────────────────────────────────
separator("14. SEND REQUEST WITH CUSTOM HEADERS")

custom_headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer fake-token-12345"
}
response = requests.get(f"{BASE_URL}/posts/1", headers=custom_headers)
# "headers" is requests.get(...) preserve keyword. injects these into the outgoing HTTP request. The server reads them to decide how to respond — e.g., rejecting if the token is invalid, or parsing the body as JSON.
print(f"Status Code: {response.status_code}")
print(f"Post title: {response.json()['title']}")

print("\n✅ All requests completed successfully!")
