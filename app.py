# Import dependencies
import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render

# Set page options for the overall app
ui.page_opts(title= "PyShiny App with Plot", fillable=True)

# Creade sidebar with slider input
with ui.sidebar():
    ui.input_slider("selected_number_of_bins", "Number of bins", 0, 100, 20)

# Create historgram
@render.plot(alt="A histogram showing random data distribution")
def draw_histogram():
    count_of_points: int = 437
    np.random.seed(3)
    random_data_array = 100 + 15 * np.random.randn(count_of_points)
    plt.hist(random_data_array, input.selected_number_of_bins(), density=True)
