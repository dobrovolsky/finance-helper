from model.models import User, Category, Item


class ModelWrapper:
    @staticmethod
    def add_user(first_name, last_name, email, phone=None):
        return User(first_name=first_name, last_name=last_name, email=email, phone=phone)

    @staticmethod
    def add_category(name, user_id, description=None):
        if name == '':
            raise ValueError('Category has to have name')
        return Category(name=name, user_id=user_id, description=description)

    @staticmethod
    def add_item(name, price, count, category_id, user_id, date, description=None):
        return Item(name=name, price=price, date=date,user_id=user_id, count=count, category_id=category_id, description=description)

