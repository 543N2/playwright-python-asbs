
def test_api_get_1(playwright):
    
    request = playwright.request.new_context()
    response = request.get("https://jsonplaceholder.typicode.com/posts/1",
                           headers={"Accept": "application/json"})
    assert response.status == 200
    json_data = response.json()
    print(json_data)
    assert json_data["id"] == 1
    request.dispose()
    print("Test completed")
    
    
def test_api_get_2(playwright):
    
    request = playwright.request.new_context(
        extra_http_headers={
            "Accept": "application/json",
            "Authorization": "Bearer YOUR_ACCESS_TOKEN",
            "X-Api-Key": "reqres-free-v1"
        }
    )
    
    response = request.get("https://reqres.in/api/users?page=2")
    
    assert response.status == 200
    json_data = response.json()
    print(json_data)
    assert json_data["data"][3]["first_name"] == "Byron"
    assert json_data["data"][4]["last_name"] == "Edwards"
    
    request.dispose()
    print("Test completed successfully.")