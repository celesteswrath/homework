class Team:
    def __init__(self, name, project, role):
        self.name = name
        self.project = project
        self.role = role
        print("--Developer létrehozva--")
    def __str__(self):
        return str(self.name) + " a " + str(self.project) + "-nél dolgozik " + str(self.role) + " szerepkörben"
    def __eq__(self, other):
        if self.name == other.name and self.project == other.project and self.role == other.role:
            print("Két azonos objectet nem hozhatunk létre")
            return False
        else:
            return self.project == other.project

if __name__ == "__main__":
    teamOne = Team("Ricsi","SolArch","Frontend")
    print(teamOne)
    teamTwo = Team("Angéla","ZerTeng","Tesztelő")
    print(teamTwo)
    teamThree = Team("Peti","KefERP","Backend")
    print(teamThree)
    teamFour = Team("Éva","KefERP","Backend")
    print(teamFour)
    l = [teamOne, teamTwo, teamThree, teamFour]
    for i in range(0, (len(l)-1)):
        for j in range(i+1, len(l)):
            if l[i] == l[j]:
                print(str(l[i].name) + " és " + str(l[j].name) + " dolgoznak egy szerepkörben")
