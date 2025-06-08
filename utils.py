def censor_username(username):
    return "@********" if username else "Без ника"

def format_users(users):
    lines = []
    for idx, user in enumerate(users, start=1):
        lines.append(f"{idx}. {censor_username(user[2])}")
    return "\n".join(lines)
