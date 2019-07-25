import urwid


MIN_PASSWORD_LENGTH = 12


def has_digit(chars):
    return any(char.isdigit() for char in chars)


def is_very_long(chars):
    return any(len(chars) > MIN_PASSWORD_LENGTH for char in chars)


def has_letters(chars):
    return any(char.isalpha() for char in chars)


def has_upper_letters(chars):
    return any(char.isupper() for char in chars)


def has_lower_letters(chars):
    return any(char.islower() for char in chars)


def has_symbols(chars):
    return any((not char.isdigit() and not char.isalpha()) for char in chars)


def has_not_only_symbols(chars):
    if len(chars) == 0:
        return False

    alphanum_counter = 0
    spec_symbol_counter = 0

    for char in chars:
        if not char.isdigit() and not char.isalpha():
            spec_symbol_counter += 1
        else:
            alphanum_counter += 1

    if (alphanum_counter == 0) and (spec_symbol_counter > 0):
        return False
    elif alphanum_counter > 0:
        return True


def main():
    
    def on_ask_change(edit, new_edit_text):
        check_passed_counter = 0

        for check in password_checks:
            if check(new_edit_text):
                check_passed_counter += 1

        score = check_passed_counter * 2
        reply.set_text("Сложность пароля: %s" % str(score))


    ask = urwid.Edit('Введите пароль: ', mask='*')
    reply = urwid.Text("")
    menu = urwid.Pile([ask, reply])
    menu = urwid.Filler(menu, valign='top')
    urwid.connect_signal(ask, 'change', on_ask_change)
    urwid.MainLoop(menu).run()


password_checks = [
    has_digit,
    is_very_long,
    has_letters,
    has_lower_letters,
    has_upper_letters,
    has_symbols,
    has_not_only_symbols
]

if __name__ == '__main__':
    main()