"""
Create classes to track homeworks.

1. Homework - accepts howework text and deadline (datetime.timedelta)
Homework has a method, that tells if deadline has passed.

2. Student - can solve homework with `do_homework` method.
Raises DeadlineError with "You are late" message if deadline has passed

3. Teacher - can create homework with `create_homework`; check homework with `check_homework`.
Any teacher can create or check any homework (even if it was created by one of colleagues).

Homework are cached in dict-like structure named `homework_done`. Key is homework, values are
solutions. Each student can only have one homework solution.

Teacher can `reset_results` - with argument it will reset results for specific homework, without -
it clears the cache.

Homework is solved if solution has more than 5 symbols.

-------------------
Check file with tests to see how all these classes are used. You can create any additional classes
you want.
"""

"""import datetime


class DeadlineError(Exception):
    pass


class Homework:
    def __init__(self, text, deadline):
        self.text = text
        self.deadline = deadline
        self.created_at = datetime.datetime.now()

    def is_active(self):
        return datetime.datetime.now() <= self.created_at + self.deadline


class Student:
    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name
        self.homework_done = {}

    def do_homework(self, homework, solution):
        if not homework.is_active():
            raise DeadlineError("You are late")
        if len(solution) < 5:
            return None
        self.homework_done[homework] = solution
        return HomeworkResult(self, homework, solution)


class HomeworkResult:
    def __init__(self, author, homework, solution):
        self.author = author
        self.homework = homework
        self.solution = solution


class Teacher:
    homework_done = {}


    @classmethod
    def create_homework(cls, text, deadline):
        return Homework(text, datetime.timedelta(days=deadline))

    @classmethod
    def check_homework(cls, homework_result):
        if len(homework_result.solution) < 5:
            return False
        if homework_result.homework not in cls.homework_done:
            cls.homework_done[homework_result.homework] = []

        cls.homework_done[homework_result.homework].append(homework_result.solution)
        return True

    @classmethod
    def reset_results(cls, homework=None):
        if homework is None:
            cls.homework_done.clear()
        elif homework in cls.homework_done:
            del cls.homework_done[homework]
            ** update

"""

import datetime


class DeadlineError(Exception):
    pass


class SolutionError(Exception):
    pass


class Homework:
    def __init__(self, text, deadline):
        self.text = text
        self.deadline = deadline
        self.created_at = datetime.datetime.now()

    def is_active(self):
        return datetime.datetime.now() <= self.created_at + self.deadline


class HomeworkResult:
    def __init__(self, author, homework, solution):
        self.author = author
        self.homework = homework
        self.solution = solution
        self.created = datetime.datetime.now()

    def __str__(self):
        return f"{self.author} - {self.homework}"

    def __repr__(self):
        return f"HomeworkResult(author={self.author}, homework={self.homework}, solution={self.solution}, created={self.created})"

    def get_solution(self):
        return self.solution

    def get_author(self):
        return self.author

    def get_homework(self):
        return self.homework


class Student:
    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name

    def do_homework(self, homework, solution):
        if not isinstance(homework, Homework):
            raise TypeError("You gave a not Homework object")
        if not homework.is_active():
            raise DeadlineError("You are late")
        if len(solution) < 5:
            raise SolutionError("Solution is too short")
        result = HomeworkResult(self, homework, solution)
        return result


class Teacher:
    homework_done = {}

    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name

    @classmethod
    def create_homework(cls, text, deadline):
        return Homework(text, datetime.timedelta(days=deadline))



    @classmethod
    def check_homework(cls, homework_result):
        if len(homework_result.get_solution()) < 5:
            return False
        if homework_result.get_homework() not in cls.homework_done:
            cls.homework_done[homework_result.get_homework()] = []

        cls.homework_done[homework_result.get_homework()].append(homework_result)
        return True

    @classmethod
    def reset_results(cls, homework=None):
        if homework is None:
            cls.homework_done.clear()
        elif homework in cls.homework_done:
            cls.homework_done[homework] = []