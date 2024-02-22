# Program 1
# from diagrams import Diagram
# from diagrams.aws.compute import EC2

# with Diagram("Simple Diagram"):
#     EC2("web")

# Program 2
# from diagrams import Diagram
# from diagrams.aws.compute import EC2

# with Diagram("Simple Diagram") as diag:
#     EC2("web")
# diag

# Program 3
#from diagrams import Diagram
#from diagrams.aws.compute import EC2

#with Diagram("Simple Diagram", outformat="jpg"):
#with Diagram("Simple Diagram", outformat="png"): => Default
#with Diagram("Simple Diagram", outformat="svg"):
#with Diagram("Simple Diagram", outformat="pdf"):
#with Diagram("Simple Diagram", outformat="dot"):
# with Diagram("Simple Diagram"):
#     EC2("web")

# Program 4: At a time multiple formats
# from diagrams import Diagram
# from diagrams.aws.compute import EC2

# with Diagram("Simple Diagram Multi Output", outformat=["jpg", "png", "dot"]):
#     EC2("web")

# Program 5: Specify which name you want to save as fileName using this property
# from diagrams import Diagram
# from diagrams.aws.compute import EC2

# with Diagram("Simple Diagram", filename="my_diagram"):
#     EC2("web")

# Program 6: If you don't want to render immediately as a popup, Background it creates
# from diagrams import Diagram
# from diagrams.aws.compute import EC2

# with Diagram("Simple Diagram", show=False):
#     EC2("web")

#Program 7: Adjust Graphviz properties => Displays the object in transparent
# from diagrams import Diagram
# from diagrams.aws.compute import EC2

# graph_attr = {
#     "fontsize": "45",
#     "bgcolor": "transparent"
# }

# with Diagram("Simple Diagram", show=False, graph_attr=graph_attr):
#     EC2("web")