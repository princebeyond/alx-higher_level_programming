def remove_char_at(input_str, n):
    if 0 <= n < len(input_str):
        result_str = input_str[:n] + input_str[n+1:]
        return result_str
    else:
        return input_str
