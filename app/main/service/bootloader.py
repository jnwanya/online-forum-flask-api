from ..model.role import Role, RoleConstant
from ..model.post_category import PostCategory


class BootLoader:
    __category_list = [
        {'name': 'General', 'description': 'For all general posting'},
        {'name': 'Politics', 'description': 'For issues and discussion related to politics'},
        {'name': 'Career', 'description': 'For description about careers and job opportunities'},
        {'name': 'Entertainers', 'description': 'For funny and entertaining post. be it music, jokes, comedy'},
    ]
    @classmethod
    def __create_roles(cls):
        role_list = [name for name in dir(RoleConstant) if not name.startswith('_')]
        for role_name in role_list:
            if not Role.find_by_name(role_name):
                role = Role(role_name)
                role.save()

    @classmethod
    def __create_post_categories(cls):
        for category in cls.__category_list:
            print(category)
            if not PostCategory.find_by_name(category['name']):
                post_category = PostCategory(**category)
                post_category.save()

    @classmethod
    def setup_app_data(cls):
        cls.__create_roles()
        cls.__create_post_categories()

