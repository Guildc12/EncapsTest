class Login:
    def __init__(self):


        while True:
            self.tratamento = self.Tratamento()
            if input('Debug ->') == '1':

                self.reg(self.tratamento)
                continue
            if input('Debug ->') == '2':
                self.__login = input('digite seu nome de usuário ')
                if self.__login:
                    print('logado com sucesso!')
                    break
                else:
                    print('usuario ou senha inválidos, tente novamente!')
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
            if controle:
                regl.write(f'!{nm}\n'
                           f'#{sn}\n\n')
                break
            else:
                print("Algo deu errado!")
                continue
    @property
    def __login(self):
        return self.touf

    @__login.setter
    def __login(self, variavel):
        senha = input('Digite sua senha: ')
        self.touf = False
        for valor in self.tratamento:
            if valor[0] == variavel and valor[1] == senha:
                self.touf = True
                break
Login()