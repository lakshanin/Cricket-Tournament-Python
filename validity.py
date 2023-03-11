def valid(prompt, v_inputs):
    v = False
    while not v:
        try:
            user_input = int(input(prompt))
            if v_inputs == 2:
                if user_input != 1 and user_input != 2:
                    raise ValueError
                else:
                    v = True
                    return user_input
            elif v_inputs == 3:
                if user_input != 1 and user_input != 2 and user_input != 3:
                    raise ValueError
                else:
                    v = True
                    return user_input
            elif v_inputs == 11:
                if user_input < 0 or user_input > 10:
                    raise ValueError
                else:
                    v = True
                    return user_input
        except ValueError:
            print('Enter a valid Input!')
