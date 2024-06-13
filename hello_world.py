secret_word = 'coucou'
health_point = 7
public_word = '_'*len(secret_word)

while health_point > 0 and public_word != secret_word : 
    letter = input('rentrez une lettre : ')
    if letter in secret_word :
        for i in range (len(secret_word)):
            if letter == secret_word[i]:
                public_word = public_word[:i] + letter + public_word[i + 1:]
    else :
        health_point -= 1
    if public_word == secret_word :
        print('bravo le mot mystère etait',public_word)
    elif health_point == 0 : 
        print('looser fallait deviner', secret_word, 'mais la tu es mort')
    else:
        print('vous avez',health_point, 'vie(s) restante(s)')
        print('le mot est :', public_word)


