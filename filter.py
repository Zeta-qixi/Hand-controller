'''
滤波、数据处理
'''

class filter:
    def __init__(self):
        self.xy_list = []
        self.pose_list = []

    def add_data(self, **kwargs):
        self.xy_list.append(kwargs['xy'])
        self.pose.append(kwargs['pose'])

        

