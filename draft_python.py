angle_min = -1.919
angle_max = 1.919
angle_increment = 0.01559

values = [ [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ] for i in range(25)]

self.mesure = 0.0 # valeur fournie par le capteur
self.total_sum = 0.0
self.Tab_length = 247
self.Tab_of_value = [0.0 for i in range(247)] 

def get_indice(self, angle_deg):
        angle_rad = angle_deg*(3.14/180)
        return int(angle_rad_- angle_min)/angle_increment

def  Setup_tab_of_value(self):
    for i in range(self.Tab_length):
        data = self.ranges[self.get_indice(-110+i)]
        self.Tab_of_value[i]= data;
        self.total_sum += data;


def Tab_update(slef): # rend la moyenne (8 bits) après nouvelle donnée dd
    self.total_sum -= self.Tab_of_value[self.Tab_length]  # on soustrait la plus ancienne valeur
    self.total_sum += dd  # on ajoute la nouvelle
    self.Tab_of_value[self.Tab_length] = dd  # table à jour

    if (++ptTaGlis==self.Tab_length):
        ptTaGlis=0     # incrémentation circulaire
    return (toTable/self.Tab_lengthis);
}