from django.shortcuts import render
from  django.views import View
from decimal import Decimal
from IsaacTool.forms.mechanics.vector_form import VectorForm
from IsaacTool.utilities import to_decimal_list
import plotly.graph_objects as go


class VectorAdditionView(View):
    template_name = "../templates/mechanics/vector_addition.html"
    form_class = VectorForm

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = VectorForm(request.POST)
            if form.is_valid():
                i = form.cleaned_data['i']
                j = form.cleaned_data['j']
                k = form.cleaned_data['k']

                # This gets a list of each vector value, adds them up, and
                # gets a list of vectors with the resultant vector appended to the end
                i_values = to_decimal_list(i)
                j_values = to_decimal_list(j)
                k_values = to_decimal_list(k)
                vectors = [(i, j, k) for i, j, k in zip(i_values, j_values, k_values)]
                resultant_vector = (0, 0, 0)
                for vector in vectors:
                    resultant_vector = (resultant_vector[0] + vector[0], resultant_vector[1] + vector[1],
                                        resultant_vector[2] + vector[2])

                vectors.append(resultant_vector)

                # This finds out how many vectors there are copies of so that the count can be added to the annotation
                vector_counts = {}
                for vector in vectors:
                    vector_tuple = tuple(vector)  # Convert vector to tuple for hashing
                    if vector_tuple in vector_counts:
                        vector_counts[vector_tuple] += 1
                    else:
                        vector_counts[vector_tuple] = 1

                vector_index = 0
                traces = []
                for vector in vectors:
                    if vector_index == len(vectors) - 1:
                        color = 'red'
                    else:
                        color = 'blue'

                    traces.append(go.Scatter3d(x=[0, vector[0]],
                                               y=[0, vector[1]],
                                               z=[0, vector[2]],
                                               mode='lines',
                                               line=dict(color=color),
                                               name='Vector'))

                    vector_index += 1

                # This adds traces to the figure
                fig = go.Figure(data=traces)

                # This adds annotations to the end of the vectors
                annotations = [
                    dict(
                        showarrow=True,
                        arrowhead=2,
                        ax=(vector[0] + 0) / 2,
                        ay=(vector[1] + 0) / 2,
                        x=vector[0],
                        y=vector[1],
                        z=vector[2],
                        text=f'({vector[0]}, {vector[1]}, {vector[2]}) Count: {vector_counts[tuple(vector)]}',
                        xanchor='auto',
                        yanchor='auto',
                        font=dict(size=12)
                    ) for vector in vectors
                ]

                # This will update the size of the graph and add axis lines
                fig.update_layout(
                    autosize=True,
                    showlegend=False,
                    width=400,
                    height=600,
                    margin=dict(l=0, r=0, b=0, t=0),
                    scene=dict(
                        xaxis=dict(showline=True, zeroline=True),
                        yaxis=dict(showline=True, zeroline=True),
                        zaxis=dict(showline=True, zeroline=True),
                        annotations=annotations
                    )
                )

                # This converts the plot so that it can be embedded in the html and
                # also changes the vector so that it displays properly
                plot_html = fig.to_html(full_html=False)
                resultant_vector = (float(resultant_vector[0]), float(resultant_vector[1]), float(resultant_vector[2]))

                # Pass the HTML string to the template context
                context = {'i': i, 'j': j, 'k': k, 'plot_html': plot_html, 'resultant_vector': resultant_vector}

                return render(request, self.template_name, context)
            else:
                i = form.data.get('i')
                j = form.data.get('j')
                k = form.data.get('k')

                return render(request, self.template_name,{'i': i, 'j': j, 'k': k, 'form': form})
        else:
            form = VectorForm()

        return render(request, self.template_name, {'form': form})