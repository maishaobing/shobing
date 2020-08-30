import  pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS

my_style =LS('#333366',base_style=LCS)

chart = pygal.Bar(style = my_style,x_label_rotation=20,show_legend=False)

chart._title = 'python project'
chart.x_labels = ['httpie','django','flask']

plot_dict = [
    {'value':16101,'label':'Description of httpie.','xlink':'https://www.baidu.com'},
    {'value':15028,'label':'Description of django.','xlink':'https://www.taobao.com'},
    {'value':14798,'label':'Description of flask.','xlink':'https://www.jd.com'},
]

chart.add('',plot_dict)
chart.render_to_file("bar_description.svg")