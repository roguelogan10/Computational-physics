import numpy as np 
import matplotlib.pyplot as plt

def central_difference(f,point = 0, h=1e-5):
    """
    Calculate the derivative of a function at a given point using central difference method.
    """
    return (f(point + h)-f(point-h))/(2*h)

def derivative_function(list_h, f,point):
     derivative_list = []
     for elmt in list_h:
       derivative_list.append(central_difference(f, point, elmt))
     return derivative_list
      
def derivative_error_function(list_h, f,point, exact_derivative):
    return (derivative_function(list_h, f,point)- exact_derivative(point))/ exact_derivative(point)

def plot_derivative_relative_error(list_h,f,point, exact_derivative):
    list_derivative = derivative_function(list_h, f, point) 
    list_error = derivative_error_function(list_h, f,point, exact_derivative)
    log10_list_error= np.log10(np.abs(list_error))
    log10_list_h = np.log10(list_h)
    fig, ax = plt.subplots(3,1, figsize=(10, 8))
    ax[0].plot(list_h, list_derivative, label='Numerical Derivative') 
    ax[1].plot(list_h, list_error, label="Derivative's relative error") 
    ax[2].plot(log10_list_h, log10_list_error, label="log10(Derivative's relative error)")
    ax[0].set_title('Numerical Derivative vs h') 
    ax[1].set_title('Relative Error vs h')
    ax[1].set_title('log10(Relative Error) vs log10(h)')
    ax[0].set_xlabel('h')
    ax[1].set_xlabel('h') 
    ax[2].set_xlabel('log10(h)') 
    ax[0].set_ylabel('Numerical Derivative')        
    ax[1].set_ylabel('Relative Error')
    ax[2].set_ylabel('log10(Relative Error)')
    ax[0].legend()
    ax[1].legend()
    ax[2].legend()
    plt.tight_layout()    
    plt.show()


def cosine_derivative(point):
    return -1 * np.sin(point)  

if __name__ == "__main__":
    h_list = np.arange(1e-5, 1e-2, 1e-5)
    approxim_derivative = central_difference(np.cos,point = 0.1, h=0.01)
    exact_derivative = -1*np.sin(0.1)
    print(f'exact derivative for h = {0.01} is {np.round(approxim_derivative, 3)}')
    print(f'relative error for h = {0.01} is {np.round((approxim_derivative-exact_derivative)/exact_derivative,6)}')

    plot_derivative_relative_error(h_list, np.cos, 0.1, cosine_derivative)

