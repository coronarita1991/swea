def solution(phone_number):
    return ''.join('*'  if i < len(phone_number)-4 else n for i, n in enumerate(phone_number))