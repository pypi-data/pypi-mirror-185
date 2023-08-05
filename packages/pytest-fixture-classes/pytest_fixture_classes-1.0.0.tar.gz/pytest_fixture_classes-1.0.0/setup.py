# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pytest_fixture_classes']

package_data = \
{'': ['*']}

install_requires = \
['pytest', 'typing-extensions>=4.4.0,<5.0.0']

setup_kwargs = {
    'name': 'pytest-fixture-classes',
    'version': '1.0.0',
    'description': 'Fixtures as classes that work well with dependency injection, autocompletetion, type checkers, and language servers',
    'long_description': '# Pytest Fixture Classes\n\nGive you the ability to write typed fixture classes that work well with dependency injection, autocompletetion, type checkers, and language servers.\n\nNo mypy plugins required!\n\n## Installation\n\n`pip install pytest-fixture-classes`\n\n## Usage\n\n### Quickstart\n\nThis is a quick and simple example of writing a very simplistic fixture class. You can, of course, add any methods you like into the class but I prefer to keep it a simple callable.\n\n```python\nfrom pytest_fixture_classes import fixture_class\nfrom collections.abc import Mapping\nimport requests\n\n\n# changing the name is optional and is a question of style. Everything will work correctly with the default name\n@fixture_class(name="my_fixture_class")\nclass MyFixtureClass:\n    existing_fixture1: Mapping[str, str]\n    existing_fixture2: requests.Session\n    existing_fixture3: Mapping[str, str | int | bool]\n\n    def __call__(self, name: str, age: int, height: int) -> dict[str, str | int | bool]:\n        ...\n\n\ndef test_my_code(my_fixture_class: MyFixtureClass):\n    some_value = my_fixture_class(...)\n    some_other_value = my_fixture_class(...)\n    one_more_value = my_fixture_class(...)\n\n    # Some testing code below\n    ...\n\n```\n\n### Rationale\n\nIf we want factory fixtures that automatically make use of pytest\'s dependency injection, we are essentially giving up any IDE/typechecker/language server support because such fixtures cannot be properly typehinted because they are returning a callable, not a value. And python is still pretty new to typehinting callables.\n\nSo we can\'t use ctrl + click, we don\'t get any autocompletion, and mypy/pyright won\'t warn us when we are using the factory incorrectly. Additionally, any changes to the factory\'s interface will require us to search for its usages by hand and fix every single one.\n\nFixture classes solve all of the problems I mentioned:\n\n* Autocompletion out of the box\n* Return type of the fixture will automatically be inferred by pyright/mypy\n* When the interface of the fixture changes or when you use it incorrectly, your type checker will warn you\n* Search all references and show definition (ctrl + click) also works out of the box\n\n### Usage scenario\n\nLet\'s say that we have a few pre-existing fixtures: `db_connection`, `http_session`, and `current_user`. Now we would like to write a new fixture that can create arbitrary users based on `name`, `age`, and `height` arguments. We want our new fixture, `create_user`, to automatically get our old fixtures using dependency injection. Let\'s see what such a fixture will look like:\n\n```python\nimport pytest\nimport requests\n\n@pytest.fixture\ndef db_connection() -> dict[str, str]:\n    ...\n\n@pytest.fixture\ndef http_session() -> requests.Session:\n    ...\n\n\n@pytest.fixture\ndef current_user() -> requests.Session:\n    ...\n\n\n@pytest.fixture\nasync def create_user(\n    db_connection: dict[str, str],\n    http_session: requests.Session,\n    current_user: requests.Session,\n) -> Callable[[str, int, int], dict[str, str | int | bool]]:\n    async def inner(name: str, age: int, height: int):\n        user = {...}\n        self.db_connection.execute(...)\n        if self.current_user[...] is not None:\n            self.http_session.post(...)\n        \n        return user\n\n    return inner\n\ndef test_my_code(create_user: Callable[[str, int str], dict[str, str | int | bool]]):\n    johny = create_user("Johny", 27, 183)\n    michael = create_user("Michael", 43, 165)\n    loretta = create_user("Loretta", 31, 172)\n\n    # Some testing code below\n    ...\n\n```\n\nSee how ugly and vague the typehints for create_user are? Also, see how we duplicate the return type and argument information? Additionally, if you had thousands of tests and if `test_my_code` with `create_user` were in different files, you would have to use plaintext search to find the definition of the fixture if you wanted to see how to use it. Not too nice.\n\nNow let\'s rewrite this code to solve all of the problems I mentioned:\n\n```python\nfrom pytest_fixture_classes import fixture_class\nfrom collections.abc import Mapping\nimport requests\nimport pytest\n\n\n@pytest.fixture\ndef db_connection() -> dict[str, str]:\n    ...\n\n\n@pytest.fixture\ndef http_session() -> requests.Session:\n    ...\n\n\n@pytest.fixture\ndef current_user() -> Mapping[str, str | int | bool]:\n    ...\n\n\n@fixture_class(name="create_user")\nclass CreateUser:\n    db_connection: Mapping[str, str]\n    http_session: requests.Session\n    current_user: Mapping[str, str | int | bool]\n\n    def __call__(self, name: str, age: int, height: int) -> dict[str, str | int | bool]:\n        user = {...}\n        self.db_connection.execute(...)\n        if self.current_user[...] is not None:\n            self.http_session.post(...)\n        \n        return user\n\n\ndef test_my_code(create_user: CreateUser):\n    johny = create_user("Johny", 27, 183)\n    michael = create_user("Michael", 43, 165)\n    loretta = create_user("Loretta", 31, 172)\n\n    # Some testing code below\n    ...\n```\n\n## Implementation details\n\n* The fixture_class decorator turns your class into a frozen dataclass with slots so you won\'t be able to add new attributes to it after definiton. You can, however, define any methods you like except `__init__`.\n',
    'author': 'Stanislav Zmiev',
    'author_email': 'szmiev2000@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Ovsyanka83/pytest-fixture-classes',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
