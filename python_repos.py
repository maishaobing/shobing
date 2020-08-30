#第十七章 使用webAPI
#17.1.1-17.1.4
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS
#执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:Go&sort=stars'
r =requests.get(url)
print("stars code",r.status_code)

#将API响应存储在一个变量中
response_dict = r.json()
#处理结果

# print(requests_dict.keys())

#17.1.1-17.1.4
#
print("Total respositories:",response_dict['total_count'])

#17.1.5探索有关仓库的信息

repo_dicts = response_dict['items']
print("Respositories returned:",len(repo_dicts))

#研究第一个仓库
# repo_dict = repo_dicts[0]
# print("\nKeys:",len(repo_dict))
# for key in sorted(repo_dict.keys()):
#     print(key)
#print("\nselected infomation about each respository:")
#17.1.6-17.1.7概述最受欢饮的仓库
# for repo_dict in repo_dicts:
#     print('Name:',repo_dict['name'])
#     print('Owner:',repo_dict['owner']['login'])
#     print('Stars:',repo_dict['stargazers_count'])
#     print('Respository:',repo_dict['html_url'])
#     print('Created:',repo_dict['created_at'])
#     print('Updated:',repo_dict['updated_at'])
#     print('Description:',repo_dict['description'])
#

#17.2.0使用pygal可视化仓库
#
# names,stars =[],[]
# for repo_dict in repo_dicts:
#     names.append(repo_dict['name'])
#     stars.append(repo_dict['stargazers_count'])
#
# my_style =LS('#333366',base_style=LCS)
# chart = pygal.Bar(style = my_style,x_label_rotation=20,show_legend=False)
# chart.title = 'Most - Starred python projects on GitHub'
# chart.x_labels =names
#
# chart.add('',stars)
# chart.render_to_file('python_repos.svg')
#17.2.1改进pygal图标

names = []
# stars=[]
plot_dicts =[]
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    # stars.append(repo_dict['stargazers_count'])
    plot_dict ={
        'value':repo_dict['stargazers_count'],
        'label':str(repo_dict['description']),
        'xlink': repo_dict['html_url'],
    }
    plot_dicts.append(plot_dict)
#可视化
my_style =LS('#333366',base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend =False
my_config.title_font_siza =24
my_config.label_font_size =14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config,style = my_style)
chart.title = 'Most - Starred python projects on GitHub'
chart.x_labels =names

chart.add('',plot_dicts)
chart.render_to_file('Go_repos2.svg')