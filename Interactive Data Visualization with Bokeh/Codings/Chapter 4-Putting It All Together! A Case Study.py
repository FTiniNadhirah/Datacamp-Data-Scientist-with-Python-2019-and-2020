# Exercise
# Some exploratory plots of the data
# Here, you'll continue your Exploratory Data Analysis by making a simple plot of Life Expectancy vs Fertility for the year 1970.

# Your job is to import the relevant Bokeh modules and then prepare a ColumnDataSource object with the fertility, life and Country columns, where you only select the rows with the index value 1970.

# Remember, as with the figures you generated in previous chapters, you can interact with your figures here with a variety of tools.

# Instructions

# Import output_file and show from bokeh.io, figure from bokeh.plotting, and HoverTool and ColumnDataSource from bokeh.models.
# Make a ColumnDataSource called source with x set to the fertility column, y set to the life column and country set to the Country column. For all columns, select the rows with index value 1970. This can be done using data.loc[1970].column_name.
# Perform necessary imports
from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.models import HoverTool, ColumnDataSource

# Make the ColumnDataSource: source
source = ColumnDataSource(data={
    'x'       : data.loc[1970].fertility,
    'y'       : data.loc[1970].life,
    'country' : data.loc[1970].Country,
})

# Create the figure: p
p = figure(title='1970', x_axis_label='Fertility (children per woman)', y_axis_label='Life Expectancy (years)',
           plot_height=400, plot_width=700,
           tools=[HoverTool(tooltips='@country')])

# Add a circle glyph to the figure p
p.circle(x='x', y='y', source=source)

# Output the file and show the figure
output_file('gapminder.html')
show(p)

# Exercise
# Beginning with just a plot
# Let's get started on the Gapminder app. Your job is to make the ColumnDataSource object, prepare the plot, and add circles for Life expectancy vs Fertility. You'll also set x and y ranges for the axes.

# As in the previous chapter, the DataCamp environment executes the bokeh serve command to run the app for you. When you hit 'Submit Answer', you'll see in the IPython Shell that bokeh serve script.py gets called to run the app. This is something to keep in mind when you are creating your own interactive visualizations outside of the DataCamp environment.

# Instructions

# Make a ColumnDataSource object called source with 'x', 'y', 'country', 'pop' and 'region' keys. The Pandas selections are provided for you.
# Save the minimum and maximum values of the life expectancy column data.life as ymin and ymax. As a guide, you can refer to the way we saved the minimum and maximum values of the fertility column data.fertility as xmin and xmax.
# Create a plot called plot by specifying the title, setting plot_height to 400, plot_width to 700, and adding the x_range and y_range parameters.
# Add circle glyphs to the plot. Specify an fill_alpha of 0.8 and source=source.
from bokeh.io import curdoc
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure

# Make the ColumnDataSource: source
source = ColumnDataSource(data={
    'x'       : data.loc[1970].fertility,
    'y'       : data.loc[1970].life,
    'country' : data.loc[1970].Country,
    'pop'     : (data.loc[1970].population / 20000000) + 2,
    'region'  : data.loc[1970].region,
})

# Save the minimum and maximum values of the fertility column: xmin, xmax
xmin, xmax = min(data.fertility), max(data.fertility)

# Save the minimum and maximum values of the life expectancy column: ymin, ymax
ymin, ymax = min(data.life), max(data.life)

# Create the figure: plot
plot = figure(title='Gapminder Data for 1970', plot_height=400, plot_width=700,
              x_range=(xmin, xmax), y_range=(ymin, ymax))

# Add circle glyphs to the plot
plot.circle(x='x', y='y', fill_alpha=0.8, source=source)

# Set the x-axis label
plot.xaxis.axis_label ='Fertility (children per woman)'

# Set the y-axis label
plot.yaxis.axis_label = 'Life Expectancy (years)'

# Add the plot to the current document and add a title
curdoc().add_root(plot)
curdoc().title = 'Gapminder'

# Exercise
# Enhancing the plot with some shading
# Now that you have the base plot ready, you can enhance it by coloring each circle glyph by continent.

# Your job is to make a list of the unique regions from the data frame, prepare a ColorMapper, and add it to the circle glyph.

# Instructions

# Make a list of the unique values from the region column. You can use the unique() and tolist() methods on data.region to do this.
# Import CategoricalColorMapper from bokeh.models and the Spectral6 palette from bokeh.palettes.
# Use the CategoricalColorMapper() function to make a color mapper called color_mapper with factors=regions_list and palette=Spectral6.
# Add the color mapper to the circle glyph as a dictionary with dict(field='region', transform=color_mapper) as the argument passed to the color parameter of plot.circle(). Also set the legend parameter to be the 'region'.
# Set the legend.location attribute of plot to 'top_right'.
# Make a list of the unique values from the region column: regions_list
regions_list = data.region.unique().tolist()

# Import CategoricalColorMapper from bokeh.models and the Spectral6 palette from bokeh.palettes
from bokeh.models import CategoricalColorMapper
from bokeh.palettes import Spectral6

# Make a color mapper: color_mapper
color_mapper = CategoricalColorMapper(factors=regions_list, palette=Spectral6)

# Add the color mapper to the circle glyph
plot.circle(x='x', y='y', fill_alpha=0.8, source=source,
            color=dict(field='region', transform=color_mapper), legend='region')

# Set the legend.location attribute of the plot to 'top_right'
plot.legend.location = 'top_right'

# Add the plot to the current document and add the title
curdoc().add_root(plot)
curdoc().title = 'Gapminder'

# Exercise
# Adding a slider to vary the year
# Until now, we've been plotting data only for 1970. In this exercise, you'll add a slider to your plot to change the year being plotted. To do this, you'll create an update_plot() function and associate it with a slider to select values between 1970 and 2010.

# After you are done, you may have to scroll to the right to view the entire plot. As you play around with the slider, notice that the title of the plot is not updated along with the year. This is something you'll fix in the next exercise!

# Instructions

# Import the widgetbox and row functions from bokeh.layouts, and the Slider function from bokeh.models.
# Define the update_plot callback function with parameters attr, old and new.
# Set the yr name to slider.value and set source.data = new_data.
# Make a slider object called slider using the Slider() function with a start year of 1970, end year of 2010, step of 1, value of 1970, and title of 'Year'.
# Attach the callback to the 'value' property of slider. This can be done using on_change() and passing in 'value' and update_plot.
# Make a row layout of widgetbox(slider) and plot and add it to the current document.
# Import the necessary modules
from bokeh.layouts import row, widgetbox
from bokeh.models import Slider

# Define the callback function: update_plot
def update_plot(attr, old, new):
    # set the `yr` name to `slider.value` and `source.data = new_data`
    yr = slider.value
    new_data = {
        'x'       : data.loc[yr].fertility,
        'y'       : data.loc[yr].life,
        'country' : data.loc[yr].Country,
        'pop'     : (data.loc[yr].population / 20000000) + 2,
        'region'  : data.loc[yr].region,
    }
    source.data = new_data


# Make a slider object: slider
slider = Slider(start=1970, end=2010, step=1, value=1970, title='Year')

# Attach the callback to the 'value' property of slider
slider.on_change('value', update_plot)

# Make a row layout of widgetbox(slider) and plot and add it to the current document
layout = row(widgetbox(slider), plot)
curdoc().add_root(layout)

# Exercise
# Customizing based on user input
# Remember how in the plot from the previous exercise, the title did not update along with the slider? In this exercise, you'll fix this.

# In Python, you can format strings by specifying placeholders with the % keyword. For example, if you have a string company = 'DataCamp', you can use print('%s' % company) to print DataCamp. Placeholders are useful when you are printing values that are not static, such as the value of the year slider. You can specify a placeholder for a number with %d. Here, when you're updating the plot title inside your callback function, you should make use of a placeholder so that the year displayed is in accordance with the value of the year slider.

# In addition to updating the plot title, you'll also create the callback function and slider as you did in the previous exercise, so you get a chance to practice these concepts further.

# All necessary modules have been imported for you, and as in the previous exercise, you may have to scroll to the right to view the entire figure.

# Instructions

# Define the update_plot callback function with parameters attr, old and new.
# Inside update_plot(), assign the value of the slider, slider.value, to yr and set source.data = new_data.
# Inside update_plot(), specify plot.title.text to update the plot title and add it to the figure. You want the plot to update based on the value of the slider, which you have assigned above to yr. Make use of the placeholder syntax provided for you.
# Make a slider object called slider using the Slider() function with a start year of 1970, end year of 2010, step of 1, value of 1970, and title of 'Year'.
# Attach the callback to the 'value' property of slider. This can be done using on_change() and passing in 'value' and update_plot.
# Define the callback function: update_plot
def update_plot(attr, old, new):
    # Assign the value of the slider: yr
    yr = slider.value
    # Set new_data
    new_data = {
        'x'       : data.loc[yr].fertility,
        'y'       : data.loc[yr].life,
        'country' : data.loc[yr].Country,
        'pop'     : (data.loc[yr].population / 20000000) + 2,
        'region'  : data.loc[yr].region,
    }
    # Assign new_data to: source.data
    source.data = new_data

    # Add title to figure
    plot.title.text = 'Gapminder data for %d' % yr

# Make a slider object: slider
slider = Slider(start=1970, end=2010, step=1, value=1970, title='Year')

# Attach the callback to the 'value' property of slider
slider.on_change('value', update_plot)

# Make a row layout of widgetbox(slider) and plot and add it to the current document
layout = row(widgetbox(slider), plot)
curdoc().add_root(layout)

# Exercise
# Adding a hover tool
# In this exercise, you'll practice adding a hover tool to drill down into data column values and display more detailed information about each scatter point.

# After you're done, experiment with the hover tool and see how it displays the name of the country when your mouse hovers over a point!

# The figure and slider have been created for you and are available in the workspace as plot and slider.

# Instructions

# Import HoverTool from bokeh.models.
# Create a HoverTool object called hover with tooltips=[('Country', '@country')].
# Add the HoverTool object you created to the plot using add_tools().
# Create a row layout using widgetbox(slider) and plot.
# Add the layout to the current document. This has already been done for you.
# Import HoverTool from bokeh.models
from bokeh.models import HoverTool

# Create a HoverTool: hover
hover = HoverTool(tooltips=[('Country', '@country')])

# Add the HoverTool to the plot
plot.add_tools(hover)

# Create layout: layout
layout = row(widgetbox(slider), plot)

# Add layout to current document
curdoc().add_root(layout)

# Exercise
# Adding dropdowns to the app
# As a final step in enhancing your application, in this exercise you'll add dropdowns for interactively selecting different data features. In combination with the hover tool you added in the previous exercise, as well as the slider to change the year, you'll have a powerful app that allows you to interactively and quickly extract some great insights from the dataset!

# All necessary modules have been imported, and the previous code you wrote is taken care of. In the provided sample code, the dropdown for selecting features on the x-axis has been added for you. Using this as a reference, your job in this final exercise is to add a dropdown menu for selecting features on the y-axis.

# Take a moment, after you are done, to enjoy exploring the visualization by experimenting with the hover tools, sliders, and dropdown menus that you have learned how to implement in this course.

# Instructions

# Inside the update_plot() callback function, read in the current value of the y dropdown, y_select.
# Use plot.yaxis.axis_label to label the y-axis as y.
# Set the start and end range of the y-axis of plot.
# Specify the parameters of the y_select dropdown widget: options, value, and title. The default value should be 'life'.
# Attach the callback to the 'value' property of y_select. This can be done using on_change() and passing in 'value' and update_plot.
# Define the callback: update_plot
def update_plot(attr, old, new):
    # Read the current value off the slider and 2 dropdowns: yr, x, y
    yr = slider.value
    x = x_select.value
    y = y_select.value
    # Label axes of plot
    plot.xaxis.axis_label = x
    plot.yaxis.axis_label = y
    # Set new_data
    new_data = {
        'x'       : data.loc[yr][x],
        'y'       : data.loc[yr][y],
        'country' : data.loc[yr].Country,
        'pop'     : (data.loc[yr].population / 20000000) + 2,
        'region'  : data.loc[yr].region,
    }
    # Assign new_data to source.data
    source.data = new_data

    # Set the range of all axes
    plot.x_range.start = min(data[x])
    plot.x_range.end = max(data[x])
    plot.y_range.start = min(data[y])
    plot.y_range.end = max(data[y])

    # Add title to plot
    plot.title.text = 'Gapminder data for %d' % yr

# Create a dropdown slider widget: slider
slider = Slider(start=1970, end=2010, step=1, value=1970, title='Year')

# Attach the callback to the 'value' property of slider
slider.on_change('value', update_plot)

# Create a dropdown Select widget for the x data: x_select
x_select = Select(
    options=['fertility', 'life', 'child_mortality', 'gdp'],
    value='fertility',
    title='x-axis data'
)

# Attach the update_plot callback to the 'value' property of x_select
x_select.on_change('value', update_plot)

# Create a dropdown Select widget for the y data: y_select
y_select = Select(
    options=['fertility', 'life', 'child_mortality', 'gdp'],
    value='life',
    title='y-axis data'
)

# Attach the update_plot callback to the 'value' property of y_select
y_select.on_change('value', update_plot)

# Create layout and add to current document
layout = row(widgetbox(slider, x_select, y_select), plot)
curdoc().add_root(layout)
