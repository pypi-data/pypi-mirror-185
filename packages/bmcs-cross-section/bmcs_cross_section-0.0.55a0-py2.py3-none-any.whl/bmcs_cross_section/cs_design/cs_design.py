# from .cs_layout import CrossSectionLayout
from .cs_layout_dict import CrossSectionLayout
from .cs_shape import Rectangle, Circle, TShape, CustomShape, ICrossSectionShape, IShape
from bmcs_utils.api import Model, Item, View, EitherTypeEditor
import traits.api as tr
from bmcs_utils.api import \
    Float, EitherType, Instance
from bmcs_cross_section.matmod import \
    PWLConcreteMatMod, EC2PlateauConcreteMatMod, EC2ConcreteMatMod

class CrossSectionDesign(Model):
    name = 'Cross Section Design'

    matrix = EitherType(options=[
        ('EC2', EC2ConcreteMatMod),
        ('EC2 with plateau', EC2PlateauConcreteMatMod),
        ('piecewise linear', PWLConcreteMatMod),
        # ('EC2 softening tension', ConcreteMaterialModelAdv),
        ], MAT=True)

    cross_section_layout = Instance(CrossSectionLayout)

    def _cross_section_layout_default(self):
        return CrossSectionLayout(cs_design=self)

    depends_on = ['matrix', 'cross_section_layout', 'cross_section_shape']
    tree = ['matrix','cross_section_layout','cross_section_shape']

    csl = tr.Property()
    def _get_csl(self):
        return self.cross_section_layout

    H = tr.Property(Float)
    def _get_H(self):
        return self.cross_section_shape_.H
    def _set_H(self,value):
        self.cross_section_shape_.H = value

    cross_section_shape = EitherType(
                          options=[('rectangle', Rectangle),
                                    # ('circle', Circle),
                                   ('I-shape', IShape),
                                    ('T-shape', TShape),
                                   ('custom', CustomShape)],
                          CS=True, tree=True)

    ipw_view = View(
        Item('matrix', latex=r'\mathrm{Conc.~law}', editor=EitherTypeEditor(show_properties=False)),
        Item('cross_section_shape', latex=r'\mathrm{CS~shape}', editor=EitherTypeEditor(show_properties=False)),
    )

    def subplots(self, fig):
        return fig.subplots(1, 1)

    def update_plot(self, ax):
        self.cross_section_shape_.update_plot(ax)
        self.cross_section_layout.update_plot(ax)
