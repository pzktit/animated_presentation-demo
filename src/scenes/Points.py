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

    def get_kubernetes_icon(self, 
                            icon_name, 
                            path="assets/icons/kubernets/", extension='svg', 
                            width=1):
        icon_path = path + icon_name + "." + extension
        return SVGMobject(icon_path,width=width)


    def construct(self):
        self.font=f"Latin Modern Sans"
        self.head_font_size=36
        plane = self.add(NumberPlane())
        logo = self.get_kubernetes_icon("logo") #SVGMobject("assets/icons/kubernets/logo.svg")
        logo.scale(0.5)
        logo.to_edge(UR).shift(0.25*UR)
        self.add(logo)
        self.item_font_size=24
        slide_texts = ["Cluster is composed of nodes", "Nodes are platform to run PODs", "Good morning"]
        initpos = np.array([-6.5, 3.5, 0])
        header = self.items_header(initpos, "Kubernets clusters",font=self.font, font_size=self.head_font_size)
        self.next_slide()

        # Prepare base picture
        canvas_width = self.camera.frame_width
        num_nodes = 3
        # create bounding rectangles, they won't be placed on a plane
        # smaller rectangles will be placed at their centers
        bound_rect = Rectangle(width=canvas_width*0.5/num_nodes, height=2, color=RED)
        bounding_rectangles = VGroup(*[
            bound_rect.copy()
            for k in range(num_nodes)
        ])
        bounding_rectangles.arrange(RIGHT, buff=0).shift(bounding_rectangles.width/2*RIGHT).shift(2*DOWN)
        # self.add(bounding_rectangles)

        # Create and position the rectangles at the center of the most left bounding rectangles
        nodes = VGroup(*[
            VGroup(Rectangle(width=1, height=2, color=BLUE,fill_opacity=1).scale(0.7).move_to(bounding_rectangles[0].get_center()))
            for k in range(num_nodes)
        ])
        nodeicon = self.get_kubernetes_icon("node")
        for node in nodes:
            icon=nodeicon.copy().scale_to_fit_width(node.width/3).move_to(node.get_corner(UR))
            node.add(icon)
        # Animation starts
        pos = self.slide_point("Cluster is composed of nodes",header.get_corner(DL)+0.5*RIGHT+0.2*DOWN)
        self.play(FadeIn(nodes[0]))
        self.add(nodes[1],nodes[2])
        make_copy_node1_animation = nodes[1].animate.move_to(bounding_rectangles[1].get_center())
        make_copy_node2_animation = nodes[2].animate.move_to(bounding_rectangles[2].get_center())
        self.play(make_copy_node1_animation,make_copy_node2_animation, run_time=0.5)
        self.next_slide()

        podicon = self.get_kubernetes_icon("pod")
        # Place icons in the corners of a triangle, triangle won't be displayed
        num_pods=3
        triangle = RegularPolygon(n=num_pods,fill_opacity=0,start_angle=PI/6).scale(0.7)
        manypods = VGroup(*[
            podicon.copy().move_to(triangle.get_vertices()[i])
            for i in range(num_pods)
        ])
        podicons = [manypods.copy() for k in range(num_nodes)]
        # for k in range(num_nodes):
        #     podicons[k].scale_to_fit_width(nodes[k][0].width*0.9) # this rectangle width
        #     podicons[k].move_to(nodes[k][0].get_center()) # this refers to the center point of the rectangle
        #     podicons[k].shift(nodes[k][0].height/8*UP) # empirical value
        #     # nodes[k].add(podicons[k]) 
        for k in range(num_nodes):
            podicons[k].scale_to_fit_width(nodes[k][0].width*0.9) # this rectangle width
            podicons[k].move_to(nodes[k][0].get_center()+nodes[k][0].height*0.25*DOWN) 
            podicons[k].shift(nodes[k][0].height/8*UP) # empirical value

        # Animation starts
        pos = self.slide_point("Nodes are platform to run PODs",pos)
        self.play([ GrowFromPoint(podicons[k], nodes[k].get_corner(UR)) for k in range(num_nodes)] )
        # ,GrowFromPoint(podicons[1], nodes[1].get_corner(UR)),GrowFromPoint(podicons[2], nodes[2].get_corner(UR)))
        for k in range(num_nodes):
            nodes[k].add(podicons[k])   
        self.next_slide()

        kproxyicon = self.get_kubernetes_icon("k-proxy").scale_to_fit_width(nodes[0][0].width*0.8)
        kproxies = VGroup(*[
            kproxyicon.copy().move_to(nodes[k][0].get_edge_center(UP))
            for k in range(num_nodes)
        ])
        lines = []
        for k in range(num_nodes):
            picons=nodes[k][2]
            for pod in picons:
                line = Line(start=kproxies[k].get_bottom(), end=pod.get_top())
                lines.append(line.copy())
        # Animation starts
        pos = self.slide_point("PODs are managed by Kube Proxy",pos)
        self.play(*[GrowFromPoint(kproxies[k], nodes[k].get_edge_center(UP)) for k in range(num_nodes)]) 
        self.play( [FadeIn(line) for line in lines] )
        self.next_slide()

        # Draw abstract network/service layer
        service0 = VGroup(Rectangle(width=bounding_rectangles[0].width*1.5, height=0.5, color=BLUE, fill_opacity=0.7, fill_color=GREEN))
        service0 = service0.move_to(RIGHT * service0.width / 2+ node[0].get_top()*UP + UP*2)
        service_icon = self.get_kubernetes_icon("svc", width=1)
        # add service icon in the middle of the rectangle and scaled to 0.8 its height
        service_icon.scale_to_fit_height(service0.height).scale(0.8).move_to(service0.get_center())
        service0.add(service_icon)
        service1=service0.copy().shift(RIGHT * service0.width)
        text = ( 
            Text(r"Service 0",color=BLACK)
            .scale_to_fit_height(service0.height*0.4)
            .next_to(service0.get_edge_center(LEFT),buff=0.1)
        )
        service0.add(text)
        pos = self.slide_point("Proxies form virtual layer ...",pos)
        self.play(FadeIn(service0))
        self.next_slide()
        pos = self.slide_point("that provides entry to the service",pos)
        arrows_svc0=VGroup()
        for n in nodes:
            arrow = Arrow(start=service0.get_edge_center(DOWN), end=n.get_edge_center(UP), color=YELLOW, buff=0, tip_length=0.1,tip_shape=StealthTip)
            arrows_svc0.add(arrow)
        self.play( *[GrowArrow(arrows_svc0[k]) for k in range(num_nodes)] )
        self.next_slide()

        text = ( 
            Text(r"Service 1",color=BLACK)
            .scale_to_fit_height(service1.height*0.4)
            .next_to(service1.get_edge_center(LEFT),buff=0.1)
        )
        pos = self.slide_point("cluster may provide many sevices",pos)
        service1.add(text)
        self.play(FadeIn(service1))
        arrows_svc1=VGroup()
        for n in nodes:
            arrow = Arrow(start=service1.get_edge_center(DOWN), end=n.get_edge_center(UP), color=YELLOW, buff=0, tip_length=0.1,tip_shape=StealthTip)
            arrows_svc1.add(arrow)
        self.play( *[GrowArrow(arrows_svc1[k]) for k in range(num_nodes)] )
        self.next_slide()

        ingress_icon = self.get_kubernetes_icon("ing", width=1).scale_to_fit_width(nodes[0][0].width)
        ingress_icon.move_to(service0.get_edge_center(RIGHT)).shift(2*UP)

        ingarrow0 = Arrow(start=ingress_icon.get_corner(DL), end=service0.get_edge_center(UP), color=YELLOW,tip_length=0.1,tip_shape=StealthTip)
        label0 = Text("/App0",color=WHITE).scale_to_fit_height(service0[0].height).scale(0.5).next_to(ingarrow0.get_center(), direction=UL,buff=0.1)
        ingarrow1 = Arrow(start=ingress_icon.get_corner(DR), end=service1.get_edge_center(UP), color=YELLOW,tip_length=0.1,tip_shape=StealthTip)
        label1 = Text("/App1",color=WHITE).scale_to_fit_height(service1[0].height).scale(0.5).next_to(ingarrow1.get_center(), direction=UR,buff=0.1)
        label2=Text("https://mydomain.com",color=WHITE).scale_to_fit_height(service1[0].height).scale(0.5).move_to(ingress_icon.get_edge_center(UP)).shift(service1[0].height*UP)
        pos = self.slide_point("They are behind Ingress proxy",pos)
        self.play(FadeIn(ingress_icon),FadeIn(label2))
        self.play(GrowArrow(ingarrow0),GrowArrow(ingarrow1),FadeIn(label0),FadeIn(label1))
        
        # self.next_slide()
        # draw lines from k-proxy bottom edge to pods top edge


        # pos = self.slide_point(slide_texts[2],pos)
        # self.next_slide()
        # self.show_points(slide_texts, header.get_corner(DL)+0.5*RIGHT+0.2*DOWN, callback=self.next_slide)
        self.wait()
