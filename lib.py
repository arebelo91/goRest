
import requests
from requests import Response
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='goRest.log', level=logging.INFO)

class goRestLib(object):

    def __init__(self,token: str | None):
        self.token=None
        if token:
            self.token = token
        self.baseUrl = "https://gorest.co.in/public/v2/"


    def validate_todo_schema(self, obj: object) -> None:
        #Validate obj type, keys, type of values 
        logger.info(f"Validating schema for {obj}")
        assert isinstance(obj,dict), "Object is not a dictionary"
        exp_keys = ["id","user_id","title","due_on","status"]
        act_keys = [x for x in obj.keys()]
        
        assert exp_keys == act_keys, "Object keys do not match schema"

        exp_val_type = [int,int,str,str,str]
        act_val_type = [type(x) for x in obj.values()]
    
        #Validate status is valid
        assert exp_val_type == act_val_type, "Object value types do not match schema"
        assert obj["status"] in ["pending", "completed"], "Status is not valid"
        logger.info("Schema is valid")

    def all_todo_completed(self) -> None:
        #List comprehension to extract status values 
        payload = self.get_todo_list().json()
        logger.info(f"Evaluate if all the following todos are completed: {payload}")
        statusList = [todo["status"] for todo in payload]
        #Assert all equal to completed
        assert all(x == "completed" for x in statusList), "There are todos to complete"
        

    def get_todo_list(self) -> Response:
        if self.token:
            payload = requests.get(f"{self.baseUrl}/todos?access-token={self.token}")
        else: 
            payload = requests.get(f"{self.baseUrl}/todos")
        return payload
    
    def get_users_list(self) -> Response:
        if self.token:
            payload = requests.get(f"{self.baseUrl}/users?access-token={self.token}")
        else: 
            payload = requests.get(f"{self.baseUrl}/users")
        return payload
    
    def get_comments_list(self) -> Response:
        if self.token:
            payload = requests.get(f"{self.baseUrl}/comments?access-token={self.token}")
        else: 
            payload = requests.get(f"{self.baseUrl}/comments")
        return payload
    
    def get_posts_list(self) -> Response:
        if self.token:
            payload = requests.get(f"{self.baseUrl}/posts?access-token={self.token}")
        else:
            payload = requests.get(f"{self.baseUrl}/posts")
        return payload
    
    def get_user_info(self, id: str) -> Response:
        if self.token:
            payload = requests.get(f"{self.baseUrl}/users/{id}?access-token={self.token}")
        else:
            payload = requests.get(f"{self.baseUrl}/users/{id}")
        return payload
    
    def get_user_id_by_name(self,name: str) -> str | None:
        payload= self.get_users_list().json()
        for p in payload:
            if p['name'] == name:
                return p['id']
        logger.warning(f"No user with name {name} was found")
        return None
    
    def create_user(self, body: dict) -> Response:
        payload = requests.post(url=f"{self.baseUrl}/users?access-token={self.token}", data=body)
        return payload
    
    def update_user_info(self, id: str, body: dict) -> Response:
        payload = requests.put(url=f"{self.baseUrl}/users/{id}?access-token={self.token}", data=body)
        return payload
    
    def delete_user(self, id: str) -> Response:
        payload = requests.delete(url=f"{self.baseUrl}/users/{id}?access-token={self.token}")
        return payload