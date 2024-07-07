import requests
import pytest
import logging

logger = logging.getLogger(__name__)



def test_validate_all_todo_schema(restLib):
    payload = restLib.get_todo_list().json()
    logger.info(f"Validate schema for following todo list: {payload}")
    for todo in payload:
        restLib.validate_todo_schema(todo)

def test_validate_all_status(restLib):
    restLib.all_todo_completed()

@pytest.mark.auth
def test_create_new_user(restLib,env):
    data = env["user_data"]
    logger.info(f"Will create new user with info {data}")
    response = restLib.create_user(data)
    assert response.status_code == 201, f"Status of response to create user is not 201. It is {response.status_code}"
    id = response.json()["id"]
    logger.info(f"New user has id {id}")
    data.update({'id': id})
    assert sorted(response.json()) == sorted(data), f"Body of response to create new user is not {data}. It is {response.json()}"

@pytest.mark.auth
def test_update_user(restLib, env):
    user_id = restLib.get_user_id_by_name('Linda Fenberg')
    data = env["user_data"]
    new_info= env["update_user_data"]
    data.update(new_info)
    logger.info(f"Will update user with id {user_id}. New info is {data}")
    response= restLib.update_user_info(id=user_id,body=data)
    assert response.status_code == 200, f"Status of response to update user {user_id} is not 200. It is {response.status_code}"
    data.update({'id': user_id})
    assert sorted(response.json()) == sorted(data), f"Body of response to update user {user_id} is not {data}. It is {response.json()}"


@pytest.mark.auth
def test_delete_user(restLib):
    user_id = restLib.get_user_id_by_name('Linda Fenberg')
    logger.info(f"Will delete user with id {user_id}.")
    response = restLib.delete_user(id=user_id)
    #Delete user
    assert response.status_code == 204, f"Status of response to delete user {user_id} is not 204. It is {response.status_code}"
    #Get user and check it is no longer present: 404 not found
    response = restLib.get_user_info(user_id)
    assert response.status_code == 404, f"Status code of response to get user {user_id} is not 404. It is {response.status_code}"
    logger.info(f"User {user_id} deleted")


