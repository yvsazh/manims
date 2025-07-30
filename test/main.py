from manim import *
import numpy as np

class NeuralNetworkScene(MovingCameraScene):
    def construct(self):
        layers = [2, 4, 4, 1]
        network = VGroup()
        layer_vgroups = []

        for i, num_neurons in enumerate(layers):
            layer = VGroup()
            for j in range(num_neurons):
                neuron = Circle(radius=0.2, color=BLUE)
                neuron.set_fill(BLUE, opacity=1)
                neuron.move_to(RIGHT * i * 1.5 + UP * (j - (num_neurons-1)/2) * 0.7)
                layer.add(neuron)
            layer_vgroups.append(layer)
            network.add(layer)

        network.move_to(ORIGIN)

        lines = VGroup()

        for layer in layer_vgroups:
            self.play(LaggedStartMap(GrowFromCenter, layer), run_time=0.2)

        for l1, l2 in zip(layer_vgroups[:-1], layer_vgroups[1:]):
            for n1 in l1:
                for n2 in l2:
                    line = Line(n1.get_center(), n2.get_center(), color=GRAY, stroke_width=1.5)
                    line.set_z_index(-1)
                    self.play(Create(line), run_time = 0.01)
                    lines.add(line)
        self.wait(0.25)

        self.play(network.animate.shift(UP * 1.5), lines.animate.shift(UP * 1.5))

        nn_text = Text("Neural Network", font_size=48)
        nn_text.shift(DOWN * 1.5)
        
        self.play(Write(nn_text))

        self.play(FadeOut(nn_text), network.animate.shift(DOWN * 1.5), lines.animate.shift(DOWN * 1.5))


        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.scale(0.1).move_to(network[1][2]))

        self.play(network[1][2].animate.set_fill(BLACK, opacity=1), run_time=0.5)

        # sigmoid

        neuron = network[1][2]
        neuron_width = neuron.width
        neuron_height = neuron.height

        sigmoidAxes = Axes(
            x_range = (-5, 5),
            y_range = (-1, 1),
            tips = False,
            axis_config={"stroke_width": 0.2, "include_ticks": False,},
            y_axis_config={"stroke_width": 0.2},
            x_axis_config={"stroke_width": 0.2},
        )

        sigmoid = sigmoidAxes.plot(
            lambda x: 1 / (1 + np.exp(-x)),
            color=BLUE,
            stroke_width=0.5
        )

        sigmoid_group = VGroup(sigmoidAxes, sigmoid)
        sigmoid_group.shift(DOWN * 0.1)
        sigmoid_group.shift(LEFT * 0.1)

        sigmoid_text = Text("Sigmoid", font_size=12)
        sigmoid_text.scale(0.75)

        scale_factor = min(neuron_width, neuron_height) * 0.75 / max(sigmoid_group.width, sigmoid_group.height)
        sigmoid_group.scale(scale_factor)
        sigmoid_group.move_to(neuron.get_center())

        self.play(Create(sigmoid_group))
        self.play(Create(sigmoid_text.next_to(sigmoid_group, UP, buff=0.15)))

        self.wait(1)

        self.play(FadeOut(sigmoid_group), FadeOut(sigmoid_text), network[1][2].animate.set_fill(BLUE, opacity=1))
        self.play(Restore(self.camera.frame))
