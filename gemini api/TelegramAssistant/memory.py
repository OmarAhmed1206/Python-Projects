from DB_server import get_history, create_users, get_users,add_message




def ensure_user(telegram_id, first_name, username):

    user = get_users(telegram_id)
    created = False
    if user is None:
        create_users(telegram_id,first_name,username)
        user = get_users(telegram_id)
        created = True

    return user, created


def save_user_message(user_id, text):
    add_message(user_id,"user",text)


def save_assistant_message(user_id, text):
    add_message(user_id,"assistant",text)


def load_history(user_id):
    return get_history(user_id)


def clear_user_history(user_id):
    clear_user_history(user_id)


