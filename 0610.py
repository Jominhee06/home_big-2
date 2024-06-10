#%%
# gugudan
class GuGuDan:
    dan_start = None
    dan_finish = None
    step_start = None
    step_finish = None
    
    def __init__(self):
        self.dan_start = 0
        self.dan_finish = 0
        self.step_start = 0
        self.step_finish = 0
        self.msg_lines = ''
    
    def set_Params(self,dan_start,dan_finish,step_start,step_finish):
        self.dan_start = dan_start
        self.dan_finish = dan_finish
        self.step_start = step_start
        self.step_finish = step_finish
    
    def calc_GuGuDan(self):
    # 세로로 구구단 작성 후 self.gugu_lines 문자열 저장
        self.msg_lines = f'{self.dan_start}*{self.step_start}'
    
   
    def calc_GuGuDan(self):
        # 세로로 구구단 작성 후 self.gugu_lines 문자열 저장
        lines = []
        for dan in range(self.dan_start,self.dan_finish + 1):            
            for step in range(self.step_start,self.step_finish + 1):
                   lines.append(f'{dan} * {step} = {dan * step}')
            lines.append('\t')
        self.msg_lines = '\n'.join(lines)
    print('--------gugudan-----------')

    
    def print_GuGuDan(self):
        print(self.msg_lines)


    def show_GuGuDan(self):
        print(self.msg_lines)

if __name__== '__main__':
    # gugu = GuGuDan()
    # gugu.set_Params(2,9,1,9)
    # gugu.calc_GuGuDan()
    # gugu.print_GuGuDan()

    gugu = GuGuDan()
    dan_start = 2
    dan_finish = 9
    step_start = 1
    step_finish = 9
    gugu.set_Params(dan_start,dan_finish,step_start,step_finish)
    gugu.calc_GuGuDan()
    # gugu.run_GuGuDan()
    gugu.show_GuGuDan()

# %%
