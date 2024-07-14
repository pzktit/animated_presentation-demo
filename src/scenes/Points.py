from manim_slides import Slide
from manim import *
from lib.addons import addons

class Points(Slide,addons):
    def slide_point(self, text, position=np.array([-6.5, 3.5, 0]), width=config.frame_width * 0.4, font="DejaVu Sans", font_size=24):
        return self.next_list_element(position, width, text, background_color=GREEN_B, background_opacity=0.8,font=font, font_size=font_size)
    def show_points(self, texts, initpos, callback=None):
        pos = initpos
        for text in texts:
            pos = self.slide_point(text,pos)
            if callback is not None:
                callback()

    def construct(self):
        self.font=f"Latin Modern Sans"
        self.head_font_size=36
        plane = self.add(NumberPlane())
        logo = SVGMobject("assets/icons/kubernets/logo.svg")
        logo.scale(0.5)
        logo.to_edge(UR).shift(0.25*UR)
        self.add(logo)
        self.item_font_size=24
        slide_texts = ["Cluster is composed of nodes", "Nodes are platform to run PODs", "Good morning"]
        initpos = np.array([-6.5, 3.5, 0])
        header = self.items_header(initpos, "Kubernets clusters",font=self.font, font_size=self.head_font_size)
        self.next_slide()
        canvas_width = self.camera.frame_width
        pos = self.slide_point(slide_texts[0],header.get_corner(DL)+0.5*RIGHT+0.2*DOWN)
        rect = Rectangle(width=1, height=2, fill_opacity=1, fill_color=BLUE).scale(0.7)
        icon = SVGMobject("assets/icons/kubernets/infrastructure_components/unlabeled/node.svg")
        icon.scale_to_fit_width(rect.width/3)
        icon.move_to(rect.get_corner(UR))
        node1 = VGroup(rect, icon)
        node_spacing = (canvas_width/2-3*node1.width)/4
        node1.to_edge(RIGHT,buff=node_spacing)
        self.play(FadeIn(node1))
        node2 = node1.copy()
        self.play(FadeIn(node2))
        self.play(node2.animate.shift((node_spacing+node2.width)*LEFT))
        node3 = node2.copy()
        self.play(FadeIn(node3))
        self.play(node3.animate.shift((node_spacing+node3.width)*LEFT))
        self.next_slide()
        pos = self.slide_point(slide_texts[1],pos)
        podicon1 = SVGMobject("assets/icons/kubernets/resources/unlabeled/pod.svg")
        podicons = [podicon1.copy(), podicon1.copy(), podicon1.copy()]
        nodes = [node1, node2, node3]
        for k in range(3):
            podicons[k].scale_to_fit_width(nodes[k].width/2).next_to(nodes[k].get_top(),DOWN)
            nodes[k].add(podicons[k]) 
        self.play(GrowFromPoint(podicons[0], nodes[0].get_corner(UR)),GrowFromPoint(podicons[1], nodes[1].get_corner(UR)),GrowFromPoint(podicons[2], nodes[2].get_corner(UR)))
        self.next_slide()
        pos = self.slide_point(slide_texts[2],pos)
        self.next_slide()
        # self.show_points(slide_texts, header.get_corner(DL)+0.5*RIGHT+0.2*DOWN, callback=self.next_slide)
        self.wait()
