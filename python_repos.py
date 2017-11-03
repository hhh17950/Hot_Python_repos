import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 执行API调用并存储响应
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
r = requests.get(url)
print("Status code: ", r.status_code)

# 将API响应存储于一个变量之中
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])
# 探索有关仓库的信息
repo_dicts = response_dict['items']
repo_counts = len(repo_dicts)
print("Repositories returned:", repo_counts)

names, plot_dicts = [], []
# 研究仓库信息
for repo_dict in repo_dicts:
    name = repo_dict['name']
    plot_dict = {'value': repo_dict['stargazers_count'],
                 'xlink': repo_dict['html_url'],
                 }
    plot_dicts.append(plot_dict)
    names.append(name)

# 对names，stars进行数据的可视化
# 这里的LS(LightenStyle)是调节颜色， LCS是基础颜色的高亮
my_style = LS('#333366', base_style=LCS)
# 改进图标的样式,我的布局
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_font_size = 18
my_config.truncate_label = 10
my_config.show_y_guides = False
my_config.width = 1000
chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Python-最受欢迎的项目仓库'
chart.x_labels = names
chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')