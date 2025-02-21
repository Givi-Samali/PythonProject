import sys
from argparse import ArgumentParser, Namespace
from typing import List, Dict, Any


# Модели данных
class Section:
    def __init__(self, id: int, number: str):
        self.id = id
        self.number = number


class Schedule:
    def __init__(self, day: str, number_id: str, classes: List[str]):
        self.day = day
        self.number_id = number_id
        self.classes = classes


class Cadet:
    def __init__(self, id: int, first_name: str, middle_name: str,
                 last_name: str, rank: str, section_id: int):
        self.id = id
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.rank = rank
        self.section_id = section_id


# Хранилища данных
sections: List[Section] = []
schedules: List[Schedule] = []
cadets: List[Cadet] = []

# Глобальная справка
GLOBAL_HELP = """Commands:
- help
- section
- schedule
- cadet"""


# Обработчики команд
def handle_global_help(args: Namespace):
    print(GLOBAL_HELP)


def handle_module_help(module: str):
    helps = {
        'section': "Section module commands:\n- help\n- list\n- add",
        'schedule': "Schedule module commands:\n- help\n- list\n- add",
        'cadet': "Cadet module commands:\n- help\n- list\n- add"
    }
    print(helps.get(module, "Unknown module"))


def handle_command_help(module: str, command: str):
    helps = {
        ('section', 'list'): "Section list command has no parameters",
        ('section', 'add'): "Section add command parameters:\n-n: section id",
        ('schedule', 'list'): "Schedule list command parameters:\n-d: day\n-n: number section",
        ('schedule', 'add'): "Schedule add command parameters:\n-d: day\n-n: number section\n-l: list of classes",
        ('cadet', 'list'): "Cadet list command parameters:\n-i: Id\n-l: last name\n-s: section Id\n-r: rank",
        ('cadet',
         'add'): "Cadet add command parameters:\n-f: first name\n-m: middle name\n-l: last name\n-r: rank\n-s: section Id"
    }
    print(helps.get((module, command), "Unknown command"))


# Обработчики модулей
def handle_section(args: Namespace):
    if args.command == 'help':
        handle_module_help('section')
    elif args.command == 'list':
        print_sections()
    elif args.command == 'add':
        sections.append(Section(len(sections) + 1, args.n))
        print("Ok")


def handle_schedule(args: Namespace):
    if args.command == 'help':
        handle_module_help('schedule')
    elif args.command == 'list':
        filtered = [s for s in schedules
                    if (not args.d or s.day == args.d) and
                    (not args.n or s.number_id == args.n)]
        print_schedules(filtered)
    elif args.command == 'add':
        schedules.append(Schedule(args.d, args.n, args.l.split(',')))
        print("Ok")


def handle_cadet(args: Namespace):
    if args.command == 'help':
        handle_module_help('cadet')
    elif args.command == 'list':
        filtered = [c for c in cadets
                    if (not args.i or c.id == int(args.i)) and
                    (not args.l or c.last_name == args.l) and
                    (not args.s or c.section_id == int(args.s)) and
                    (not args.r or c.rank == args.r)]
        print_cadets(filtered, args.s)
    elif args.command == 'add':
        cadets.append(Cadet(len(cadets) + 1, args.f, args.m, args.l, args.r, int(args.s)))
        print("Ok")


# Вспомогательные функции
def print_sections():
    for s in sorted(sections, key=lambda x: x.id):
        print(f"{{Section:{{ Id:{s.id}, Number: {s.number} }}")


def print_schedules(s_list: List[Schedule]):
    for s in s_list:
        print(f"{{Schedule:{{Day: {s.day}, NumberId: {s.number_id}, ListClass: {s.classes} }}")


def print_cadets(c_list: List[Cadet], sort_key: str = 'id'):
    reverse = sort_key.startswith('-')
    key = sort_key.lstrip('-')
    sorted_cadets = sorted(c_list,
                           key=lambda x: x.id if key == 'id' else x.last_name,
                           reverse=reverse)
    for c in sorted_cadets:
        print(f"{{Cadet:{{Id:{c.id}, Rank:{c.rank}, FirstName: {c.first_name}, "
              f"MiddleName: {c.middle_name}, LastName: {c.last_name}, SectionId: {c.section_id} }}")


# Парсинг аргументов
def main():
    parser = ArgumentParser(prog='program', add_help=False)
    parser.add_argument('module', nargs='?', default='help')
    parser.add_argument('command', nargs='?', default='help')
    parser.add_argument('args', nargs='*')

    args, unknown = parser.parse_known_args()

    # Глобальная команда help
    if args.module == 'help' or (not args.module and not args.command):
        handle_global_help(args)
        return

    # Обработка модулей
    if args.module == 'section':
        section_parser = ArgumentParser(prog='program section')
        section_parser.add_argument('command')
        section_parser.add_argument('-n', required=False)
        section_args = section_parser.parse_args([args.command] + unknown)
        handle_section(section_args)

    elif args.module == 'schedule':
        schedule_parser = ArgumentParser(prog='program schedule')
        schedule_parser.add_argument('command')
        schedule_parser.add_argument('-d', required=False)
        schedule_parser.add_argument('-n', required=False)
        schedule_parser.add_argument('-l', required=False)
        schedule_args = schedule_parser.parse_args([args.command] + unknown)
        handle_schedule(schedule_args)

    elif args.module == 'cadet':
        cadet_parser = ArgumentParser(prog='program cadet')
        cadet_parser.add_argument('command')
        cadet_parser.add_argument('-f', required=False)
        cadet_parser.add_argument('-m', required=False)
        cadet_parser.add_argument('-l', required=False)
        cadet_parser.add_argument('-r', required=False)
        cadet_parser.add_argument('-s', required=False)
        cadet_args = cadet_parser.parse_args([args.command] + unknown)
        handle_cadet(cadet_args)

    else:
        print("Invalid command")


if __name__ == "__main__":
    main()