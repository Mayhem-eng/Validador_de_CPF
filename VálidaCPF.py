valores = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
import re

class Valida_CPF:
    def __init__(self, cpf):
        self.cpf = cpf

    def valida(self):
        
        #-> Remove tudo que não for entre 0-9
        self.cpf = re.sub(r'[^0-9]', '', self.cpf)

        #-> Pega o CPF orginal para testa-lo no final
        cpf_aux = self.cpf

        
        resultado = 0

        #-> Fatia o CPF para validar
        self.cpf = self.cpf[:9]

        #-> Itera sobre o CPF e os valores e salva a soma da multiplicação de ambos.
        if len(self.cpf) == 9:
            for index, cpf in enumerate(self.cpf):
                resultado += int(cpf) * valores[1:][index]
        #-> AO digito pega o resultado das multiplicações tira o módulo dela por 11 e subtrai pelo mesmo.
        #   Caso seja maior que 9 o 1° dígito equivale a 0, senão ele equivale ao mesmo.
            digito = 11 - (resultado % 11)
    
            if digito > 9:
                self.cpf += "0"
            else:
                self.cpf += str(digito)
        
        resultado = 0

        #-> Com isso ele pega o primeiro digito e parte para o segundo digito 
        # reiniciando o loop e fórmula.
        
        if len(self.cpf) == 10:
            for index, cpf in enumerate(self.cpf):
                resultado += int(cpf) * valores[index]
             
       
            digito = 11 - (resultado % 11)
       
            if digito > 9:
                self.cpf += "0"
            else:
                self.cpf += str(digito)

        #-> Ele verifica se o CPF gerado a partir do loop e formula é igual ao 
        # cpf_aux que é o original e formata o CPF.
        if cpf_aux == self.cpf:
            print(f"{cpf_aux[:3]}.{cpf_aux[3:6]}.{cpf_aux[6:9]}-{cpf_aux[9:]} é VÁLIDO")
        else:
            print(f"{cpf_aux[:3]}.{cpf_aux[3:6]}.{cpf_aux[6:9]}-{cpf_aux[9:]} é INVÁLIDO")


cpf = Valida_CPF("67548523726")

cpf.valida()
        


