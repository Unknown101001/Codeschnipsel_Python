""" 
Example of a Lorentz System IVP 3D Plot

Try other initial values for seeing the beautiful chaotic behavior. 
As we have only console output in CodePlayground, try it on a real machine to see the plot.
"""
import numpy as np
import abc 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def expl_euler(t, u0, f): 
    tau = t[1] - t[0] 
    if isinstance(u0, (int, float)): 
        u = np.zeros(shape=(len(t)))          
    else: 
        u = np.zeros(shape=(len(t), len(u0)))    
    u[0] = u0 
    for n in range(1, len(t)): 
        u[n] = u[n - 1] + tau * f(t[n - 1], u[n - 1]) 
    return u 

class IVP:
    """ 
    Initial value problems of the shape: 
    u'(t) = f(t, u) u(0) = u0 
    """ 
    def __init__(self, name, t, u0): 
        self.name = name 
        self.t = t 
        self.tau = t[1] - t[0] 
        self.Nt = len(t) - 1 
        self.u0 = u0 
        
        @abc.abstractmethod 
        def f(self, *args): 
            """ Right hand side ODE """
     
        def u(self, *args): 
            """ Returns exact solution function """ 
        
        def plot_solution(self, t, u, label, ax): 
            ax.plot(t, u, label=label) 
            ax.set_title(r'Solution of {}, $N = {}$'.format(self.name, len(self.t) - 1))  
            
            


class LorenzSystem(IVP):
    def __init__(self, t, u0=np.array([1.0, 0.0, 0.0]), **kwargs): 
        super().__init__('Lorenz System', t, u0)     
        self.exact_sol = False 
        self.sigma = kwargs.get('alpha', 10.0)
        self.rho = kwargs.get('rho', 28.0)
        self.beta = kwargs.get('beta', 2.667) # 8 / 3 
    def f(self, t, u): 
        u0 = self.sigma * (u[1] - u[0]) 
        u1 = self.rho * u[0] - u[1] - u[0] * u[2]
        u2 = u[0] * u[1] - self.beta * u[2]
        return np.array([u0, u1, u2]) 


if __name__ == "__main__":
    plt.style.use('dark_background')
    fig = plt.figure(figsize=(20,20),dpi=100) 
    ax = fig.add_subplot(111, projection='3d') 
    Tmin, Tmax = 0,30 
    # Discretization and solver
    N = 16000 
    t = np.linspace(Tmin, Tmax, N + 1)      
    ivp = LorenzSystem(t) 
    sol = expl_euler(t, ivp.u0, ivp.f) 
    ax.plot(sol[:, 0], sol[:, 1], sol[:, 2],color = "brown",linewidth=0.7) 

    u1 = np.array([0.95, 0.05, 0.0])      
    ivp2 = LorenzSystem(t,u1) 
    sol = expl_euler(t, ivp2.u0, ivp2.f) 
    ax.plot(sol[:, 0], sol[:, 1], sol[:, 2],color = "darkgoldenrod",linewidth=0.7) 

    u2 = np.array([1.05, 0.00, 0.05])      
    ivp3 = LorenzSystem(t,u2) 
    sol = expl_euler(t, ivp3.u0, ivp3.f) 
    ax.plot(sol[:, 0], sol[:, 1], sol[:, 2],color = "goldenrod",linewidth=0.7) 

    u3 = np.array([1.05, -0.05, 0.05])      
    ivp4 = LorenzSystem(t,u3) 
    sol = expl_euler(t, ivp4.u0, ivp4.f) 
    ax.plot(sol[:, 0], sol[:, 1], sol[:, 2],color = "chocolate",linewidth=0.7) 
    # Hide grid lines
    ax.grid(False)
    ax.w_xaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
    ax.w_yaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
    ax.w_zaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
    ax.w_xaxis.set_visible(False)
    ax.get_yaxis().set_visible(False)
    # Hide axes ticks
    #ax.set_xticks([])
    #ax.set_yticks([])
    #ax.set_zticks([]) 
    plt.show()
