import datetime

# 更新README.md
with open('README.md', mode='a') as f:
  f.write(f'{datetime.datetime.now()}\n\n')