# import sys
# import os
# import aiohttp
# import asyncio
# from faker import Faker
 
# # Add project root to Python path
# project_root = os.path.abspath(
#     os.path.join(os.path.dirname(__file__), '..', '..')
# )
 
# sys.path.append(project_root)
# from src.configurations.conf import Conf


# async def user_service(url, id, session):
#     user_service_url = url + "/users"+"/"+str(id)
#     print(user_service_url)
#     async with session.get(user_service_url) as response:
#         if response.status == 200:
#             user_data = await response.json()
#             user_data = {
#                 "id" : user_data["id"],
#                 "name" : user_data["name"],
#                 "email" : user_data["email"],
#             }
#             return user_data
#         else:
#             print(f"Failed to fetch user data. Status code: {response.status}")
#             return None

# async def post_service(url, id, session):#functional level async function to fetch post data from the post service
#     post_service_url = url + "/posts"+"/"+str(id)
#     print(post_service_url)
#     async with session.get(post_service_url) as response:#async created within function to make the http request to the post service
#         if response.status == 200:
#             post_data = await response.json()
#             post_data = {
#                 "id" : post_data["id"],
#                 "title" : post_data["title"],
#                 "body" : post_data["body"]
#             }
#             return post_data
#         else:
#             print(f"Failed to fetch post data. Status code: {response.status}")
#             return None
    
# async def album_service(url, id, session):
#     album_service_url = url + "/albums"+"/"+str(id)
#     print(album_service_url)
#     async with session.get(album_service_url) as response:
#         if response.status == 200:
#             album_data = await response.json()
#             album_data = {
#                 "userId" : album_data["userId"],
#                 "id" : album_data["id"],
#                 "title" : album_data["title"],
#             }
#             return album_data
#         else:
#             print(f"Failed to fetch album data. Status code: {response.status}")
#             return None

# async def photos_service(url, id, session):
#     photos_service_url = url + "/photos"+"/"+str(id)
#     print(photos_service_url)
#     async with session.get(photos_service_url) as response:
#         if response.status == 200:
#             photos_data = await response.json()
#             photos_data = {
#                 "albumId" : photos_data["userId"],
#                 "id" : photos_data["id"],
#                 "title" : photos_data["title"],
#                 "url": photos_data["url"],
#                 "thumbnailUrl": photos_data["thumbnailUrl"]
#             }
#             return photos_data
#         else:
#             print(f"Failed to fetch album data. Status code: {response.status}")
#             return None

# async def dashboard(url):
#     async with aiohttp.ClientSession() as session:
#         #concurrently fetch data from all services using asyncio.gather
#         user_data,post_data,album_data,photos_data = await asyncio.gather(
#             user_service(url, 1, session),
#             post_service(url, 1, session),
#             album_service(url, 1, session),
#             photos_service(url, 1, session)
#         )

#         dashboard_data = {
#             "user": user_data,
#             "post": post_data,
#             "album": album_data,
#             "photos": photos_data
#         }
#         return dashboard_data
# if __name__ == "__main__":
#     conf = Conf()
#     print(conf.url)
#     try:
#         results = asyncio.run(dashboard(conf.url))
#         print(results)
#     except aiohttp.ClientError as e:
#         print(f"An HTTP error occurred: {e}")#specific exception

#     except Exception as e:
#         print(f"An error occurred: {e}")
    
import sys 
import os
import aiohttp
import asyncio
 
project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..')
)
sys.path.append(project_root)
from src.configurations.conf import Conf 
 
async def user_service(url, id, session):
    user_service_url = f"{url}/users/{id}"
    print(user_service_url)
    async with session.get(user_service_url) as response:
        if response.status == 200:
            user_data = await response.json()
            return {
                "id": user_data["id"],
                "name": user_data["name"],
                "email": user_data["email"]
            }
        else:
            print(f"Failed to fetch user data. Status code: {response.status}")
            return None
 
async def post_service(url, id, session):
    post_service_url = f"{url}/posts/{id}"
    print(post_service_url)
    async with session.get(post_service_url) as response:
        if response.status == 200:
            post_data = await response.json()
            return {
                "id": post_data["id"],
                "title": post_data["title"],
                "body": post_data["body"]
            }
        else:
            print(f"Failed to fetch post data. Status code: {response.status}")
            return None
 
async def album_service(url, id, session):
    album_service_url = f"{url}/albums/{id}"
    print(album_service_url)
    async with session.get(album_service_url) as response:
        if response.status == 200:
            album_data = await response.json()
            return {
                "user_id": album_data["userId"],
                "id": album_data["id"],
                "title": album_data["title"]
            }
        else:
            print(f"Failed to fetch album data. Status code: {response.status}")
            return None
 
async def photo_service(url, id, session):
    photo_service_url = f"{url}/photos/{id}"
    print(photo_service_url)
    async with session.get(photo_service_url) as response:
        if response.status == 200:
            photo_data = await response.json()
            return {
                "album_id": photo_data["albumId"],
                "id": photo_data["id"],
                "title": photo_data["title"],
                "url": photo_data["url"],
                "thumbnail_url": photo_data["thumbnailUrl"]
            }
        else:
            print(f"Failed to fetch photo data. Status code: {response.status}")
            return None
 
async def dashboard_service(url):
    async with aiohttp.ClientSession() as session:
        # Run all requests in parallel
        user_data, post_data, album_data, photo_data = await asyncio.gather(
            user_service(url, 1, session),
            post_service(url, 1, session),
            album_service(url, 1, session),
            photo_service(url, 1, session)
        )
        dashboard_data = {
            "user": user_data,
            "post": post_data,
            "album": album_data,
            "photo": photo_data
        }
        return dashboard_data
 
if __name__ == "__main__":
    Conf = Conf()
    print(f"Connecting to: {Conf.url}")
    try:
        # Use standard asyncio.run
        result = asyncio.run(dashboard_service(Conf.url))
        print("\nDashboard Data Results:")
        print(result)
    except aiohttp.ClientError as e:
        print(f"HTTP error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")