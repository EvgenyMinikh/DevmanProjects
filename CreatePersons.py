from faker import Faker
import file_operations as fo
import random

NUMBER_OF_ANKETAS = 10
TEMPLATE_SOURCE_PATH = "charsheet.svg"
READY_FILE_PATH_TEMPLATE = "Anketas/result{}.svg"

skills = [
    "Стремительный прыжок",
    "Электрический выстрел",
    "Ледяной удар",
    "Стремительный удар",
    "Кислотный взгляд",
    "Тайный побег",
    "Ледяной выстрел",
    "Огненный заряд"
]

runes_alphabet = {
    'а': 'а͠', 'б': 'б̋', 'в': 'в͒͠',
    'г': 'г͒͠', 'д': 'д̋', 'е': 'е͠',
    'ё': 'ё͒͠', 'ж': 'ж͒', 'з': 'з̋̋͠',
    'и': 'и', 'й': 'й͒͠', 'к': 'к̋̋',
    'л': 'л̋͠', 'м': 'м͒͠', 'н': 'н͒',
    'о': 'о̋', 'п': 'п̋͠', 'р': 'р̋͠',
    'с': 'с͒', 'т': 'т͒', 'у': 'у͒͠',
    'ф': 'ф̋̋͠', 'х': 'х͒͠', 'ц': 'ц̋',
    'ч': 'ч̋͠', 'ш': 'ш͒͠', 'щ': 'щ̋',
    'ъ': 'ъ̋͠', 'ы': 'ы̋͠', 'ь': 'ь̋',
    'э': 'э͒͠͠', 'ю': 'ю̋͠', 'я': 'я̋',
    'А': 'А͠', 'Б': 'Б̋', 'В': 'В͒͠',
    'Г': 'Г͒͠', 'Д': 'Д̋', 'Е': 'Е',
    'Ё': 'Ё͒͠', 'Ж': 'Ж͒', 'З': 'З̋̋͠',
    'И': 'И', 'Й': 'Й͒͠', 'К': 'К̋̋',
    'Л': 'Л̋͠', 'М': 'М͒͠', 'Н': 'Н͒',
    'О': 'О̋', 'П': 'П̋͠', 'Р': 'Р̋͠',
    'С': 'С͒', 'Т': 'Т͒', 'У': 'У͒͠',
    'Ф': 'Ф̋̋͠', 'Х': 'Х͒͠', 'Ц': 'Ц̋',
    'Ч': 'Ч̋͠', 'Ш': 'Ш͒͠', 'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠', 'Ы': 'Ы̋͠', 'Ь': 'Ь̋',
    'Э': 'Э͒͠͠', 'Ю': 'Ю̋͠', 'Я': 'Я̋',
    ' ': ' '
}


def change_letters_to_runes(phrase):
    letters = set(phrase)

    for letter in letters:
        phrase = phrase.replace(letter, runes_alphabet[letter])

    return phrase


def character_anketas_generator(character_number):
    character_skills_list = random.sample(skills, 3)
    runic_skills = [change_letters_to_runes(character_skills_list[i]) for i in range(3)]

    fake = Faker("ru_RU")
    first_name = fake.first_name()
    last_name = fake.last_name()
    job = fake.job()
    town = fake.city()
    strength = random.randint(8, 14)
    agility = random.randint(8, 14)
    endurance = random.randint(8, 14)
    intelligence = random.randint(8, 14)
    luck = random.randint(8, 14)
    skill_1 = runic_skills[0]
    skill_2 = runic_skills[1]
    skill_3 = runic_skills[2]

    context = {
        "first_name": first_name,
        "last_name": last_name,
        "job": job,
        "town": town,
        "strength": strength,
        "agility": agility,
        "endurance": endurance,
        "intelligence": intelligence,
        "luck": luck,
        "skill_1": skill_1,
        "skill_2": skill_2,
        "skill_3": skill_3
    }

    fo.render_template(TEMPLATE_SOURCE_PATH, READY_FILE_PATH_TEMPLATE.format(character_number), context)


for i in range(NUMBER_OF_ANKETAS):
    character_anketas_generator(i + 1)