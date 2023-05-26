import numpy as np

from bokeh.layouts import column
from bokeh.models import Slider, CustomJS, ColumnDataSource
from bokeh.plotting import figure, show
import math

h_size = 3.14 * 4
h_shift_len = h_size / 2
# Create a main chart
x = np.linspace(-h_size, h_size, 500)
y = np.sin(x)

source = ColumnDataSource(data=dict(x=x, y=y))

plot = figure(y_range=(-10, 10), width=400, height=400)

plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6)

# Create a slider
a = Slider(title="Center Value (a)", start=-6.28, end=6.28, step=1.571, value=0)
degree = Slider(title="Degree of Taylor Polynomial", start=0, end=6, step=1, value=0)

# Define a JavaScript callback function
callback = CustomJS(args=dict(plot=plot, a=a, degree=degree, h_shift_len=h_shift_len), code="""
    // Get the selected value from the slider
    var selectedValue = a.value;

    // Calculate the new range around the selected value
    var newStart = selectedValue - h_shift_len;
    var newEnd = selectedValue + h_shift_len;

    // Update the range of the main chart
    plot.x_range.start = newStart;
    plot.x_range.end = newEnd;
""")

# Attach the callback function to the slider's 'value' property
a.js_on_change('value', callback)
degree.js_on_change('value', callback)

# Display the chart and the slider
layout = column(plot, a)
# show(layout)
