#Importando o pyplot
from matplotlib import pyplot as plt

# Eixo_x, Eixo_y
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.axis('off')
plt.savefig('line5.png')
plt.show()
plt.close()

