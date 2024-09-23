# %%
import numpy as np

# \sin \omega \approx \frac{\gamma_{l v} D_{T C L}\left(\cos \theta_{r e c}-\cos \theta_{a d v}\right)}{\rho g V}
#D_{T C L}=2 \sin \bar{\theta}\left[\frac{3 V}{\pi\left(2-3 \cos \bar{\theta}+\cos ^3 \bar{\theta}\right)}\right]^{\frac{1}{3}}
#\cos \bar{\theta}=\frac{\left(\cos \theta_{a d v}+\cos \theta_{r e c}\right)}{2}
#write a function to calculate the value of omega from theta_adv, theta_rec, where gamma_lv, rho, g, V are constants
gamma_lv_water = 72e-3 #N/m
rho_water = 1000 #kg/m^3
g = 10 #m/s^2
V = 20e-9 #m^3

def compute_omega(theta_adv, theta_rec, gamma_lv=gamma_lv_water, rho=rho_water, g=g, V=V):
    #convert theta to radians
    theta_adv = np.deg2rad(theta_adv)
    theta_rec = np.deg2rad(theta_rec)
    cos_bar_theta = (np.cos(theta_adv) + np.cos(theta_rec))/2
    D_TCL = 2*np.sin(np.arccos(cos_bar_theta))*((3*V)/(np.pi*(2-3*cos_bar_theta+cos_bar_theta**3)))**(1/3)
    sin_omega = (gamma_lv*D_TCL*(np.cos(theta_rec)-np.cos(theta_adv)))/(rho*g*V)
    omega = np.arcsin(sin_omega)
    return np.rad2deg(omega)

theta_adv = 100.4
theta_rec = 93.5
# for example on oil(but usually we use water)
#gamma_lv_oil = 0.025 #N/m
#rho_oil = 900 #kg/m^3
omega = compute_omega(theta_adv, theta_rec, gamma_lv=gamma_lv_water, rho=rho_water, g=g, V=V)
print(omega)
# %%
#use the function to calculate the sliding angle for each row in the data
# we can compare experiment data with the calculated sliding angle
import pandas as pd
import matplotlib.pyplot as plt

# load the data from data.csv
data = pd.read_csv('data.csv')

# compute the sliding angle for each row in the data
data['omega'] = compute_omega(data['theta_adv'], data['theta_rec'])
print(data)
# %%
# plot omega vs. theta_adv
plt.scatter(data['theta_adv'], data['omega'])
plt.xlabel('theta_adv')
plt.ylabel('omega')
# %%
#compare experiment data with the calculated sliding angle
plt.plot(data['theta_sliding'], data['omega'])
plt.xlabel('theta_sliding')
plt.ylabel('omega')
# %%