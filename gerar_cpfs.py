class gerador_de_cpfs():
    def __init__(self, nums_meio):
        self.nums_meio = nums_meio

    def gerar_digitos(self, nums_cpf):
        sum = 0
        sum2 = 0
        dig_cpf = nums_cpf

        # for digit 1
        for i in range(len(dig_cpf)):
            sum = sum + int(dig_cpf[i])*(10-i)

        r_dig1 = sum % 11

        if r_dig1 == 0 or r_dig1 == 1:
            dig1 = 0
        else:
            dig1 = 11 - r_dig1

        dig_cpf = dig_cpf + str(dig1)

        # for digit 2
        for i in range(1,len(dig_cpf)):
            sum2 = sum2 + int(dig_cpf[i])*(11-i)
        
        r_dig2 = sum2 % 11

        if r_dig2 == 0 or r_dig2 == 1:
            dig2 = 0
        else:
            dig2 = 11 - r_dig2

        dig_cpf = dig_cpf + str(dig2)

        return dig_cpf

    def gerar_cpfs(self):
        num_meio = self.nums_meio
        cpfs = []
        for i in range(1000):
            cpf = str(i).zfill(3) + str(num_meio)
            cpf = self.gerar_digitos(cpf)
            cpfs.append(cpf)

        return cpfs