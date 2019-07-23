import urwid

def has_digit(chars):
  for char in chars:
    if (char.isdigit()):
      return True
  
  return False


def is_very_long(chars):
  if (len(chars) > min_password_length):
    return True
  
  return False


def has_letters(chars):
  for char in chars:
    if (char.isalpha()):
      return True
  
  return False


def has_upper_letters(chars):
    for char in chars:
      if (char.isupper()):
        return True
    
    return False


def has_lower_letters(chars):
    for char in chars:
      if (char.islower()):
        return True
    
    return False


def has_symbols(chars):
    for char in chars:
      if (not char.isdigit() and not char.isalpha()):
        return True

    return False


def has_not_only_symbols(chars):
    if (len(chars) == 0):
      return False
    
    alphanum_counter = 0
    spec_symbol_counter = 0

    for char in chars:
      if (not char.isdigit() and not char.isalpha()):
        spec_symbol_counter += 1
      else:
        alphanum_counter += 1
    
    if ((alphanum_counter == 0) and (spec_symbol_counter > 0)):
      return False
    elif (alphanum_counter > 0):
      return True


def on_ask_change(edit, new_edit_text):
  global score
  score = 0
  check_passed_counter = 0
  
  message = ''

  for check in password_checks:
    message = message + '\n' + str(check) + ' * ' + str(check(new_edit_text))
    
    if (check(new_edit_text)):
      check_passed_counter += 1

  score = check_passed_counter * 2
  reply.set_text("Сложность пароля: %s" % str(score) + message)


password_checks = [
                    has_digit,
                    is_very_long,
                    has_letters,
                    has_lower_letters,
                    has_upper_letters,
                    has_symbols,
                    has_not_only_symbols
                  ]

score = 14
min_password_length = 12

ask = urwid.Edit('Введите пароль: ', mask='*')
reply = urwid.Text("")
menu = urwid.Pile([ask, reply])
menu = urwid.Filler(menu, valign='top')
urwid.connect_signal(ask, 'change', on_ask_change)
urwid.MainLoop(menu).run()