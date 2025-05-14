import requests

def get_user_info(email: str, phone: str):
    userInfo = f"Return user information : \nPhone - {phone}\n Email - {email}"

    lucky_number_url = "https://www.randomnumberapi.com/api/v1.0/random?min=1&max=10&count=1"

    response = requests.get(url=lucky_number_url)

    if response.status_code == 200:
        return {
            "statusCode": 200,
            "userInfo": userInfo,
            "luckyNumber": response.json()[0],
        }
        
    else:
        return {
            "statusCode": 500
        }
    