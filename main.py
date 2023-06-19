import requests

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    example_url = 'https://petstore.swagger.io/#'
    response_example = requests.get(example_url + "/pet/findByStatus", )
    print(response_example.raw)
    doggo_data = {
  "id": 144654779853,
  "category": {
    "id": 144654779853,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 144654779853,
      "name": "string"
    }
  ],
  "status": "available"
}
    response_post_example = requests.post(example_url + "/pet", doggo_data)
    print(response_post_example)
    iss_example_url = "http://api.open-notify.org/iss-now.json"
    iss_get_example = requests.get(iss_example_url)
    print(iss_get_example.text)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
