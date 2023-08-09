class OwnException(Exception):
    pass


class LevelError(OwnException):
    def __init__(self, us_level, adm_level):
        self.us_level = us_level
        self.adm_level = adm_level 

    def __str__(self):
        return f'Ошибка уровя доступа. Уровень доступа должен быть больше ({self.adm_level})'


class NotAllowedError(OwnException):
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def __str__(self):
        return f'У пользователя {self.name} нет доступа'
    

class AdminError(OwnException):
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def __str__(self):
        return f'Нет такого администратора ({self.name})'
