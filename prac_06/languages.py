from prac_06.programming_language import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

languages = [ruby, python, visual_basic]
dynamic_languages = []

print("The dynamically typed languages are:")
for language in languages:
    if language.is_dynamic() == True:
        print(language.language)

