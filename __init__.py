"""
Example panels.

| Copyright 2017-2024, Voxel51, Inc.
| `voxel51.com <https://voxel51.com/>`_
|
"""
import os

import fiftyone.operators as foo
import fiftyone.operators.types as types


IMAGE_URL = "https://images.plot.ly/language-icons/api-home/python-logo.png"


class PlotlyImageExample(foo.Panel):
    @property
    def config(self):
        return foo.PanelConfig(
            name="example_plotly_image",
            label="Example: PlotlyImage",
        )

    def on_load(self, ctx):

        ctx.panel.data.scatter ={"x": [1.0,2.0,3.0], "y": [1.1,2.2,3.3], "type": "scatter"}
                                    
        # Launch panel in a horizontal split view
        ctx.ops.split_panel("example_plotly_image", layout="horizontal")

    def on_change_view(self, ctx):
        # Update histogram when current view changes
        self.on_load(ctx)

    def on_plot_click(self, ctx):
        ctx.ops.clear_view()
        self.on_load(ctx)
        
    def reset(self, ctx):
        ctx.ops.clear_view()
        self.on_load(ctx)

    def render(self, ctx):
        panel = types.Object()

        panel.plot(
            "scatter",
            layout={
                "xref":"paper",
                "yref":"paper",
                "sizing":"stretch",               
                "images":[{"source":IMAGE_URL, 
                           "opacity":0.5,
                            "layer":"below",
                            "name":"logo",
                            "x":0.5,
                            "y":0.5,
                            "sizex":1,
                            "sizey":1,
                            "xanchor":"center",
                            "yanchor":"middle",
                            }]
            },
            on_click=self.on_plot_click,
        )
      


        return types.Property(
            panel,
            view=types.GridView(
                align_x="center",
                align_y="center",
                orientation="vertical",
                height=100,
                width=100,
                gap=2,
                padding=0,
            ),
        )




def register(p):
    p.register(PlotlyImageExample)
