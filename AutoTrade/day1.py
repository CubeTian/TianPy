from atrader import *

def init(context:Context):
    # 设置初始资金为100万
    set_back(initial_cash=1000000)
    # 注册1min的数据
    reg_kdata(frequency='min',fre_num=1)

def on_data(context:Context):  
    # context.reg_kdata根据注册的先后顺序标记，0代表第一个注册的频率，为1min
    # 获取1min注册的数据，并获取50个最新的1min数据，并以dataframe的形式输出
    df_min = get_reg_data(reg_idx=context.reg_kdata[0],length=50,df=True)
    print(df_min)
if __name__ == '__main__':
    run_backtest(strategy_name='example_text',file_path='数据驱动.py',\
        target_list=['shfe.rb0000'],frequency='min',fre_num=15,\
            begin_date='2018-01-01',end_date='2018-06-30')
      