import ttkbootstrap as tb
from ttkbootstrap.constants import BOTH, YES
from ttkbootstrap.validation import add_regex_validation
from ttkbootstrap.style import Bootstyle
from ttkbootstrap.scrolled import ScrolledFrame
from ttkbootstrap.utility import enable_high_dpi_awareness
from functools import partial


from DoubleScrolledFrame import DoubleScrolledFrame
from input_setup import CreateInputWidgets
from nodes_transformations_setup import AddNode
from utils import CollapsingFrame, make_button
from make_json import make_json
from sys import platform

from edges_setup import AddEdgeWidgets
# GUI window

main_window = tb.Window(themename="superhero", minsize=(300, 1))

if platform == "linux" or platform == "linux2":
    enable_high_dpi_awareness(main_window, scaling=2)
    main_window.geometry("2500x2136")

else:
    main_window.geometry("1400x950")

main_window.title("BidsSM maker")

# Turn it into a scrolled frame
scrolling_window = DoubleScrolledFrame(main_window)
scrolling_window.pack(fill=BOTH, expand=YES, padx=10, pady=10)

# Set up so all added frames (added to cf) will be collapsing frames
cf = CollapsingFrame(scrolling_window)
cf.pack(fill=BOTH)
label_width = 30
s = tb.Style()
s.configure(".", font=("Helvetica", 18))

# Inputs Section
top_level_frame = tb.Frame(cf, padding=10)
top_level_data = CreateInputWidgets(top_level_frame)
cf.add(child=top_level_frame, title="Top level data")

# Nodes
nodes_frame = tb.Frame(cf, padding=10)
node_widgets = AddNode(nodes_frame)
cf.add(child=nodes_frame, title="Nodes")

# Edges
edges_frame = tb.Frame(cf, padding=10)
edge_widgets = AddEdgeWidgets(edges_frame)
cf.add(child=edges_frame, title="Edges")

# Button to display json
make_button(
    main_window,
    "Show Model Spec!",
    partial(make_json, top_level_data, node_widgets, edge_widgets),
)

main_window.mainloop()
