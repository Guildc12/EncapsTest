class Login:
    def __init__(self):
        tratamento = self.Tratamento()
        while True:
            if input('Debug ->') == '1':
                self.reg(tratamento)
                continue
            if input('Debug ->') == '2':
                self.bixo(tratamento)
                continue

    def getter(self, info):
        pass
    def setter(self, info):
        pass

    def Tratamento(self):
        txt = open("logs.txt", "r")
        tratar = txt.read()
        txt.close()
        abc = tratar.split("\n")
        final = list()
        add = list()
        for a in abc:
            if "!" in a:
                add.append(a[1:])
            elif "#" in a:
                add.append(a[1:])
                final.append(add)
                add = list()
        return final

    def reg(self, trat):
        regl = open("logs.txt", "a")
        controle = True
        while True:
            nm = input("Nome -->")
            sn = input("Senha -->")

            for elementos in trat:
                if elementos[0] == nm:
                    controle = False
                elif elementos[1] == sn:
                    controle = False
            if controle:
                regl.write(f'!{nm}\n'
                           f'#{sn}\n\n')
                break
            else:
                print("Algo deu errado!")
                continue

    def bixo(self, trat):
        inp = input("Qual nome? --> ")
        for elementos in trat:
            if elementos[0] == inp:
                inpp = input("Qual senha? -->")
                if elementos[1] == inpp:
                    print("Você está dentro")
                    break

Login()