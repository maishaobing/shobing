
#第十七章17.3Hacker NewAPl

import requests
from operator import itemgetter
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS

#执行Apl调用并存储响应
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)

# print("Status code:",r.status_code)

#处理有关每篇文章的信息
submission_ids = r.json() #将调用的内容转为json格式
submission_dicts = []
for submission_id in submission_ids[:30]:
    #对于每篇文章，都执行一个APi调用
     url = ('https://hacker-news.firebaseio.com/v0/item/' + str(submission_id) + '.json')
     submission_r = requests.get(url)
     # print(submission_r.status_code)
     response_dict = submission_r.json()

     submission_dict ={
        'title':response_dict['title'],
        'link':'https://news.ycombinator.com/item?id=' + str(submission_id),
        'comments':response_dict.get('descendants',0)
     }
     submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts,key=itemgetter('comments'),reverse=True)
titles,commets =[],[]
for submission_dict in submission_dicts:
    # print('\nTitle:',submission_dict['title'])
    # print('\nLink:', submission_dict['link'])
    # print('\nComment:', submission_dict['comment'])
    titles.append(response_dict['title'])
    commets.append(response_dict.get('descendants',0))

    #图形可视化
my_style = LS('#333366',base_style=LCS)
chart = pygal.Bar(my_style=my_style,x_label_rotation=45,show_legend=False)
chart.title="first do it!"
chart.x_labels=titles
chart.add('',commets)
chart.render_to_file('firsttest.svg')


# titles,comment_dicts =[],[]
# for submission_dict in submission_dicts:
#     # print('\nTitle:',submission_dict['title'])
#     # print('\nLink:', submission_dict['link'])
#     # print('\nComment:', submission_dict['comment'])
#     titles.append(response_dict['title'])
#     comment_dict={
#         "comments":response_dict['descendants],
#         "url":response_dict['url']
#     }
# comment_dicts.append(comment_dict)
#     #图形可视化
# my_style = LS('#333366',base_style=LCS)
# chart = pygal.Bar(my_style=my_style,x_label_rotation=45,show_legend=False)
# chart.title="first do it!"
# chart.x_labels=titles
# chart.add('',comment_dicts)
# chart.render_to_file('firsttest.svg')


