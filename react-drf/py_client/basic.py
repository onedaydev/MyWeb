import requests

# endpoint = "http://127.0.0.1:8000/todo/1/"
# get_response = requests.get(endpoint)
# print(get_response.text)

# endpoint = "http://127.0.0.1:8000/todo/2/"
# test_data = {'title':'test2','description':'test2'}
# put_response = requests.put(endpoint, data=test_data)
# print(put_response)

endpoint = "http://127.0.0.1:30080/todo/"
test_data = {'label':'test1','description':'test1'}
post_response = requests.post(endpoint, data=test_data)
print(post_response)

# endpoint = "http://127.0.0.1:8000/logout/"
# post_response = requests.post(endpoint)
# print(post_response)


######################################################
# Login Test

# from requests_toolbelt import MultipartEncoder
# import requests

# endpoint = "http://127.0.0.1:8000/posts/"

# mp_encoder = MultipartEncoder(
#     fields={
#         'title':'post test',
#         'body':'post test is it work?'
#     }
# )
# r = requests.post(
#     endpoint,
#     data=mp_encoder,
#     headers={'Content-Type': mp_encoder.content_type,'Authorization': 'Token 0c95d73337cd62043fc4f169109c695cd55033b3'}
# )
############################################################

