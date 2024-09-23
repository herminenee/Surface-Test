# %%
import numpy as np
#\gamma_{S V}=\gamma_{S V}^d+\gamma_{S V}^p
#\gamma_{L V}=\gamma_{L V}^d+\gamma_{L V}^p
#\gamma_{S V}^d=\gamma_{L V}^d_hexdacane\left(\frac{1+\cos \theta_Y^d_hexdacane}{2}\right)^2
#\gamma_{S V}^p=\frac{1}{\gamma_{L V}^p_water}\left[\frac{\gamma_{L V}_water\left(1+\cos \theta_Y^p_water\right)}{2}-\sqrt{\gamma_{S V}^d \gamma_{L V}^d_water}\right]^2
#\theta_{\mathrm{Y}} \approx \theta_{\mathrm{adv}}
#write a function to calculate the value of gamma_sv from theta_adv_hexadacane, theta_adv_water, where gamma_lv_hexadacane,gamma_lv_hexadacane_d, gamma_lv_water,gamma_lv_water_d,gamma_lv_water_p are constants


def compute_gamma_sv(theta_adv_hexadacane, theta_adv_water, gamma_lv_hexadacane=gamma_lv_hexadacane, gamma_lv_hexadacane_d=gamma_lv_hexadacane_d, gamma_lv_water=gamma_lv_water, gamma_lv_water_d=gamma_lv_water_d, gamma_lv_water_p=gamma_lv_water_p):
    #convert theta to radians
    theta_adv_hexadacane = np.deg2rad(theta_adv_hexadacane)
    theta_adv_water = np.deg2rad(theta_adv_water)
    gamma_sv_d = gamma_lv_hexadacane_d*((1+np.cos(theta_adv_hexadacane))/2)**2
    gamma_sv_p = (1/gamma_lv_water_p)*((gamma_lv_water*(1+np.cos(theta_adv_water))/2-np.sqrt(gamma_sv_d*gamma_lv_water_d))**2)
    gamma_sv = gamma_sv_d + gamma_sv_p
    return gamma_sv, gamma_sv_d, gamma_sv_p

# %%
gamma_lv_hexadacane = 27.5 #mN/m
gamma_lv_hexadacane_d= 27.5 #mN/m
gamma_lv_water= 72 #mN/m
gamma_lv_water_d= 21 #mN/m
gamma_lv_water_p= 51 #mN/m
theta_adv_hexadacane = 19.9
theta_adv_water = 100.4
print(compute_gamma_sv(theta_adv_hexadacane, theta_adv_water))

# %%
