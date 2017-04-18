from model.models import User, Category, Item


class ModelWrapper:
    @staticmethod
    def add_user(first_name, last_name, email, phone=None):
        return User(first_name=first_name, last_name=last_name, email=email, phone=phone)

    @staticmethod
    def add_category(name, description=None):
        return Category(name=name, description=description)

    @staticmethod
    def add_item(name, price, count, category_id, description=None):
        return Item(name=name, price=price, count=count, category_id=category_id, description=description)

    @staticmethod
    def add_item_list(date, item_id, user_id):
        return User(date=date, item_id=item_id, user_id=user_id)
