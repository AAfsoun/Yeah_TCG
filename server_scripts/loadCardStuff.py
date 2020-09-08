CARDPATH = './cards/cards.txt'
import json

def loadCards():
    with open(CARDPATH) as f:
        return json.loads(f.read())

def saveCards(cards):
    with open(CARDPATH, 'w') as f:
        f.write(json.dumps(cards, indent=4))

def loadDecks():
    # TODO: check deck to make sure it works.
    decks = {'k':{ 'deck': ['Dragon King Hades',
                            'Dragon King Hades', 
                            'Dragon King Hades', 
                            'Lucifer the Demon King',
                            'Miyamoto Musashi',
                            'Miyamoto Musashi',
                            'Miyamoto Musashi',
                            'ROID RAGE',
                            'ROID RAGE',
                            'ROID RAGE',
                            'Call of Hades',
                            'Call of Hades',
                            'Call of Hades',
                            'Tyranny',
                            'Breath User Jaycob',
                            'Breath User Jaycob',
                            'Breath User Jaycob',
                            'Recruitment',
                            'Soul Bond',
                            'Skinny Jaycob',
                            'Skinny Jaycob',
                            'Skinny Jaycob',], 
                      'goals': ['The March of the Fairyfly',
                                'Power of a Homeowner',
                                'Pretty Good Attack']},
             'j':{ 'deck': ['Tyranny',
                            'Tyranny',
                            'Tyranny',
                            'Sharpen Swords',
                            'Sharpen Swords',
                            'Sharpen Swords',
                            'Breath User Jaycob',
                            'Breath User Jaycob',
                            'Breath User Jaycob',
                            'Skinny Jaycob',
                            'Skinny Jaycob',
                            'Skinny Jaycob',
                            'Ajax the Spearman',
                            'Ajax the Spearman',
                            'Ajax the Spearman',
                            'Chad Squire',
                            'Chad Squire',
                            'Chad Squire',
                            'Mr. Deffrey Javis',
                            'Mr. Deffrey Javis',
                            'Mr. Deffrey Javis',
                            'Call of Hades',
                            'Call of Hades',
                            'Call of Hades',
                            'Lucifer the Demon King'], 
                      'goals': ['The March of the Fairyfly',
                                'Power of a Homeowner',
                                'Pretty Good Attack']},
             
             'hello':{'deck': ['Call of Hades',
                               "Hero's Chant",
                               'Ouija Board',
                               'Skinny Jaycob',
                               'Skinny Jaycob',
                               'Skinny Jaycob',
                               'Messenger of Hades',
                               "Lucifer's Servant",
                               'Flesh Blade',
                               'Jack the Ripper',
                               'Jack the Ripper',
                               'Baby Demon',
                               'Sweaty Homunculus',
                               'Lucifer the Demon King',
                               'Dragon King Hades',
                               'Breath User Jaycob',
                               'Breath User Jaycob',
                               'Breath User Jaycob',
                               'Golden Claws',
                               'Golden Claws',
                               'Golden Claws',
                               'Jack the Ripper',
                               'Jack the Ripper',
                               'Jack the Ripper',],
                      'goals': ['The March of the Fairyfly',
                                'Power of a Homeowner',
                                'Pretty Good Attack']},
             'virginia':{'deck': ['Sharpen Swords',
                                  'Sharpen Swords',
                                  'Sharpen Swords',
                                  'Chad Squire',
                                  'Chad Squire',
                                  'Chad Squire',
                                  'Recruitment',
                                  'Recruitment',
                                  'Recruitment',
                                  'Julius Caesar',
                                  'Julius Caesar',
                                  'Julius Caesar',
                                  'Baseball Lad',
                                  'Baseball Lad',
                                  'Baseball Lad',
                                  'Mr. Deffrey Javis',
                                  'Mr. Deffrey Javis',
                                  'Mr. Deffrey Javis',
                                  'Ajax the Spearman',
                                  'Ajax the Spearman',
                                  'Ajax the Spearman',
                                  'Jason the Hero',
                                  'Jason the Hero',
                                  'Jason the Hero',
                                  'Breath User Jaycob',
                                  'Breath User Jaycob',
                                  'Breath User Jaycob',
                                  'Scout the Scout',
                                  'Scout the Scout',
                                  'Scout the Scout',
                                  'Sir Lancelot ',
                                  'Sir Lancelot ',
                                  'Sir Lancelot ',
                                  'Achilles the mythical Swordsman ',
                                  'Achilles the mythical Swordsman ',
                                  'Achilles the mythical Swordsman ',
                                  'King Arthur',
                                  'Skinny Jaycob',
                                  'Skinny Jaycob',
                                  'Skinny Jaycob',
                                  'Excalibur',
                                  'Swords Man',
                                  'Swords Man',
                                  'Swords Man'],
                         'goals': ['Dance of Metal',
                                   'Power of a Homeowner',
                                   'Pretty Good Attack']},
             'dame dame':{'deck': ['Baseball Lad', 'Baseball Lad', 'Baseball Lad', 'Breath User Jaycob', 'Breath User Jaycob', 'Breath User Jaycob', 'Excalibur', 'Excalibur', 'Excalibur', 'King Arthur', 'King Arthur', 'King Arthur', 'Skinny Jaycob', 'Skinny Jaycob', 'Skinny Jaycob', "Jaycob's inner demon", "Jaycob's inner demon", "Jaycob's inner demon", 'Sir Lancelot ', 'Achilles the mythical Swordsman ', 'Sharpen Swords', 'Sharpen Swords', 'Sharpen Swords', 'Mr. Deffrey Javis', 'Mr. Deffrey Javis', 'Mr. Deffrey Javis'],
                          'goals': ['The March of the Fairyfly', 'Pretty Good Attack', 'Dance of Metal']
                          },
             }
    return decks

def saveDeck(deck):
    return





def main():
    cards = loadCards()

    
    
    saveCards(cards)


if __name__ == '__main__':
    CARDPATH = '../cards/cards.txt'
    main()
