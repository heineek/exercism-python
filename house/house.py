def verse(num):
    verses = ['This is the horse and the hound and the horn',
              'that belonged to the farmer sowing his corn',
              'that kept the rooster that crowed in the morn',
              'that woke the priest all shaven and shorn',
              'that married the man all tattered and torn',
              'that kissed the maiden all forlorn',
              'that milked the cow with the crumpled horn',
              'that tossed the dog',
              'that worried the cat',
              'that killed the rat',
              'that ate the malt',
              'that lay in the house that Jack built.']

    if num == 0:
        return 'This is the house that Jack built.'
    else:
        verse_list = verses[-num - 1:]
        first_verse = verse_list[0].split()
        first_verse[0] = 'This'
        first_verse[1] = 'is'
        if num == 10:
            first_verse.remove('to')            # to the farmer
        verse_list[0] = ' '.join(first_verse)
        return '\n'.join(verse_list)


def rhyme():
    verses = [verse(i) for i in range(12)]
    return '\n\n'.join(verses)