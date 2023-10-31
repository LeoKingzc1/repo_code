import gradio as gr
from src.ui_fun import *
from src.fun_csv import *

def create_ui():
    with gr.Blocks() as demo:
        gr.Markdown(
        """
        # 智能财报分析系统
        """)
        with gr.Tab("PDF文件处理"):
                file = gr.File(label="请上传PDF文件", file_types=['pdf'])
                with gr.Row(equal_height=True):
                  with gr.Column():
                    with gr.Row():
                      with gr.Column():
                        p_s_profit = gr.Textbox(label = '利润表起始页码', info="请输入起始页码")
                        p_e_profit = gr.Textbox(label = '终止页码', info="请输入终止页码(如果是单页，请输入相同页码即可)")
                      with gr.Column():
                        p_s_balance = gr.Textbox(label = '资产负债表起始页码', info="请输入起始页码")
                        p_e_balance = gr.Textbox(label = '终止页码', info="请输入终止页码(如果是单页，请输入相同页码即可)")
                      with gr.Column():
                        p_s_flow = gr.Textbox(label = '现金流量表起始页码', info="请输入起始页码")
                        p_e_flow = gr.Textbox(label = '终止页码', info="请输入终止页码(如果是单页，请输入相同页码即可)")
        
                button1 = gr.Button("匹配")
                with gr.Column():
                  with gr.Row(equal_height=True) :
                    # profit_options = gr.CheckboxGroup(label = '请选择需要列')
                    profit_dataframe = gr.HTML()
        
                  with gr.Row(equal_height=True) :
                    # balance_options = gr.CheckboxGroup(label = '请选择需要的列')
                    balance_dataframe = gr.HTML()
        
                  with gr.Row(equal_height=True) :
                    # flow_options = gr.CheckboxGroup(label = '请选择需要列')
                    flow_dataframe = gr.HTML()
        
                  numbers = gr.CheckboxGroup(label = '选择需要列的序号')
                  numbers = gr.Textbox(label = '请选择需要列的序号', info="从1开始计数")
                  button2 = gr.Button("下载")
                  csv = gr.File(interactive=False, visible=False)
        
                button1.click(mock_ocr, [file,p_s_profit, p_e_profit,p_s_balance, p_e_balance, p_s_flow, p_e_flow], [profit_dataframe,balance_dataframe,flow_dataframe])
                button2.click(export_csv, [profit_dataframe, balance_dataframe, flow_dataframe,numbers], csv)
        with gr.Tab("Excel文件处理"):
                file_csv = gr.File(label="请上传PDF文件", file_types=['xlsx','csv'])
                with gr.Row(equal_height=True):
                  with gr.Column():
                    with gr.Row():
                      with gr.Column():
                        sheet_profit = gr.Dropdown(label = '利润表名称', allow_custom_value = False,interactive = True,multiselect = False)
                        file_csv.change(read_excel, [file_csv], [sheet_profit])
                        # sheet_profit = gr.Textbox(label = '利润表名称', info="请输入利润表名称")
                        row_p = gr.Textbox(label = '属性行号', info="请输入属性行号")
                      with gr.Column():
                        sheet_balance = gr.Dropdown(label = '资产负债表名称', allow_custom_value = False,interactive = True,multiselect = False)
                        file_csv.change(read_excel, [file_csv], [sheet_balance])
                        # sheet_balance = gr.Textbox(label = '资产负债表名称', info="请输入资产负债表名称")
                        row_b = gr.Textbox(label = '属性行号', info="请输入属性行号")
                      with gr.Column():
                        sheet_flow = gr.Dropdown(label = '现金流量表名称', allow_custom_value = False,interactive = True,multiselect = False)
                        file_csv.change(read_excel, [file_csv], [sheet_flow])
                        # sheet_flow = gr.Textbox(label = '现金流量表名称', info="请输入现金流量表名称")
                        row_f = gr.Textbox(label = '属性行号', info="请输入属性行号")
                # sheet = [sheet_profit, row_p, sheet_balance, row_b, sheet_flow, row_f]
                button1 = gr.Button("匹配")
                with gr.Column():
                  attrs_profit = gr.Dropdown(label = '利润表属性', allow_custom_value = False,interactive = True,multiselect = True)
                  with gr.Row(equal_height=True) :
                    # profit_options = gr.CheckboxGroup(label = '请选择需要列')
                    # attrs_profit = gr.Dropdown(label = '利润表属性', allow_custom_value = False,interactive = True,multiselect = True)
                    profit_dataframe = gr.HTML()
                    profit_dataframe.change(read_df, [profit_dataframe], [attrs_profit])
        
                  attrs_balance = gr.Dropdown(label = '资产负债表属性', allow_custom_value = False,interactive = True,multiselect = True)
                  with gr.Row(equal_height=True) :
                    # balance_options = gr.CheckboxGroup(label = '请选择需要的列')
                    # attrs_balance = gr.Dropdown(label = '资产负债表属性', allow_custom_value = False,interactive = True,multiselect = True)
                    balance_dataframe = gr.HTML()
                    balance_dataframe.change(read_df, [balance_dataframe], [attrs_balance])
        
                  attrs_flow = gr.Dropdown(label = '现金流量表属性', allow_custom_value = False,interactive = True,multiselect = True)
                  with gr.Row(equal_height=True) :
                    # flow_options = gr.CheckboxGroup(label = '请选择需要列')
                    # attrs_flow = gr.Dropdown(label = '现金流量表属性', allow_custom_value = False,interactive = True,multiselect = True)
                    flow_dataframe = gr.HTML()
                    flow_dataframe.change(read_df, [flow_dataframe], [attrs_flow])
        
                  numbers = gr.CheckboxGroup(label = '选择需要列的序号')
                  numbers = gr.Textbox(label = '请选择需要列的序号', info="从1开始计数")
                  button2 = gr.Button("下载")
                  csv = gr.File(interactive=False, visible=False)
                button1.click(sep_df, [file_csv, sheet_profit, row_p, sheet_balance, row_b, sheet_flow, row_f],[profit_dataframe, balance_dataframe, flow_dataframe])
                button2.click(export_csv, [attrs_profit, profit_dataframe, attrs_balance, balance_dataframe, attrs_flow, flow_dataframe], csv)

    return demo
