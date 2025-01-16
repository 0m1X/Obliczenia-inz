from sympy import symbols, sympify

from trapezoidal_integration import trapezoidal
from simpson_integration import simpson
from monte_carlo_integration import monte_carlo

def main():
    
    f = input('Wpisz wzór funkcji f(x): ')
    method = input('Wybierz metodę całkowania: trapezoidal, Simpson, Monte Carlo: ')

    try:
        dx = float(input('Określ krok całkowania dla metod trapezoidal i Simpson lub ilość prób dla metody Monte Carlo: '))
        x0 = float(input('Podaj warunek początkowy x0: '))
        xk = float(input('Podaj warunek końcowy xk: '))
    except ValueError:
        print("Błąd: Podano nieprawidłową wartość dla dx, x0 lub xk.")
        return
    
    x = symbols('x')
    expr = sympify(f)

    def temp_f(q):
        return expr.subs(x, q)
    
    if x0 > xk:
        print('Niewłaściwe warunki początkowe, x0 musi być mniejsze od xk. ')
    #if dx > xk - x0:
    #    print('Zbyt duży krok całkowania')

    if method == 'trapezoidal':
        area = trapezoidal(x0, xk, dx, temp_f)
    elif method == 'Simpson':
        area = simpson(x0, xk, dx, temp_f)
    elif method == 'Monte Carlo':
        area = monte_carlo(x0, xk, dx, temp_f)
    else:
        ('Błąd, wybierz opcję z listy')
        return

    print('Wynik całkowania: ' + str(area))

if __name__ == '__main__':
    main()