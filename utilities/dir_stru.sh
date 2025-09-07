#!/bin/bash

# Root folder
ROOT="practical-python"

# Create root and top-level files
mkdir -p $ROOT
touch $ROOT/README.md
touch $ROOT/progress.md
touch $ROOT/.gitignore

# 01 - Talk to the Machine
mkdir -p $ROOT/01_talk_to_the_machine/say_hello
touch $ROOT/01_talk_to_the_machine/say_hello/hello.py
touch $ROOT/01_talk_to_the_machine/say_hello/quiz_hello.py
touch $ROOT/01_talk_to_the_machine/say_hello/README.md

mkdir -p $ROOT/01_talk_to_the_machine/project_favorite_quote
touch $ROOT/01_talk_to_the_machine/project_favorite_quote/favorite_quote.py
touch $ROOT/01_talk_to_the_machine/project_favorite_quote/README.md

touch $ROOT/01_talk_to_the_machine/README.md

# 02 - Make It Do Math
mkdir -p $ROOT/02_make_it_do_math
touch $ROOT/02_make_it_do_math/math_basics.py
touch $ROOT/02_make_it_do_math/quiz_math.py
touch $ROOT/02_make_it_do_math/project_age_in_days.py
touch $ROOT/02_make_it_do_math/README.md

# 03 - Teach Your Code to Remember
mkdir -p $ROOT/03_teach_your_code_to_remember
touch $ROOT/03_teach_your_code_to_remember/variables_basics.py
touch $ROOT/03_teach_your_code_to_remember/quiz_variables.py
touch $ROOT/03_teach_your_code_to_remember/project_about_you.py
touch $ROOT/03_teach_your_code_to_remember/README.md

# 04 - Mix Words and Numbers
mkdir -p $ROOT/04_mix_words_and_numbers
touch $ROOT/04_mix_words_and_numbers/strings_numbers.py
touch $ROOT/04_mix_words_and_numbers/quiz_strings_numbers.py
touch $ROOT/04_mix_words_and_numbers/project_character_intro.py
touch $ROOT/04_mix_words_and_numbers/README.md

# 05 - Make the Machine Ask
mkdir -p $ROOT/05_make_the_machine_ask
touch $ROOT/05_make_the_machine_ask/input_basics.py
touch $ROOT/05_make_the_machine_ask/quiz_input.py
touch $ROOT/05_make_the_machine_ask/project_birthday_calc.py
touch $ROOT/05_make_the_machine_ask/README.md

# Resources
mkdir -p $ROOT/resources
touch $ROOT/resources/cheatsheet.md
touch $ROOT/resources/extra_exercises.md
touch $ROOT/resources/roadmap.md

echo "✅ Repository structure created inside: $ROOT"