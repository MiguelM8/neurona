from django.shortcuts import render

class Neurona:
    def __init__(self):
        self.w0 = 1.5
        self.w1 = 0.5 
        self.w2 = 1.5
        self.sp = 0 
        self.er = 0
        self.neti = 0
        self.entrenado = False
        self.mat = [
            [0, 0, 0],
            [0, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ]

    def evaluar(self, x1, x2):
        escalon = (x1 * self.w1+ x2 * self.w2+ self.w0) >= 0
        return 1 if escalon else 0

    def entrenar(self):
        while not self.entrenado:
            self.entrenado = True
            for i in range(4):
                self.neti = self.mat[i][0] * self.w1 + self.mat[i][1] * self.w2 + self.w0
                if self.neti >= 0:
                    self.sp = 1
                else:
                    self.sp = 0
                self.er = self.mat[i][2] - self.sp
                if self.er != 0:
                    self.entrenado = False
                    self.w0 = self.w0 + self.er * 1
                    self.w1 = self.w1 + self.er * self.mat[i][0]
                    self.w2 = self.w2 + self.er * self.mat[i][1]


def index(request):
    if request.method == "POST":
        val1 = request.POST["valor1"]
        val2 = request.POST["valor2"]
        out = None
        # aqui se debe realizar la logica de prediccion de la neurona.
        if val1 and val2:
            neurona = Neurona()
            neurona.entrenar()
            out = neurona.evaluar(int(val1), int(val2))
        context = {
            "salida": out
        }
        return render(request, 'inicio.html', context)
    return render(request, 'inicio.html')