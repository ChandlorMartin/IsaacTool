from django.urls import path
from IsaacTool.views.mechanics import average_speed
from IsaacTool.views.IsaacTool import directory
from IsaacTool.views.thermalPhysics import linear_thermal_expansion
from IsaacTool.views.mechanics import vector_addition

urlpatterns = [
    path("", directory.index, name="directory"),
    path("average_speed/", average_speed.AverageSpeedView.as_view(), name="average speed"),
    path("directory/", directory.index, name="directory"),
    path("linear_thermal_expansion/", linear_thermal_expansion.LinearThermalExpansionView.as_view(), name="linear thermal expansion"),
    path("vector_addition/", vector_addition.VectorAdditionView.as_view(), name="vector addition")
]
