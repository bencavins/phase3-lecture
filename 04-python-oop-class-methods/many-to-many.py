class Bar:
    def __init__(self, name) -> None:
        self.name = name
        self.cocktails = []
    
    def get_all_proofs(self):
        for drink in self.cocktails:
            drink.get_proof()


class Cocktail:
    def __init__(self, name) -> None:
        self.name = name
        self.proof = 80
        self.bars = []

    def get_proof(self):
        print(f'{self.name} is {self.proof} proof')
    

if __name__ == '__main__':
    bar1 = Bar('White Horse')
    bar2 = Bar('Barcelona Bar')

    c1 = Cocktail('Gin & Tonic')
    c2 = Cocktail('Whiskey Sour')
    c3 = Cocktail('Espresso Martini')

    # link the cocktails to the bars
    bar1.cocktails = [c1, c2, c3]
    bar2.cocktails = [c1, c2]

    # link the bars to the cocktails
    c1.bars = [bar1, bar2]
    c2.bars = [bar1, bar2]
    c3.bars = [bar1]

    # get all cocktails per bar
    print('Drinks for ' + bar1.name)
    for drink in bar1.cocktails:
        drink.get_proof()
    
    print('-'*10)
    # get all bars that serve this cocktail
    print('Bars serving ' + c1.name)
    for bar in c1.bars:
        print(bar.name)
