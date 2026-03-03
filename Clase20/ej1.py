class CuentaBancaria:
    def __init__(self, titular, saldo_inicial = 0):
        self._titular = titular #Atributo privado 
        self._saldo = saldo_inicial # Artributo privado
        self._historial = [] # lista para almacenar el historial de transacciones 
        
        self._historial.append(f'Cuenta creada con saldo inicial de {saldo_inicial}')
        
    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo
    
    @property
    def historial(self):
        return self._historial.copy()
    

    def depositar(self, cantidad):
        if cantidad <= 0 :
            raise ValueError("La cantidad a depostirar debe mayor que cero.")
        self.saldo += cantidad
        self
        

    

                