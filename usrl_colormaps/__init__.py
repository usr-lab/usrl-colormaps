import matplotlib
import numpy as np


ORANGE = np.array([244,114,22, 255]) / 255 # orange
RED = np.array([241,69,91, 255]) / 255 # red
GREEN = np.array([151,211,33, 255]) / 255 # green
BLUE = np.array([98,200,243, 255]) / 255  # blue
OFF_WHITE = np.array([245, 245, 245, 255]) / 255
WHITE = np.array([255, 255, 255, 255]) / 255

usr_reds = matplotlib.colors.ListedColormap(np.linspace(OFF_WHITE, RED, 255), name="usr_reds")
usr_blues = matplotlib.colors.ListedColormap(np.linspace(OFF_WHITE, BLUE, 255), name="usr_blues")
usr_greens = matplotlib.colors.ListedColormap(np.linspace(OFF_WHITE, GREEN, 255), name="usr_greens")
usr_oranges = matplotlib.colors.ListedColormap(np.linspace(OFF_WHITE, ORANGE, 255), name="usr_oranges")
usr_diverge = matplotlib.colors.ListedColormap(np.vstack((np.linspace(BLUE, WHITE, 255), np.linspace(WHITE, RED, 255))), name="usr_diverging")
usr_diverge2 = matplotlib.colors.ListedColormap(np.vstack((np.linspace(GREEN, WHITE, 255), np.linspace(WHITE, ORANGE, 255))), name="usr_diverging2")
usr_qualitative = matplotlib.colors.ListedColormap((RED, BLUE, ORANGE, GREEN), name="usr_qualitative")

matplotlib.cm.register_cmap(cmap=usr_reds)
matplotlib.cm.register_cmap(cmap=usr_blues)
matplotlib.cm.register_cmap(cmap=usr_greens)
matplotlib.cm.register_cmap(cmap=usr_oranges)
matplotlib.cm.register_cmap(cmap=usr_diverge)
matplotlib.cm.register_cmap(cmap=usr_diverge2)
matplotlib.cm.register_cmap(cmap=usr_qualitative)
